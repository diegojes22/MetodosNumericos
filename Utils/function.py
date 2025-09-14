import math

class Function:
    def __init__(self, expresion: str):
        self.expresion = expresion
        self.real_roots : list[float] = []

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
    
    def __str__(self):
        return self.expresion
    


        