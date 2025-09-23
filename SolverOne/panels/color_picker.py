import customtkinter as ctk
from panels.basic import center_window

class ColorPickerDialog(ctk.CTkToplevel):
    def __init__(self, parent, initial_color="#ffffff"):
        super().__init__(parent)
        self.title("Seleccionar color")
        self.geometry("300x300")
        self.minsize(300, 300)
        self.transient(parent)
        self.grab_set()  # Modal

        self.result = None

        # Convertir color inicial a RGB
        self.r = ctk.IntVar(value=int(initial_color[1:3], 16))
        self.g = ctk.IntVar(value=int(initial_color[3:5], 16))
        self.b = ctk.IntVar(value=int(initial_color[5:7], 16))

        # Sliders
        ctk.CTkLabel(self, text="Rojo").pack()
        ctk.CTkSlider(self, from_=0, to=255, variable=self.r, command=self.update_color).pack(fill="x")
        ctk.CTkLabel(self, text="Verde").pack()
        ctk.CTkSlider(self, from_=0, to=255, variable=self.g, command=self.update_color).pack(fill="x")
        ctk.CTkLabel(self, text="Azul").pack()
        ctk.CTkSlider(self, from_=0, to=255, variable=self.b, command=self.update_color).pack(fill="x")

        # Preview
        self.preview = ctk.CTkLabel(self, text="", width=100, height=40, corner_radius=8)
        self.tag_color = ctk.CTkLabel(self, text="#")

        self.preview.pack(pady=10)
        self.tag_color.pack()
        self.update_color()

        # Buttons
        btn_frame = ctk.CTkFrame(self)
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="Aceptar", command=self.on_accept).pack(side="left", padx=5, fill="y")
        ctk.CTkButton(btn_frame, text="Cancelar", command=self.on_cancel).pack(side="left", padx=5, fill="y")

        self.protocol("WM_DELETE_WINDOW", self.on_cancel)

    def update_color(self, *args):
        color = f"#{self.r.get():02x}{self.g.get():02x}{self.b.get():02x}"
        self.preview.configure(fg_color=color)
        self.tag_color.configure(text=color)

    def on_accept(self):
        self.result = f"#{self.r.get():02x}{self.g.get():02x}{self.b.get():02x}"
        self.grab_release()
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.grab_release()
        self.destroy()

def ask_color(parent, initial_color="#ffffff"):
    dialog = ColorPickerDialog(parent, initial_color)
    center_window(dialog, 300, 300)
    parent.wait_window(dialog)
    return dialog.result
