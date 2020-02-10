#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
import numpy as np
import cupy as cp

from logicqubit.utils import *

class Hilbert():

    def setSymbolic(self, symbolic):
        Hilbert.__symbolic = symbolic

    def setCuda(self, cuda):
        Hilbert.__cuda = cuda

    def ket(self, value, d = 2):
        return Matrix([[Utils.onehot(i, value)] for i in range(d)])

    def bra(self, value, d = 2):
        return Matrix([Utils.onehot(i, value) for i in range(d)])

    def product(self, list):
        A = list[0] # atua no qubit 1 que é o mais a esquerda
        for M in list[1:]:
            A = TensorProduct(A, M)
        return A

    def kronProduct(self, list): # produto de Kronecker
        A = list[0] # atua no qubit 1 que é o mais a esquerda
        for M in list[1:]:
            A = TensorProduct(A, M)
        return A