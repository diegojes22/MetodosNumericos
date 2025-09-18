import customtkinter as ctk
import tkinter as tk
import logic as lg

from tkinter import messagebox

class Section(ctk.CTkFrame):
    ''' Objeto base para las secciones de la aplicación '''
    def __init__(self, root):
        super().__init__(root)
        self.root = root

    def set_section_title(self, title):
        ''' Establece el título de la sección o menu'''
        self.title = ctk.CTkLabel(self, text=title, font=ctk.CTkFont(size=20, weight="bold", family="Plus Jakarta Sans"))
        self.title.pack(pady=5)

    def create_widget(self, widget_type, **kwargs):
        ''' 
        Metodo para implementar widgets de una forma muy simple.
        @note: No se recomienda si se desea eliminar o modificar un widget luego de creado.
        '''
        if widget_type == "label":
            return ctk.CTkLabel(self, **kwargs)
        elif widget_type == "entry":
            return ctk.CTkEntry(self, **kwargs)
        elif widget_type == "button":
            return ctk.CTkButton(self, **kwargs)
        elif widget_type == "textbox":
            return ctk.CTkTextbox(self, **kwargs)
        elif widget_type == "combobox":
            return ctk.CTkComboBox(self, **kwargs)
        else:
            raise ValueError(f"Tipo de widget '{widget_type}' no soportado.")

class ProblemSection(Section):
    '''
    Seccion para definir el problema a resolver, ademas de que aqui se
    mostrara el analisis correspondiente.
    '''
    def __init__(self, root, function: lg.Function):
        '''Constructor'''
        super().__init__(root)
        self.function = function

        self.set_section_title("Definición del Problema")
        self.create_widgets()

    def create_widgets(self):
        ''' Crea los widgets de la sección '''
        # Usando el metodo de la super clase
        self.problem_label = self.create_widget("label", text="Ingrese la función:")
        self.problem_label.pack(pady=5, padx=5, fill='x', anchor='w')

        self.problem_entry = self.create_widget("entry")
        self.problem_entry.pack(padx=5, fill="x")

        self.add_button = self.create_widget("button", text="Agregar", command=self.add_problem)
        self.add_button.pack(padx=5, pady=2, fill="x")

        # Aquí puedes agregar más widgets específicos para esta sección

    ### Events
    def add_problem(self):
        ''' 
        Evento para agregar el problema 
        @note: Este metodo debe ser remplazado por uno mas avanzado
         '''
        problem = self.problem_entry.get()

        if problem:
            self.function.set_expression(problem)
            messagebox.showinfo("OK", f"Función '{problem}' agregada correctamente.")


class MethodSection(Section):
    '''
    Pendiente de construir
    '''
    def __init__(self, root):
        super().__init__(root)
        self.set_section_title("Selección del Método")
        # Aquí puedes agregar más widgets específicos para esta sección
