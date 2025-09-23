import customtkinter as ctk

from PIL import Image, ImageTk

def add_image_to_button(button: ctk.CTkButton, image_path: str, size: tuple[int, int] = (24, 24)):
    image = Image.open(image_path)

    photo_image = ctk.CTkImage(light_image=image, dark_image=image, size=size)

    button.configure(image=photo_image)

def center_window(window, width, height):
    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")