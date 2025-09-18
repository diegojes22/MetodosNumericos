import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Menú moderno")
app.geometry("500x300")

# Frame lateral
menu_frame = ctk.CTkFrame(app, width=120, corner_radius=0)
menu_frame.pack(side="left", fill="y")

# Botones estilo menú
btn1 = ctk.CTkButton(menu_frame, text="Inicio")
btn1.pack(pady=10, padx=10)

btn2 = ctk.CTkButton(menu_frame, text="Configuración")
btn2.pack(pady=10, padx=10)

btn3 = ctk.CTkButton(menu_frame, text="Salir", command=app.destroy)
btn3.pack(pady=10, padx=10)

# Contenido principal
label = ctk.CTkLabel(app, text="Contenido principal aquí")
label.pack(pady=50)

app.mainloop()
