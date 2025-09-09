from Utils import utils
from Utils import csv

if(__name__ == "__main__"):
    print("Metodo de biseccion")

    # Variables
    path : str = "./out/biseccion.csv" # File out path
    file = csv.File(path)

    hidden : bool = False

    function : str = "x**3 + 4*x**2 - 10" # function f(x)
    def f(x) -> float:
        return utils.function(function, x)

    a : float = float(input("Ingrese el valor de a: "))  # Interval start
    b : float = float(input("Ingrese el valor de b: "))  # Interval end

    m : float = 0   # Mid point

    f_a : float = 0
    f_b : float = 0
    f_m : float = 0

    limit : int = int(input("Ingrese el numero de iteraciones: "))

    # Procedure
    utils.lines()

    print("\tIniciando procedimiento")
    print(f"\tFuncion: f(x) = {function}")
    print(f"\tIntervalo inicial: [{a}, {b}]")

    file.clear()
    file.append([f"Funcion: f(x) = {function}\n"])
    file.append([f"Intervalo inicial: [{a}, {b}]\n\n"])
    file.append(["Iteracion, a, b, m, f(a), f(b), f(m)\n"])

    utils.lines()

    # Check if the user wants to hide the output
    hidden = utils.confirm("¿Desea ocultar la salida de las iteraciones?")

    for i in range(limit):
        f_a = f(a)              # Calculate vars for this iteration
        f_b = f(b)

        m = (a + b) / 2
        f_m = f(m)

        if(not hidden):
            print(f"Iteración {i}: a = {a}, b = {b}, m = {m}, f(a) = {f_a}, f(b) = {f_b}, f(m) = {f_m}")
        file.append([f"Iteracion {i}, {a}, {b}, {m}, {f_a}, {f_b}, {f_m}\n"])

        if(f_m == 0):  # Exact root found
            break

        # refine new interval
        if f_a * f_m < 0:
            b = m
        else:
            a = m

    utils.lines()

    print(f"\tLa raiz aproximada es: {m}")
    file.append([f"\nRaiz aproximada: {m},,,,,,\n"])

    print("\tProcedimiento finalizado\n")
    print("Nota: Puede consultar los resultados en el archivo ./out/biseccion.csv")
    utils.lines()
