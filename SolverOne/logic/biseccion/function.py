from abc import ABC, abstractmethod

class Function:
    ''' Class representing a mathematical function '''
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


#### The Mediator Pattern Implementation ####
# These classes need a update because they are not compatible
# with the new Function class
class FunctionObserver(ABC):
    '''
    Interface for observers that need to be notified when the function changes.
    Another words, this is teh contract
    '''
    @abstractmethod
    def update(self, function: Function):
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
        self.observers.remove(observer)