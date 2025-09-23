import customtkinter as ctk

from logic.biseccion.function import FunctionMediator, FunctionObserver
from panels.color_picker import ask_color
from panels.basic import add_image_to_button

import random
import os

### Panels for graphing functions ###
class GraphControls(ctk.CTkFrame, FunctionObserver):
    def __init__(self, master, mediator: FunctionMediator, **kwargs):
        ''' Constructor'''
        super().__init__(master, **kwargs)
        self.mediator : FunctionMediator = mediator
        self.mediator.register(self)
        self.master = master

        self.graph_panel = None

        self._config()
        self._define_widgets()

    def __del__(self):
        ''' Destructor '''
        self.mediator.remove_observer(self)

    # Setters
    def set_graph_panel(self, graph_panel):
        self.graph_panel = graph_panel

    # Getters
    def get_graph_panel(self):
        return self.graph_panel

    # Events
    def zoom_in(self):
        if self.graph_panel is not None:
            current_scale = self.graph_panel.get_scale()
            new_scale = current_scale + 5

            if new_scale > 1000:
                new_scale = 1000

            self.graph_panel.set_scale(new_scale)
            self.graph_panel.paint_graph()

    def zoom_out(self):
        if self.graph_panel is not None:
            current_scale = self.graph_panel.get_scale()
            new_scale = current_scale - 5

            if new_scale < 1:
                new_scale = 1

            self.graph_panel.set_scale(new_scale)
            self.graph_panel.paint_graph()

    def move_left(self):
        if self.graph_panel is not None:
            current_center = self.graph_panel.get_center()
            new_center = (current_center[0] + 10, current_center[1])
            self.graph_panel.set_center(new_center)
            self.graph_panel.paint_graph()

    def move_right(self):
        if self.graph_panel is not None:
            current_center = self.graph_panel.get_center()
            new_center = (current_center[0] - 10, current_center[1])
            self.graph_panel.set_center(new_center)
            self.graph_panel.paint_graph()

    def move_up(self):
        if self.graph_panel is not None:
            current_center = self.graph_panel.get_center()
            new_center = (current_center[0], current_center[1] + 10)
            self.graph_panel.set_center(new_center)
            self.graph_panel.paint_graph()

    def move_down(self):
        if self.graph_panel is not None:
            current_center = self.graph_panel.get_center()
            new_center = (current_center[0], current_center[1] - 10)
            self.graph_panel.set_center(new_center)
            self.graph_panel.paint_graph()

    def goto_center(self):
        if self.graph_panel is not None:
            self.graph_panel.recalculate_center()
            self.graph_panel.paint_graph()

    def change_color(self):
        new_color = ask_color(self.master, self.graph_panel.get_function_color() if self.graph_panel is not None else "#005eff")

        if new_color is not None and self.graph_panel is not None:
            self.graph_panel.set_function_color(new_color)
            self.graph_panel.paint_graph()

    # Private methods
    def _define_widgets(self):
        self.HEIGHT_BUTTON = 40

        self._add_zoom_buttons()
        self._add_color_paint_button()

        self._add_move_buttons()

    def _add_zoom_buttons(self):
        self.zoom_in_button = ctk.CTkButton(self, text="", command=self.zoom_in, height=self.HEIGHT_BUTTON)
        self.zoom_in_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.zoom_in_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "zoom_in_40p.png")
        ), (40,40))

        self.zoom_out_button = ctk.CTkButton(self, text="", command=self.zoom_out)
        self.zoom_out_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.zoom_out_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "zoom_out_40p.png")
        ), (40,40))

    def _add_move_buttons(self):
        self.move_left_button = ctk.CTkButton(self, text="", command=self.move_left)
        self.move_left_button.grid(row=0, column=5, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.move_left_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "left.png")
        ), (40,40))

        self.move_right_button = ctk.CTkButton(self, text="", command=self.move_right)
        self.move_right_button.grid(row=0, column=6, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.move_right_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "right.png")
        ), (40,40))

        self.move_up_button = ctk.CTkButton(self, text="", command=self.move_up)
        self.move_up_button.grid(row=0, column=7, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.move_up_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "up.png")
        ), (40,40))

        self.move_down_button = ctk.CTkButton(self, text="", command=self.move_down)
        self.move_down_button.grid(row=0, column=8, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.move_down_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "down.png")
        ), (40,40))

        self.center_button = ctk.CTkButton(self, text="", command=self.goto_center)
        self.center_button.grid(row=0, column=10, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.center_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "center_focus.png")
        ), (40,40))

    def _add_color_paint_button(self):
        self.paint_button = ctk.CTkButton(self, text="", command=self.change_color)
        self.paint_button.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", )
        add_image_to_button(self.paint_button, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "palette_40p.png")
        ), (40,40))

    def _config(self):
        self._config_grid()
        self.configure(fg_color="#212121")

    def _config_grid(self):
        ''' 
        Configures the grid layout of the panel 
        
        Example layout:
        +---+---+---+---+---+---+---+---+---+---+---+
        |   |   |   |   |   |   |   |   |   |   |   |
        +---+---+---+---+---+---+---+---+---+---+---+
        is a grid with 1 row and 11 columns
        '''
        # config the only row
        self.grid_rowconfigure(0, weight=1)

        # config the columns
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)

    # Interface methods
    def update(self, function):
        pass

class GraphPanel(ctk.CTkFrame, FunctionObserver):
    def __init__(self, master, mediator : FunctionMediator, function_color = "#005eff", scale=30, **kwargs):
        ''' Constructor'''
        super().__init__(master, **kwargs)
        self.mediator : FunctionMediator = mediator
        self.function_color = function_color
        self.scale = scale

        self.center = (0, 0)

        self.mediator.register(self)
        self._define_canvas()

    # Getters
    def recalculate_center(self):
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.center = (width // 2, height // 2)
        return self.center

    def get_center(self):
        return self.center
    
    def get_function_color(self):
        return self.function_color
    
    def get_scale(self):
        return self.scale
    
    def get_canvas(self):
        return self.canvas

    # Setters
    def set_random_function_color(self):
        r = lambda: random.randint(0,255)
        self.function_color = f'#{r():02x}{r():02x}{r():02x}'
    
    def set_function_color(self, color: str):
        self.function_color = color

    def set_scale(self, scale: int):
        self.scale = scale

    def set_center(self, center: tuple):
        self.center = center
    

    # Private methods
    def _define_canvas(self):
        self.canvas = ctk.CTkCanvas(self, bg="#212121", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    # Graphing methods
    def paint_graph(self):
        ''' Draw all components of the graph in the canvas '''
        self.clear_canvas()

        self.get_center()
        self.draw_ejes()

        self.draw_function()

    def draw_ejes(self):
        ''' Draw the X and Y axes in the canvas '''
        self.canvas.create_line(0, self.center[1], self.canvas.winfo_width(), self.center[1], fill="#a6072c", width=3)   # Eje X
        self.canvas.create_line(self.center[0], 0, self.center[0], self.canvas.winfo_height(), fill="#2c730b", width=3)  # Eje Y

    def clear_canvas(self):
        ''' Clear all drawings in the canvas '''
        self.canvas.delete("all")

    def draw_function(self):
        func = self.mediator.function

        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        prev_x = None
        prev_y = None

        for pixel_x in range(0, width):
            x = (pixel_x - self.center[0]) / self.scale  # Convertir coordenada de píxel a coordenada matemática
            try:
                y = func.evaluate(x)  # Evaluar la función en x
                pixel_y = self.center[1] - (y * self.scale)  # Convertir coordenada matemática a coordenada de píxel

                if prev_x is not None and prev_y is not None:
                    self.canvas.create_line(prev_x, prev_y, pixel_x, pixel_y, fill=self.function_color, width=3)  # Dibujar línea entre puntos

                prev_x = pixel_x
                prev_y = pixel_y
                
            except Exception as e:
                # Si hay un error al evaluar la función, simplemente saltar ese punto
                prev_x = None
                prev_y = None

    # Interface methods
    def update(self, function):
        self.paint_graph()


### Window for graphing functions ###
class GraphDialog(ctk.CTkToplevel):
    def __init__(self, master, mediator: FunctionMediator, **kwargs):
        super().__init__(master, **kwargs)

        self.mediator : FunctionMediator = mediator
        
        self._config()
        self._define_widgets()

    def _define_widgets(self):
        self.graphPanel : GraphPanel = GraphPanel(self, self.mediator)
        self.graphPanel.pack(fill="both", expand=True)
        self.graphPanel.set_random_function_color()

        self.graphControls : GraphControls = GraphControls(self, self.mediator, height=100)
        self.graphControls.pack(fill="x")
        self.graphControls.set_graph_panel(self.graphPanel)

    def _config(self):
        self.title("Graph Dialog")
        self.geometry("600x400")
        self.minsize(400, 300)

    def show(self):
        self.graphPanel.get_canvas().bind("<Configure>", lambda ev: self.graphPanel.paint_graph())
        self.graphPanel.recalculate_center()
        self.graphPanel.paint_graph()
