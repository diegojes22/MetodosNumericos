import tkinter
import customtkinter as ctk

from panels.modelSelection import ModelMediator, ModelObserver, Model, BISECCION, NEWTON_RAPHSON, PY_TOOL
from panels.const import *
from panels.basic import add_image_to_button, center_window

from logic.biseccion.function import Function, FunctionMediator, FunctionObserver
import logic.biseccion.logic as lo
from logic.newton_raphson.logic import newton_raphson_method
from logic.newton_raphson.logic import ProcessReference

import os

class ResultsArea(ctk.CTkFrame, FunctionObserver, ModelObserver):
    def __init__(self, master, function_mediator: FunctionMediator, model_mediator: ModelMediator, **kwargs):
        ''' Constructor'''
        super().__init__(master, **kwargs)
        self.function_mediator = function_mediator
        self.model_mediator = model_mediator

        self.function_mediator.register(self)
        self.register(None)

        self.elements : list[float] = function_mediator.function.get_real_roots()
        self._config_grid()
        self._add_widgets()

        self.bind("<Destroy>", lambda e: self.destructor())

    # widgets methods
    def _add_widgets(self):
        ''' Adds the widgets to the panel '''
        self._add_nav_buttons()
        self._add_scroll_area()

    def _add_nav_buttons(self):
        ''' Left and right navigation buttons '''
        self.left_button = ctk.CTkButton(
            self,
            text="<",
            width=45,
            height=45,
            font=ctk.CTkFont(size=20, weight=BOLD),
            command=lambda: self._scroll(-100)  # move left
        )
        self.left_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.right_button = ctk.CTkButton(
            self,
            text=">",
            width=45,
            height=45,
            font=ctk.CTkFont(size=20),
            command=lambda: self._scroll(100)  # move right
        )
        self.right_button.grid(row=0, column=4, padx=5, pady=5, sticky="e")

    def _add_scroll_area(self):
        ''' Central frame with scrollable content '''
        self.scroll_frame = ctk.CTkScrollableFrame(self, orientation="horizontal", height=50)
        self.scroll_frame.grid(row=0, column=1, columnspan=3, sticky="ew", padx=5, pady=5)

        # get internal canvas
        self.canvas = self.scroll_frame._parent_canvas
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Append elements
        for i, el in enumerate(self.elements):
            lbl = ctk.CTkLabel(
                self.scroll_frame, 
                text=f"x{i} = {el}", 
                width=150, 
                height=40, 
                fg_color=("#190CCE", "#3A3A3A"), 
                bg_color="transparent",
                corner_radius=8,
                font=ctk.CTkFont(size=16, weight=BOLD)
            )
            lbl.grid(row=0, column=i, padx=10, pady=10)

    def add_solutions(self):
        # Append elements
        for i, el in enumerate(self.elements):
            lbl = ctk.CTkLabel(
                self.scroll_frame, 
                text=f"x{i} = {el}", 
                width=150, 
                height=40, 
                fg_color=("#190CCE", "#3A3A3A"), 
                bg_color="transparent",
                corner_radius=8,
                font=ctk.CTkFont(size=16, weight=BOLD)
            )

    def _scroll(self, delta):
        """ Scroll the canvas horizontally"""
        self.canvas.xview_scroll(int(delta / 2), "units")

    def _update_widgets(self):
        ''' Updates the displayed widgets with the new elements '''
        for widget in self.winfo_children():
            widget.destroy()

        self._add_widgets()

    def _config_grid(self):
        ''' 
        Configures the grid layout of the panel 

        +---+------+------+------+---+ 
        |   |      |      |      |   | 
        +---+------+------+------+---+ 
        
        is a grid with 1 row and 5 columns 
        '''

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure(4, weight=0)

    # Interface methods
    def update(self, function: Function):
        ''' Updates the results area when the function changes '''
        self.elements = function.get_real_roots()
        self._update_widgets()

    def destructor(self):
        ''' Destructor'''
        self.function_mediator.remove_observer(self)
        self.unregister(None)

    def update(self, model: Model):
        pass

    def unregister(self, model: Model):
        self.model_mediator.remove_model_observer(self)

    def register(self, model: Model):
        self.model_mediator.register(self)

class ResultsPanel(ctk.CTkToplevel, FunctionObserver):
    def __init__(self, master, function_mediator : FunctionMediator, model_mediator: ModelMediator, **kwargs):
        ''' Contructor '''
        super().__init__(master, **kwargs)
        self.function_mediator : FunctionMediator = function_mediator
        self.model_mediator = model_mediator
        self.custom_range : tuple[float, float] = None

        self.function_mediator.register(self)
        self.model_mediator.register(self)

        self._add_widgets()

        self.bind("<Destroy>", lambda e: self.destructor())

    def set_custom_range(self, min: float, max : float):
        '''
        Cuando el analizador de rangos no logra detectar los rangos de forma
        automatica, el usuario puede definir un rango personalizado.

        Esto se pasa de forma manual a travez de este metodo y se guarda en una
        tupla
        '''
        self.custom_range = (min, max)

    def get_custom_range(self) -> tuple[float, float]:
        '''
        Devuelve el rango personalizado definido por el usuario.
        Tal vez se quite porque no creo que sea necesario.
        '''
        return self.custom_range

    def destructor(self):
        ''' Destructor'''
        self.function_mediator.remove_observer(self)
        self.model_mediator.remove_model_observer(self)

    # widgets methods
    def _add_widgets(self):
        self.minsize(800, 600)
        center_window(self, 800, 600)
        self.title_label = ctk.CTkLabel(self, text="RESULTADOS", font=ctk.CTkFont(size=SUBTITLE_SIZE, weight=BOLD))
        self.title_label.pack(pady=10)

        self._add_solution_area()
        self._add_text_table()

    def _add_solution_area(self):
        self.results_area = ResultsArea(self, self.function_mediator, model_mediator=self.model_mediator, height=80, width=300)
        self.results_area.pack(pady=10, padx=10, fill="x")

    def _add_text_table(self):
        self.table = ctk.CTkTextbox(self, width=400, height=200, font=ctk.CTkFont(size=16), wrap="none")
        self.table.pack(pady=10, padx=10, fill="both", expand=True)

    def add_procedure_in_table(self, procedure: str):
        self.table.insert("0.0", procedure)

    def append_procedure_in_table(self, procedure: str):
        self.table.insert("end", procedure)

    def clear_table(self):
        self.table.delete("0.0", "end")

    def solver(self):
        model_name = self.model_mediator.get_model()
        self.function_mediator.function.clear_roots()

        print(model_name)
        if model_name == BISECCION:
            self.by_bisection()
        elif model_name == NEWTON_RAPHSON:
            self.by_newton_raphson()
        elif model_name == PY_TOOL:
            self.function_mediator.function.absolute_solver()
        else:
            tkinter.messagebox.showerror("Error", "Método no implementado")

        self.results_area.add_solutions()
        self.results_area._update_widgets()

    def by_bisection(self):
        function = self.function_mediator.function
        process = ProcessReference()

        intervals = lo.get_intervals(function)

        if self.custom_range is not None:
            a, b = self.custom_range

            root = lo.biseccion(function, a, b, 100, procedure=process)
            if root is not None:
                function.append_real_root(root)

                self.function_mediator.notify_observers()

                self.clear_table()
                self.add_procedure_in_table(process.get())
                return;
            

        for interval in intervals:
            a, b = interval
            root = lo.biseccion(function, a, b, 100, procedure=process)

            function.append_real_root(root)
            '''
            if root is not None:
                print(f"Root found in interval [{a}, {b}]: {root}")
                function.append_real_root(root)
            else:
                print(f"No root found in interval [{a}, {b}]")
            '''
            process.append(f"Root found in interval [{a}, {b}]: {root}\n" if root is not None else f"No root found in interval [{a}, {b}]\n")
            process.append("\n")
        self.function_mediator.notify_observers()
        #self.function_mediator.function.absolute_solver()

        self.clear_table()
        self.add_procedure_in_table(process.get())

    def by_newton_raphson(self):
        function = self.function_mediator.function
        process = ProcessReference()

        intervals = lo.get_intervals(function)

        if self.custom_range is not None:
            a = self.custom_range[0]

            try:
                root = newton_raphson_method(function, a, procedure=process)
                function.append_real_root(root)

                process.append(f"Root found aprox {a}: {root}\n" if root is not None else f"No root found aprox {a}\n")
                process.append("\n")
                self.function_mediator.notify_observers()

                self.clear_table()
                self.add_procedure_in_table(process.get())
                return
            except ValueError as e:
                print(f"No root found aprox {a}: {e}")

        for interval in intervals:
            a = interval[0]

            try:
                root = newton_raphson_method(function, a, procedure=process)
                function.append_real_root(root)
            except ValueError as e:
                print(f"No root found aprox {a}: {e}")

            process.append(f"Root found aprox {a}: {root}\n" if root is not None else f"No root found aprox {a}\n")
            process.append("\n")

        self.function_mediator.notify_observers()
        #self.function_mediator.function.absolute_solver()

        self.clear_table()
        self.add_procedure_in_table(process.get())

    def by_absolute_solver(self):
        self.function_mediator.function.absolute_solver()
        self.function_mediator.notify_observers()
        self.table.config(font=ctk.CTkFont(size=20, weight=BOLD))
        self.clear_table()
        self.add_procedure_in_table("No es posible ver el procedimiento con el modelo actual\n debido a que no cuenta con subcripcion premium.\n")

    def show(self):
        self.grab_set()
        self.master.wait_window(self)

    # Interface methods
    def update(self, function: Function):
        pass

    def update(self, model: Model):
        pass

    def unregister(self, model: Model):
        self.model_mediator.unregister(self)

    def register(self, model: Model):
        self.model_mediator.register(self)