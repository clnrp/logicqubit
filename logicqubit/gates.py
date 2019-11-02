#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

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

    def H(self, p):
        M = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
        return M

    def CNOT(self, p1, p2):
        M = Matrix([[0, 1], [1, 0]])
        return M

    def KetBra0(self):
        M = Matrix([[1, 0], [0, 0]])  # |0><0|
        return M

    def KetBra1(self):
        M = Matrix([[1, 0], [0, 0]])  # |1><1|
        return M