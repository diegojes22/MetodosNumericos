'''
This module contains the PromptPanel class, which is a custom Tkinter frame
for user input of mathematical functions. It includes an input area for the
function expression and a button to submit the input.

Design in Figma: https://www.figma.com/design/pDC9BuB5fXu5lWfgEwzTBh/BiseccionGrapInterface?node-id=0-1&t=aKpFX2sonbDXfVj2-0
'''

# Imports
import customtkinter as ctk
from tkinter import messagebox
from panels import const
from panels.graph import GraphDialog
from panels.basic import add_image_to_button, center_window
from panels.results import ResultsPanel
from panels.modelSelection import ModelSelectionPanel, ModelMediator, ModelObserver

from panels.custom_range_dialog import DialogoNumeros
from panels.secret import SecretDialog

import os
from PIL import Image

from logic.biseccion.function import Function, FunctionMediator, FunctionObserver

# Classes
class PromptInputArea(ctk.CTkFrame):
    ''' A frame containing an input field for the function expression '''
    def __init__(self, root, function_mediator: FunctionMediator, model_mediator : ModelMediator, **kwargs):
        ''' Constructor '''
        super().__init__(root, **kwargs)
        self.root = root
        self.model_mediator = model_mediator
        self.function_mediator = function_mediator
        self._add_widgets()

        # Other attributes here if needed

    def _add_widgets(self):
        ''' Adds and configures the widgets in the input area '''
        self._add_title()

        # this is the input field for the function expression
        # the style is very smilar to the style of ChatGPT input field
        self.input_field = ctk.CTkEntry(self, 
                                        placeholder_text="f(x) = ", 
                                        width=400,
                                        height=40, 
                                        font=ctk.CTkFont(size=const.SUBTITLE_SIZE, family=const.DEFAULT_FONT_FAMILY),
                                        border_width=3, 
                                        corner_radius=8
                                        )
        self.input_field.pack(pady=(0, 20), padx=20)
        self.input_field.pack_propagate(False)
        self.input_field.bind("<KeyRelease>", lambda e: self.on_input_change())

        self._add_action_btns()

    # Widgets representation methods
    def _add_title(self):
        # adding an icon to the title
        img_path = os.path.join(os.path.dirname(__file__), "..", "sources", "img", "icon.ico")
        img_path = os.path.abspath(img_path)
        icon_img = ctk.CTkImage(light_image=Image.open(img_path), size=(40, 40))

        # title label
        self.label_title = ctk.CTkLabel(self, 
                                        text="Problema", 
                                        font=ctk.CTkFont(size=const.TITLE_SIZE, weight=const.BOLD, family=const.DEFAULT_FONT_FAMILY),
                                        image=icon_img, 
                                        compound="left",
                                        )
        self.label_title.pack(pady=(20, 10))

    def _add_action_btns(self):
        ''' Adds the resolve button to the input area '''
        # Icons for the buttons
        img_path = os.path.join(os.path.dirname(__file__), "..", "sources", "img", "chart_24p.png")
        img_path = os.path.abspath(img_path)
        chart_icon = ctk.CTkImage(light_image=Image.open(img_path), size=(24, 24))

        img_path = os.path.join(os.path.dirname(__file__), "..", "sources", "img", "calculate_24p.png")
        img_path = os.path.abspath(img_path)
        calculate_icon = ctk.CTkImage(light_image=Image.open(img_path), size=(24, 24))

        # area for the buttons
        self.btn_area = ctk.CTkFrame(self, 
                                     fg_color="transparent", 
                                     bg_color="transparent",
                                     width=400,
                                    )
        self.btn_area.pack(pady=(0, 10))

        # button for graphical representation of the function
        self.graph_func_btn = ctk.CTkButton(self.btn_area, 
                                     text="Graficar",
                                     command=self.on_graph,
                                     width=150,
                                     height=40,
                                     font=ctk.CTkFont(size=const.SUBTITLE_SIZE, family=const.DEFAULT_FONT_FAMILY),
                                     image=chart_icon,
                                     compound="left"
                                    )
        self.graph_func_btn.pack(side="right", padx=10)

        self.resolve_btn = ctk.CTkButton(self.btn_area, 
                                         text="Resolver",
                                         command=self.on_resolve,
                                         width=150,
                                         height=40,
                                         font=ctk.CTkFont(size=const.SUBTITLE_SIZE, family=const.DEFAULT_FONT_FAMILY),
                                         image=calculate_icon,
                                         compound="left"
                                        )
        self.resolve_btn.pack(side="left", padx=10)


    ### events ###
    def on_graph(self):
        graph : GraphDialog = GraphDialog(self.root, self.function_mediator)
        graph.show()
        #graph.grab_set()
        #self.root.wait_window(graph)

    def on_resolve(self):
        results_panel = ResultsPanel(self.root, self.function_mediator, self.model_mediator)
        if self.root.custom_range is not None:
            results_panel.set_custom_range(min=self.root.custom_range[0], max=self.root.custom_range[1])
        results_panel.solver()
        results_panel.show()
        self.root.custom_range = None

    def on_input_change(self):
        ''' Event handler for input field changes '''
        new_expression = self.input_field.get()

        try:
            new_function = Function(new_expression)
            self.function_mediator.set_function(new_function)
        except Exception as e:
            print(f"Invalid function expression: {e}")
            print(e.__traceback__)


class PromptPanel(ctk.CTkFrame, FunctionObserver):
    ''' 
    A custom Tkinter frame for user input of mathematical functions.
    This method implements the Mediator pattern to update the input field
    and other components when the function changes.
    '''
    def __init__(self, root, mediator: FunctionMediator, **kwargs):
        super().__init__(root, **kwargs)
        self.root = root
        self.function_mediator: FunctionMediator = mediator
        self.model_mediator : ModelMediator = ModelMediator()

        self.custom_range : tuple[float, float] = None

        self.function_mediator.register(self)

        self._add_widgets()

    # If you can't understand this method, please read about the Mediator pattern
    def update(self, function: Function):
        pass

    # Widgets representation methods
    def _config_grid(self):
        ''' 
        Configures the grid layout of the panel 
        
        Example layout:
        +---+---+---+---+---+
        | B |   |   |   |   |
        +---+---+---+---+---+
        |   |   |   |   |   |
        +---+---+---+---+---+
        |   |   | I |   |   |
        +---+---+---+---+---+
        |   |   |   |   | R |
        +---+---+---+---+---+
        |   |   |   |   | H |
        +---+---+---+---+---+

        is a grid with 5 rows and 5 columns
        '''
        # rows
        self.grid_rowconfigure((0), weight=1)        # button here
        self.grid_rowconfigure((1), weight=3)        # space here
        self.grid_rowconfigure((2), weight=4)        # main area here
        self.grid_rowconfigure((3), weight=3)        # space here
        self.grid_rowconfigure((4), weight=1)        # button here

        # columns
        self.grid_columnconfigure((0, 1, 3, 4), weight=1)
        self.grid_columnconfigure((2), weight=2)

    def _add_widgets(self):
        ''' Adds and configures the widgets in the panel '''
        self._config_grid()

        # adding the input area ( I hate this, It was difficult )
        self.prompt_input_area = PromptInputArea(self, function_mediator=self.function_mediator, model_mediator=self.model_mediator)
        self.prompt_input_area.configure(width=600, height=400, fg_color="transparent")
        self.prompt_input_area.grid(row=2, column=2, sticky="nsew")
        self.prompt_input_area.grid_propagate(False)
        self.prompt_input_area.update_idletasks()
        self.prompt_input_area.grid(row=2, column=2)

        # adding the buttons
        self._add_menu_btn()
        self._add_help_btn()
        self._add_custom_range_button()

        # If you need add more widgets, add them here
        # . . .

    def _open_custom_range_dialog(self):
        dialog = DialogoNumeros(self)

        temp_range = dialog.obtener_valores()

        if temp_range is not None:
            self.custom_range = temp_range

    def _add_custom_range_button(self):
        '''
        El boton abre un dialogo para que el usuario
        defina un rango personalizado para la grafica
        y lo guarda en self.custom_range
        '''

        img_path = os.path.join(os.path.dirname(__file__), "..", "sources", "img", "range_40p.png")
        img_path = os.path.abspath(img_path)
        icon_img = ctk.CTkImage(light_image=Image.open(img_path), size=(40, 40))

        self.custom_range_button = ctk.CTkButton(
            self,
            text="",
            width=50,
            height=50,
            fg_color="transparent",
            image=icon_img,
            command=self._open_custom_range_dialog,
        )
        self.custom_range_button.grid(row=0, column=6, padx=10, pady=10, sticky="ne")

    def _add_menu_btn(self):
        ''' Adds the menu button to the panel '''
        # adding an icon to the button
        img_path = os.path.join(os.path.dirname(__file__), "..", "sources", "img", "side_nav_40p.png")
        img_path = os.path.abspath(img_path)
        icon_img = ctk.CTkImage(light_image=Image.open(img_path), size=(40, 40))

        self.menu_btn = ctk.CTkButton(self, 
                                       text="",
                                       command=lambda: self._show_select_model_panel(),
                                       width=50,
                                       height=50,
                                       image=icon_img,
                                       fg_color="transparent",
                                       )
        self.menu_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    def _add_help_btn(self):
        ''' Adds the help button to the panel '''
        # adding an icon to the button
        img_path = os.path.join(os.path.dirname(__file__), "..", "sources", "img", "help_50p.png")
        img_path = os.path.abspath(img_path)
        icon_img = ctk.CTkImage(light_image=Image.open(img_path), size=(40, 40))

        self.help_btn = ctk.CTkButton(self, 
                                       text="",
                                       width=50,
                                       height=50,
                                       image=icon_img,
                                       fg_color="transparent",
                                       )
        self.help_btn.grid(row=4, column=6, padx=10, pady=10, sticky="se")
        self.help_btn.bind("<Double-1>", lambda event: self._on_help())

    ### events ###
    def _show_select_model_panel(self):
        self.model_selection_panel = ModelSelectionPanel(self, self.model_mediator)
        self.model_selection_panel.grab_set()
        center_window(self.model_selection_panel, 450, 300)
        self.master.wait_window(self.model_selection_panel)

    def _on_help(self):
        dialog = SecretDialog(self)
        center_window(dialog, 300, 200)
        dialog.grab_set()
        self.master.wait_window(dialog)

