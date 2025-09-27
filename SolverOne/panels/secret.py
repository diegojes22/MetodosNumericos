import customtkinter as ctk
import os

from panels.basic import add_image_to_button

class SecretDialog(ctk.CTkToplevel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self._config()
        self._add_widgets()
        
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def _config(self):
        self.title("Secret Panel")
        self.geometry("300x200")
        self.minsize(200, 200)
        
        self.grab_set()  # Modal

    def _add_widgets(self):
        self.label = ctk.CTkLabel(self, text="This is a secret panel!")
        self.label.pack(pady=20)
        add_image_to_button(self.label, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "nico.jpg")
        ), (200,200))

    def on_close(self):
        self.grab_release()
        self.destroy()