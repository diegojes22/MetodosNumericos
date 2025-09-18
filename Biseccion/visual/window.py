import customtkinter as ctk

# Temas ctk
DARK_MODE = "dark"
LIGHT_MODE = "light"
SYSTEM_MODE = "system"
# Colores ctk
BLUE_COLOR = "blue"
GREEN_COLOR = "green"

class Window(ctk.CTk):
    '''Clase que representa la ventana principal de la aplicación'''
    def __init__(self, width=800, height=600):
        '''Constructor de la clase Window'''
        super().__init__()
        self.title("Método de la Bisección")
        self.geometry(f"{width}x{height}")

    def set_theme(self, theme=SYSTEM_MODE, color=BLUE_COLOR):
        '''Establece el tema de la aplicación'''
        ctk.set_appearance_mode(theme)
        ctk.set_default_color_theme(color)

    def goto_center(self):
        '''Centra la ventana en la pantalla'''
        self.update_idletasks()

        x = (self.winfo_screenwidth() // 2) - (self.winfo_width() // 2)
        y = (self.winfo_screenheight() // 2) - (self.winfo_height() // 2)

        self.geometry(f"{self.winfo_width()}x{self.winfo_height()}+{x}+{y}")