from logic.biseccion.function import Function

class ProcessReference:
    def __init__(self):
        self.process : str = ""

    def append(self, text: str):
        self.process += text

    def get(self) -> str:
        return self.process
    
    def set(self, text: str):
        self.process = text

    def clear(self):
        self.process = ""

    def __str__(self):
        return self.process

def newton_raphson_method(func: Function, x0: float, tol: float = 1e-7, max_iter: int = 100, procedure : ProcessReference | None= None) -> float:
    """
    Implements the Newton-Raphson method for finding roots of a function.
    
    Parameters:
    func (Function): The function object containing the expression and its evaluation method.
    x0 (float): Initial guess for the root.
    tol (float): Tolerance for stopping criterion.
    max_iter (int): Maximum number of iterations.
    
    Returns:
    float: Approximation of the root.
    
    Raises:
    ValueError: If the derivative is zero during the iteration.
    """
    x_n = x0
    for n in range(max_iter):
        f_xn = func.evaluate(x_n)
        f_prime_xn = func.diferentiate_eval(x_n)
        
        if f_prime_xn == 0:
            raise ValueError("Derivative is zero. No solution found.")
        
        x_n1 = x_n - f_xn / f_prime_xn
        
        if abs(x_n1 - x_n) < tol:
            return x_n1
        
        if procedure is not None:
            procedure.append(f"Iter {n+1}: x_n = {x_n}, f(x_n) = {f_xn}, f'(x_n) = {f_prime_xn}, x_n1 = {x_n1}\n")
        
        x_n = x_n1
    
    raise ValueError("Maximum iterations reached. No solution found.")

