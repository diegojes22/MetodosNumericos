from logic.biseccion.function import Function

def newton_raphson_method(func: Function, x0: float, tol: float = 1e-7, max_iter: int = 100) -> float:
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
        
        x_n = x_n1
    
    raise ValueError("Maximum iterations reached. No solution found.")