import customtkinter as ctk
from tkinter import messagebox

class DialogoNumeros(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        # Configuración de la ventana
        self.title("Ingresar Números")
        self.geometry("300x350")
        self.resizable(False, False)
        
        # Hacer la ventana modal
        self.transient(parent)
        self.grab_set()
        
        # Variables para almacenar los valores
        self.numero1 = None
        self.numero2 = None
        self.resultado = None
        
        # Centrar la ventana respecto a la ventana padre
        self.center_window()
        
        # Crear widgets
        self.crear_widgets()
        
        # Esperar a que la ventana se cierre
        self.wait_window(self)
    
    def center_window(self):
        """Centra la ventana respecto a la ventana padre"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (width // 2)
        y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - (height // 2)
        self.geometry(f"+{x}+{y}")
    
    def crear_widgets(self):
        """Crea los widgets de la interfaz"""
        # Frame principal
        frame = ctk.CTkFrame(self)
        frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        # Título
        titulo = ctk.CTkLabel(frame, text="Ingrese dos números", 
                             font=ctk.CTkFont(size=16, weight="bold"))
        titulo.pack(pady=(10, 20))
        
        # Entrada para el primer número
        lbl_numero1 = ctk.CTkLabel(frame, text="Primer número:")
        lbl_numero1.pack(anchor="w", padx=10)
        
        self.entry_numero1 = ctk.CTkEntry(frame, placeholder_text="Ingrese el primer número")
        self.entry_numero1.pack(fill="x", padx=10, pady=(0, 10))
        
        # Entrada para el segundo número
        lbl_numero2 = ctk.CTkLabel(frame, text="Segundo número:")
        lbl_numero2.pack(anchor="w", padx=10)
        
        self.entry_numero2 = ctk.CTkEntry(frame, placeholder_text="Ingrese el segundo número")
        self.entry_numero2.pack(fill="x", padx=10, pady=(0, 20))
        
        # Frame para los botones
        frame_botones = ctk.CTkFrame(frame, fg_color="transparent")
        frame_botones.pack(fill="x", padx=10, pady=10)
        
        # Botón Aceptar
        btn_aceptar = ctk.CTkButton(frame_botones, text="Aceptar", 
                                   command=self.aceptar)
        btn_aceptar.pack(side="right", padx=(10, 0))
        
        # Botón Cancelar
        btn_cancelar = ctk.CTkButton(frame_botones, text="Cancelar", 
                                    command=self.cancelar, 
                                    fg_color="transparent", 
                                    border_width=1)
        btn_cancelar.pack(side="right")
        
        # Bind Enter key para aceptar
        self.bind('<Return>', lambda e: self.aceptar())
        self.bind('<Escape>', lambda e: self.cancelar())
        
        # Focus en el primer campo
        self.after(100, self.entry_numero1.focus)
    
    def validar_numeros(self):
        """Valida que los campos contengan números válidos"""
        try:
            num1 = float(self.entry_numero1.get())
            num2 = float(self.entry_numero2.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
            return None, None
    
    def aceptar(self):
        """Maneja el evento del botón Aceptar"""
        num1, num2 = self.validar_numeros()
        
        if num1 is not None and num2 is not None:
            self.numero1 = num1
            self.numero2 = num2
            self.resultado = (num1, num2)
            self.destroy()
    
    def cancelar(self):
        """Maneja el evento del botón Cancelar"""
        self.resultado = None
        self.destroy()
    
    def obtener_valores(self):
        """Retorna los valores ingresados por el usuario"""
        return self.resultado


# Ejemplo de uso
class AplicacionPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Aplicación Principal")
        self.geometry("400x300")
        
        # Crear widgets de la aplicación principal
        self.crear_widgets()
    
    def crear_widgets(self):
        """Crea los widgets de la aplicación principal"""
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        titulo = ctk.CTkLabel(frame, text="Aplicación Principal", 
                             font=ctk.CTkFont(size=18, weight="bold"))
        titulo.pack(pady=20)
        
        self.btn_abrir_dialogo = ctk.CTkButton(frame, text="Abrir Diálogo de Números", 
                                              command=self.abrir_dialogo)
        self.btn_abrir_dialogo.pack(pady=10)
        
        self.lbl_resultado = ctk.CTkLabel(frame, text="Resultado: Esperando entrada...", 
                                         font=ctk.CTkFont(size=14))
        self.lbl_resultado.pack(pady=20)
    
    def abrir_dialogo(self):
        """Abre el diálogo modal y obtiene los resultados"""
        dialogo = DialogoNumeros(self)
        resultado = dialogo.obtener_valores()
        
        if resultado:
            num1, num2 = resultado
            self.lbl_resultado.configure(
                text=f"Resultado: Número 1 = {num1}, Número 2 = {num2}"
            )
            # Aquí puedes usar los números como necesites
            print(f"Números ingresados: {num1}, {num2}")
        else:
            self.lbl_resultado.configure(text="Resultado: Operación cancelada")
            print("El usuario canceló la operación")
