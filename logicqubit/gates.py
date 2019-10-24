from sympy import *

class Gates:
    def X(self):
        M = Matrix([[0, 1], [1, 0]])
        return M

    def Y(self):
        M = Matrix([[0,-I], [I,0]])
        return M

    def Z(self):
        M = Matrix([[1,0], [0,-1]])
        return M