import customtkinter as ctk

from panels.results import ResultsPanel
from logic.biseccion.function import Function, FunctionMediator, FunctionObserver
import logic.biseccion.logic as lo

root = ctk.CTk()
root.geometry("600x600")

function = Function("x**2 - 4.5")
function_mediator = FunctionMediator()
function_mediator.set_function(function)

r_panel = ResultsPanel(root, function_mediator)
r_panel.solver()
r_panel.show()


