'''
The script that runs the application
but the interface is not complete yet
'''

import customtkinter as ctk
from panels import prompt

from logic.biseccion.function import FunctionMediator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# change this function pls
def centrar_ventana(ventana, ancho, alto):
    ventana.update_idletasks()
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

if(__name__ == "__main__"):
    # pending move this in a specific file class
    mediator = FunctionMediator()
    mediator.set_function(prompt.Function("x"))
    
    app = ctk.CTk()
    app.minsize(600, 400)
    app.title("CustomTkinter Button Example")

    centrar_ventana(app, 800, 600)

    prompt_panel = prompt.PromptPanel(app, mediator)
    prompt_panel.pack(fill="both", expand=True)

    app.mainloop()
