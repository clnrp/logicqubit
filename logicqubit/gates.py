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

    @staticmethod
    def X():
        M = Matrix([[0, 1], [1, 0]])
        return M

    @staticmethod
    def Y():
        M = Matrix([[0,-I], [I,0]])
        return M

    @staticmethod
    def Z():
        M = Matrix([[1,0], [0,-1]])
        return M

    @staticmethod
    def S(): # sqrt(Z)
        M = Matrix([[1, 0], [0, I]])
        return M

    @staticmethod
    def T(): # sqrt(S)
        M = Matrix([[1, 0], [0, (1+I)/sqrt(2)]])
        return M

    @staticmethod
    def H():
        M = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
        return M

    @staticmethod
    def CNOT():
        M = Matrix([[0, 1], [1, 0]])
        return M

    @staticmethod
    def U1(_lambda):
        M = Matrix([[1, 0], [0, exp(I*_lambda)]])
        return M

    @staticmethod
    def U2(phi, _lambda):
        M = Matrix([[1, -exp(I*_lambda)], [exp(I*phi), exp(I*(phi+_lambda))]])
        return M

    @staticmethod
    def U3(theta, phi, _lambda):
        M = Matrix([[cos(theta/2), -exp(I*_lambda)*sin(theta/2)],
                    [exp(I*phi)*sin(theta/2), exp(I*(phi+_lambda))*cos(theta/2)]])
        return M

    @staticmethod
    def RX(theta):
        M = Matrix([[cos(theta/2), -I*sin(theta/2)],
                    [-I*sin(theta/2), cos(theta/2)]])
        return M

    @staticmethod
    def RY(theta):
        M = Matrix([[cos(theta/2), -sin(theta/2)],
                    [sin(theta/2), cos(theta/2)]])
        return M

    @staticmethod
    def RZ(phi):
        M = Matrix([[exp(-I*phi/2), 0], [0, exp(I*phi/2)]])
        return M

    @staticmethod
    def SWAP():
        M = Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                    [0, 1, 0, 0], [0, 0, 0, 1]])
        return M

    @staticmethod
    def CCNOT(): # Toffoli Gate
        M = Matrix([[1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1],
                    [0, 0, 0, 0, 0, 0, 1, 0]])
        return M

    @staticmethod
    def P0():
        M = Matrix([[1, 0], [0, 0]])  # |0><0|
        return M

    @staticmethod
    def P1():
        M = Matrix([[0, 0], [0, 1]])  # |1><1|
        return M