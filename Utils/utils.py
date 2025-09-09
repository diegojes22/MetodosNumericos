def lines():
    print("-" * 50)

def confirm(prompt : str) -> bool:
    lines()
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            lines()
            return True
        elif response in ['n', 'no']:
            lines()
            return False
        else:
            print("Respuesta no valida. Por favor ingrese 'y' o 'n'.")

def function(expression : str, x : float) -> float:
    expression = expression.replace("x", f"{x}")
    return eval(expression)