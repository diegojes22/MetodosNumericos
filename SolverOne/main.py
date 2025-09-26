'''
The script that runs the application
'''
import customtkinter as ctk
from panels import prompt

from logic.biseccion.function import FunctionMediator
from panels import basic

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

if(__name__ == "__main__"):
    # pending move this in a specific file class
    mediator = FunctionMediator()
    mediator.set_function(prompt.Function("x**2"))
    
    app = ctk.CTk()
    app.minsize(600, 400)
    app.title("CustomTkinter Button Example")

    basic.center_window(app, 800, 600)

    prompt_panel = prompt.PromptPanel(app, mediator)
    prompt_panel.pack(fill="both", expand=True)

    app.mainloop()
