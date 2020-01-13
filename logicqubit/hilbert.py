#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

from logicqubit.utils import *

class Hilbert():

    def ket(self, value, d = 2):
        return Matrix([[Utils.onehot(i, value)] for i in range(d)])

    def bra(self, value, d = 2):
        return Matrix([Utils.onehot(i, value) for i in range(d)])

    def product(self, list):
        A = list[0] # atua no qubit 1 que é o mais a esquerda
        for M in list[1:]:
            A = TensorProduct(A, M)
        return A