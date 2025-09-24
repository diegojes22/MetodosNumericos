import customtkinter as ctk
from panels.const import *
from logic.biseccion.function import Function, FunctionMediator, FunctionObserver
import logic.biseccion.logic as lo

from panels.basic import add_image_to_button

import os

class ResultsArea(ctk.CTkFrame, FunctionObserver):
    def __init__(self, master, function_mediator: FunctionMediator, **kwargs):
        ''' Constructor'''
        super().__init__(master, **kwargs)
        self.function_mediator = function_mediator
        self.function_mediator.register(self)
        self.elements : list[float] = function_mediator.function.get_real_roots()
        self._config_grid()
        self._add_widgets()

        self.bind("<Destroy>", lambda e: self.destructor())

    def destructor(self):
        ''' Destructor'''
        self.function_mediator.remove_observer(self)

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

    def _scroll(self, delta):
        """ Scroll the canvas horizontally"""
        self.canvas.xview_scroll(int(delta / 2), "units")

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

    def _update_widgets(self):
        ''' Updates the displayed widgets with the new elements '''
        for widget in self.winfo_children():
            widget.destroy()

        self._add_widgets()

class ResultsPanel(ctk.CTkToplevel, FunctionObserver):
    def __init__(self, master, function_mediator : FunctionMediator, **kwargs):
        ''' Contructor '''
        super().__init__(master, **kwargs)
        self.function_mediator : FunctionMediator = function_mediator
        self.function_mediator.register(self)

        self._add_widgets()

        self.bind("<Destroy>", lambda e: self.destructor())

    def destructor(self):
        ''' Destructor'''
        self.function_mediator.remove_observer(self)

    # widgets methods
    def _add_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="RESULTADOS", font=ctk.CTkFont(size=SUBTITLE_SIZE, weight=BOLD))
        self.title_label.pack(pady=10)

        self._add_solution_area()

    def _add_solution_area(self):
        self.results_area = ResultsArea(self, self.function_mediator, height=80, width=300)
        self.results_area.pack(pady=10, padx=10, fill="x")

    def solver(self):
        function = self.function_mediator.function

        intervals = lo.get_intervals(function)

        for interval in intervals:
            a, b = interval
            root = lo.biseccion(function, a, b, 1000)
            if root is not None:
                print(f"Root found in interval [{a}, {b}]: {root}")
                function.append_real_root(root)
            else:
                print(f"No root found in interval [{a}, {b}]")
        self.function_mediator.notify_observers()

    def show(self):
        self.grab_set()
        self.master.wait_window(self)

    # Interface methods
    def update(self, function: Function):
        pass