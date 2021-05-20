#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from logicqubit.utils import *
from logicqubit.hilbert import *

class PauliDecomposition:

    def __init__(self, H):
        self.H = Matrix(H)  # Hermitian matrix

    def sigma(self):
        ID = Matrix([[1, 0], [0, 1]])
        X = Matrix([[0, 1], [1, 0]])
        Y = Matrix([[0, -1j], [1j, 0]])
        Z = Matrix([[1, 0], [0, -1]])
        return [ID, X, Y, Z]

    def get_a(self):
        a = [[0]*4 for i in range(4)]
        for i, sigma_i in enumerate(self.sigma()):
            for j, sigma_j in enumerate(self.sigma()):
                a[i][j] = 1/4*(sigma_i.kron(sigma_j) * self.H).trace().get().item()
        return a