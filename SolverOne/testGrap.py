import customtkinter as ctk
from logic.biseccion.function import FunctionMediator, FunctionObserver, Function
from panels import graph

if __name__ == "__main__":
    root = ctk.CTk()

    function = Function("math.sin(x) - ln(x)")
    func = FunctionMediator()
    func.set_function(function)

    graph_dialog = graph.GraphDialog(root, func)
    graph_dialog.show()
    graph_dialog.grab_set()

    root.wait_window(graph_dialog)
    