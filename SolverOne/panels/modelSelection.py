import os
import customtkinter as ctk
from abc import ABC, abstractmethod

from panels.const import BOLD, SUBTITLE_SIZE, TITLE_SIZE
from panels.basic import add_image_to_button

### Name for methods ###
#
BISECCION = "Biseccion"

# 
NEWTON_RAPHSON = "Newton-Raphson"

# This method resolve a function using
# python libraries but the process is not
# explained to the user
PY_TOOL = "Py Tool"

class Model():
    def __init__(self, model : str = BISECCION):
        self.model = model

    def get_model(self) -> str:
        return self.model
    
    def set_model(self, model: str):
        self.model = model

    def __str__(self) -> str:
        return self.model
    
class ModelMediator:
    def __init__(self):
        self.model = Model()
        self.observers = []

    def set_model(self, model: str):
        self.model.set_model(model)
        self.notify_model_observers()

    def get_model(self) -> str:
        return self.model.get_model()

    def notify_model_observers(self):
        for observer in self.observers:
            observer.update(self.model)

    def register(self, observer):
        self.observers.append(observer)

    def remove_model_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

class ModelObserver(ABC):
    @abstractmethod
    def update(model: Model):
        pass

    @abstractmethod
    def unregister(self, model: Model):
        pass

    @abstractmethod
    def register(self, model: Model):
        pass

### 
class ModelSelectionPanel(ctk.CTkToplevel):
    def __init__(self, master, model_mediator: ModelMediator):
        ''' Constructor '''
        super().__init__(master)
        self.model_mediator : ModelMediator = model_mediator
        self._add_widgets()

    def update(self, model: Model):
        pass

    def unregister(self, model: Model):
        self.bind("<Destroy>", lambda e: self.model_mediator.remove_model_observer(self))

    def register(self, model: Model):
        self.model_mediator.register(self)

    def get_model(self) -> str:
        return self.model_mediator.get_model()

    def _set_model(self, name: str):
        self.model_mediator.set_model(name)
        self.model_mediator.notify_model_observers()
        self.destroy()
    
    def _add_widgets(self):
        self.title_label = ctk.CTkLabel(self, text="Modelos", font=ctk.CTkFont(size=TITLE_SIZE, weight=BOLD))
        self.title_label.pack(pady=10, padx=10)

        self._add_buttons()

    def _add_buttons(self):
        model_name = self.model_mediator.get_model()

        self.bisection_btn = ctk.CTkButton(
            self, text=BISECCION, 
            command=lambda: self._set_model(BISECCION), 
            font=ctk.CTkFont(size=SUBTITLE_SIZE),
            fg_color="transparent" if model_name != BISECCION else "#0b1253",
            hover_color="#0b2f53",
            corner_radius=20
        )
        self.bisection_btn.pack(pady=5, padx=10, fill="x")
        

        self.newton_raphson_btn = ctk.CTkButton(
            self, text=NEWTON_RAPHSON, 
            command=lambda: self._set_model(NEWTON_RAPHSON), 
            font=ctk.CTkFont(size=SUBTITLE_SIZE),
            fg_color="transparent" if model_name != NEWTON_RAPHSON else "#0b1253",
            hover_color="#0b2f53",
            corner_radius=20
        )
        self.newton_raphson_btn.pack(pady=5, padx=10, fill="x")

        self.py_tool_btn = ctk.CTkButton(
            self, text=PY_TOOL, 
            command=lambda: self._set_model(PY_TOOL), 
            font=ctk.CTkFont(size=SUBTITLE_SIZE),
            fg_color="transparent" if model_name != PY_TOOL else "#0b1253",
            hover_color="#534d0b",
            corner_radius=20
        )
        add_image_to_button(self.py_tool_btn, os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "sources", "img", "premium.png")
        ), (20,20))
        self.py_tool_btn.pack(pady=5, padx=10, fill="x")
