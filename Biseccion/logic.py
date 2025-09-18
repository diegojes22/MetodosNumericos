from math import *

class Function:
    ''' Clase para representar una función matemática '''
    def __init__(self, expresion: str):
        self.expresion = expresion
        self.real_roots : list[float] = []

    def set_expression(self, expresion: str):
        self.expresion = expresion

    def evaluate(self, x: float) -> float:
        ''' Evaluates the polynomial function at a given x value '''
        return eval(self.expresion.replace('x', f'({x})'))
    
    def get_coefficients(self) -> list[float]:
        ''' Returns the coefficients of the polynomial function'''
        terms = self.expresion.replace('-', '+-').split('+')
        coefficients : list[float] = []

        for term in terms:
            term = term.strip()
            if(term == ''):
                continue

            val = eval(term.replace('x', ('(1)')))
            if val != 0:
                coefficients.append(val)

        return coefficients
    
    def append_real_root(self, root: float):
        self.real_roots.append(root)

    def get_real_roots(self) -> list[float]:
        return self.real_roots
    
    def _filter_expression(self):
        pass
    
    def __str__(self):
        return self.expresion
    
######################################

def get_multiples(number) -> list[int]:
    ''' Returns the multiples of a number '''
    multiples : list[int] = []

    for n in range(1, number + 1):
        if(number % n == 0):
            multiples.append(n)

    return multiples

def get_rational_roots(p : float, q : float) -> list[float]:
    ''' Returns the possible rational roots of a polynomial using the Rational Root Theorem '''
    multiplesP = get_multiples(p)
    multiplesQ = get_multiples(q)

    roots : list[float] = []

    for i in range(len(multiplesP)):
        for j in range(len(multiplesQ)):
            roots.append(multiplesP[i] / multiplesQ[j])
            roots.append(-multiplesP[i] / multiplesQ[j])

    # order and remove duplicates
    roots = list(set(roots))
    roots.sort()

    return roots    

def count_real_solutions(function : Function) -> int:
    ''' Uses Descartes' Rule of Signs to count the number of possible real solutions of a polynomial function '''
    coefficients : list[float] = function.get_coefficients()
    changes : int = 0
    
    for i in range(len(coefficients)-1):
        if coefficients[i] * coefficients[i+1] < 0:
            changes += 1

    return changes

def get_intervals(function : Function) -> list[tuple[float, float]]:
    ''' Returns a list of intervals [a, b] where f(a) and f(b) have opposite signs '''
    intervals : list[tuple[float, float]] = []

    rational_nums : list[float] = get_rational_roots(
        abs(int(function.get_coefficients()[-1])), 
        abs(int(function.get_coefficients()[0]))
    )
    results : list[float] = []

    print(f"Rational candidates: {rational_nums}")
    for r in rational_nums:
        results.append((function.evaluate(r)))

        if(r == 0):
            function.append_real_root(rational_nums[i])

    i = 0
    while i < len(results)-1:
        if results[i] * results[i + 1] < 0:
            intervals.append((rational_nums[i], rational_nums[i + 1]))
        
        i += 1

    return intervals

def biseccion(function, a: float, b: float, limit: int) -> float:
    ''' Bisection method to find a root of the function in the interval [a, b] '''
    m : float = 0   # Mid point

    f_a : float = 0
    f_b : float = 0
    f_m : float = 0

    for i in range(limit):
        f_a = function(a)              # Calculate vars for this iteration
        f_b = function(b)

        m = (a + b) / 2
        f_m = function(m)

        if(f_m == 0):  # Exact root found
            break

        # refine new interval
        if f_a * f_m < 0:
            b = m
        else:
            a = m

    return m