from abc import ABC, abstractmethod

import math
import re

class Function:
    '''
    Class to represent a mathematical function
    '''
    def __init__(self, expresion: str):
        ''' Constructor'''
        self.original_expression = expresion  # Original user expression
        self.expresion = self._transform_expression(expresion)
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
        ''' Appends a real root to the list of real roots '''
        self.real_roots.append(root)

    def get_real_roots(self) -> list[float]:
        ''' Returns the list of real roots '''
        return self.real_roots
    
    def _transform_expression(self, expression: str) -> str:
        """
        Transforms mathematical notation to Python-compatible notation
        Examples:
        - x^2 -> x**2
        - ln(x) -> math.log(x)  # Natural logarithm
        - log(x) -> math.log10(x)  # Base 10 logarithm (when no base specified)
        - log(x, b) -> math.log(x, b)  # Logarithm with base b
        - sen(x) -> math.sin(x)
        - cos(x) -> math.cos(x)
        - tan(x) -> math.tan(x)
        - sqrt(x) -> math.sqrt(x)
        - e^x -> math.exp(x)
        """
        # Remove spaces for easier processing
        expr = expression.replace(' ', '')
        
        # Replace power notation x^n with x**n
        expr = re.sub(r'(\w+|\([^)]+\))\^(\w+|\([^)]+\))', r'\1**\2', expr)
        
        # Handle logarithms more carefully
        # First handle log with explicit base: log(x, base) -> math.log(x, base)
        expr = re.sub(r'log\(([^,)]+),([^)]+)\)', r'math.log(\1,\2)', expr)
        
        # Then handle ln (natural log): ln(x) -> math.log(x)
        expr = re.sub(r'ln\(', 'math.log(', expr)
        
        # Finally handle log without base (assume base 10): log(x) -> math.log10(x)
        # This regex ensures we don't match already transformed math.log
        expr = re.sub(r'(?<!math\.)log\(', 'math.log10(', expr)
        
        # Replace mathematical functions
        transformations = [
            # Trigonometric functions (Spanish notation)
            (r'sen\(', 'math.sin('),
            (r'cos\(', 'math.cos('),
            (r'tan\(', 'math.tan('),
            (r'sec\(', '(1/math.cos('),
            (r'csc\(', '(1/math.sin('),
            (r'cot\(', '(1/math.tan('),
            
            # Inverse trigonometric functions
            (r'arcsen\(', 'math.asin('),
            (r'arccos\(', 'math.acos('),
            (r'arctan\(', 'math.atan('),
            (r'asen\(', 'math.asin('),
            (r'acos\(', 'math.acos('),
            (r'atan\(', 'math.atan('),
            
            # Exponential functions
            (r'exp\(', 'math.exp('),
            (r'sqrt\(', 'math.sqrt('),
            
            # Mathematical constants
            (r'\be\b', 'math.e'),
            (r'\bpi\b', 'math.pi'),
        ]
        
        # Apply all transformations
        for pattern, replacement in transformations:
            expr = re.sub(pattern, replacement, expr)
        
        # Handle e^x notation specially
        expr = re.sub(r'math\.e\*\*(\w+|\([^)]+\))', r'math.exp(\1)', expr)
        
        # Fix closing parentheses for sec, csc, cot
        expr = re.sub(r'\(1/math\.(cos|sin|tan)\(([^)]+)\)\)', r'(1/math.\1(\2))', expr)
        
        return expr
    
    def get_original_expression(self) -> str:
        """Returns the original expression as entered by the user"""
        return self.original_expression
    
    def get_transformed_expression(self) -> str:
        """Returns the Python-compatible transformed expression"""
        return self.expresion
    
    def __str__(self):
        return self.expresion


#### The Mediator Pattern Implementation ####
# These classes need a update because they are not compatible
# with the new Function class
class FunctionObserver(ABC):
    '''
    Interface for observers that need to be notified when the function changes.
    Another words, this is teh contract
    '''
    @abstractmethod
    def update(function: Function):
        pass

class FunctionMediator:
    '''
    Mediator class for managing the communication between the function and its observers.
    '''
    def __init__(self):
        self.observers = []
        self.function = None

    def set_function(self, function: Function):
        self.function = function
        self.notify_observers()

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.function)

    def register(self, observer: FunctionObserver):
        '''
        If your class needs to be notified when the function changes, register it here.
        '''
        self.observers.append(observer)

    def remove_observer(self, observer: FunctionObserver):
        ''' Removes an observer from the list, is the opposite of register '''
        try:
            self.observers.remove(observer)
        except ValueError:
            pass
        