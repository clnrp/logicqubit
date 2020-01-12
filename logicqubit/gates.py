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
    def P0():
        M = Matrix([[1, 0], [0, 0]])  # |0><0|
        return M

    @staticmethod
    def P1():
        M = Matrix([[0, 0], [0, 1]])  # |1><1|
        return M