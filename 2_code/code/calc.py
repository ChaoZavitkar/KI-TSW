from code.operations import *

class Calculator:
    def __init__(self):
        self._ans = 0

    @property
    def ans(self) -> int:
        return self._ans
    
    def _operate(self, a, b, operator):
        self._ans = operator(a, b)
        return self._ans
    
    def plus(self, a, b):
        return self._operate(a, b, operator=add)
    
    def minus(self, a, b):
        return self._operate(a, b, operator=sub)
    
    def asterisk(self, a, b):
        return self._operate(a, b, operator=mul)
    
    def slash(self, a, b):
        return self._operate(a, b, operator=div)
    
    # test-driven development
    def delete(self):
        self._ans = 0

    def  modulo(self, a, b):
        return self._operate(a, b, operator=mod)
    
    def pythagoras(self, a , b, c):
        return self._operate((a**2 + b**2), c**2, operator=pyt)