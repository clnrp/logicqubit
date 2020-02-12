#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp
from sympy.physics.quantum import TensorProduct
import cupy as cp

from logicqubit.utils import *

class Hilbert():

    def setSymbolic(self, symbolic):
        Hilbert.__symbolic = symbolic

    def setCuda(self, cuda):
        Hilbert.__cuda = cuda

    def getCuda(self):
        return Hilbert.__cuda

    def ket(self, value, d = 2):
        if (Hilbert.__cuda):
            result = cp.array([[Utils.onehot(i, value)] for i in range(d)])
        else:
            result = sp.Matrix([[Utils.onehot(i, value)] for i in range(d)])
        return result

    def bra(self, value, d = 2):
        if (Hilbert.__cuda):
            result = cp.array([Utils.onehot(i, value) for i in range(d)])
        else:
            result = sp.Matrix([Utils.onehot(i, value) for i in range(d)])
        return result

    def product(self, Operator, psi):
        if(Hilbert.__cuda):
            result = cp.dot(Operator, psi)
        else:
            result = Operator * psi
        return result

    def kronProduct(self, list): # produto de Kronecker
        A = list[0] # atua no qubit 1 que é o mais a esquerda
        if (Hilbert.__cuda):
            for M in list[1:]:
                A = cp.kron(A, M)
        else:
            for M in list[1:]:
                A = TensorProduct(A, M)
        return A