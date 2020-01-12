#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger
from cmath import *

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

    def S(self): # sqrt(Z)
        M = Matrix([[1, 0], [0, I]])
        return M

    def T(self): # sqrt(S)
        M = Matrix([[1, 0], [0, (1+I)/sqrt(2)]])
        return M

    def H(self):
        M = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
        return M

    def CNOT(self):
        M = Matrix([[0, 1], [1, 0]])
        return M

    def U1(self, _lambda):
        M = Matrix([[1, 0], [0, exp(I*_lambda)]])
        return M

    def U2(self, phi, _lambda):
        M = Matrix([[1, -exp(I*_lambda)], [exp(I*phi), exp(I*(phi+_lambda))]])
        return M

    def U3(self, theta, phi, _lambda):
        M = Matrix([[cos(theta/2), -exp(I*_lambda)*sin(theta/2)],
                    [exp(I*phi)*sin(theta/2), exp(I*(phi+_lambda))*cos(theta/2)]])
        return M

    def RX(self, theta):
        M = Matrix([[cos(theta/2), -I*sin(theta/2)],
                    [-I*sin(theta/2), cos(theta/2)]])
        return M

    def RY(self, theta):
        M = Matrix([[cos(theta/2), -sin(theta/2)],
                    [sin(theta/2), cos(theta/2)]])
        return M

    def RZ(self, phi):
        M = Matrix([[exp(-I*phi/2), 0], [0, exp(I*phi/2)]])
        return M

    def SWAP(self):
        M = Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                    [0, 1, 0, 0], [0, 0, 0, 1]])
        return M

    def CCNOT(self): # Toffoli Gate
        M = Matrix([[1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 1, 0]])
        return M

    def P0(self):
        M = Matrix([[1, 0], [0, 0]])  # |0><0|
        return M

    def P1(self):
        M = Matrix([[0, 0], [0, 1]])  # |1><1|
        return M