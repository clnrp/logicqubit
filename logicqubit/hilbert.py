#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp
import numpy as np
from sympy.physics.quantum import TensorProduct

cupy_is_available = True
try:
    import cupy as cp
except Exception as ex:
    cupy_is_available = False
    print("Cuda is not available!")

from logicqubit.utils import *


class Hilbert():
    __number_of_qubits = 1
    __cuda = True
    __first_left = True

    @staticmethod
    def ket(value):
        result = Matrix([[Utils.onehot(i, value)] for i in range(2)], Hilbert.__cuda)
        return result

    @staticmethod
    def bra(value):
        result = Matrix([Utils.onehot(i, value) for i in range(2)], Hilbert.__cuda)
        return result

    @staticmethod
    def getState():
        if Hilbert.getCuda():
            state = Hilbert.kronProduct([Hilbert.ket(0) for i in range(Hilbert.getNumberOfQubits())])
        else:
            if Hilbert.isFirstLeft():
                a = sp.symbols([str(i) + "a" + str(i) + "_0" for i in range(1, Hilbert.getNumberOfQubits() + 1)])
                b = sp.symbols([str(i) + "b" + str(i) + "_1" for i in range(1, Hilbert.getNumberOfQubits() + 1)])
            else:
                a = sp.symbols([str(Hilbert.getNumberOfQubits() + 1 - i) + "a" + str(i) + "_0" for i in
                                reversed(range(1, Hilbert.getNumberOfQubits() + 1))])
                b = sp.symbols([str(Hilbert.getNumberOfQubits() + 1 - i) + "b" + str(i) + "_1" for i in
                                reversed(range(1, Hilbert.getNumberOfQubits() + 1))])
            state = Hilbert.kronProduct([Hilbert.ket(0) * a[i] + Hilbert.ket(1) * b[i] for i in range(Hilbert.getNumberOfQubits())])
        return state

    @staticmethod
    def getAdjoint(psi):
        result = psi.adjoint()
        return result

    @staticmethod
    def product(Operator, psi):
        result = Operator * psi
        return result

    @staticmethod
    def kronProduct(list):  # produto de Kronecker
        A = list[0]  # atua no qubit 1 que é o mais a esquerda
        for M in list[1:]:
            A = A.kron(M)
        return A

    @staticmethod
    def setNumberOfQubits(number):
        Hilbert.__number_of_qubits = number

    @staticmethod
    def getNumberOfQubits():
        return Hilbert.__number_of_qubits

    @staticmethod
    def setCuda(cuda):
        Hilbert.__cuda = cuda

    @staticmethod
    def getCuda():
        return Hilbert.__cuda

    @staticmethod
    def setFirstLeft(value):
        Hilbert.__first_left = value

    @staticmethod
    def isFirstLeft():
        return Hilbert.__first_left


class Matrix:

    def __init__(self, matrix, cuda=True):
        self.__matrix = matrix
        self.__cuda = cuda
        if isinstance(matrix, list):
            if self.__cuda:
                if cupy_is_available:
                    self.__matrix = cp.array(matrix)
                else:
                    self.__matrix = np.array(matrix)
            else:
                self.__matrix = sp.Matrix(matrix)
        else:
            if isinstance(matrix, Matrix):
                self.__matrix = matrix.get()
            else:
                self.__matrix = matrix

    def __add__(self, other):
        result = self.__matrix + other.get()
        return Matrix(result, self.__cuda)

    def __sub__(self, other):
        result = self.__matrix - other.get()
        return Matrix(result, self.__cuda)

    def __mul__(self, other):
        if isinstance(other, Matrix):
            other = other.get()
            if self.__cuda:
                if cupy_is_available:
                    result = cp.dot(self.__matrix, other)
                else:
                    result = np.dot(self.__matrix, other)
            else:
                result = self.__matrix * other
        else:
            result = self.__matrix * other
        return Matrix(result, self.__cuda)

    def __truediv__(self, other):
        result = self.__matrix * (1./other)
        return Matrix(result, self.__cuda)

    def __eq__(self, other):
        return self.__matrix == other.get()

    def __str__(self):
        return str(self.__matrix)

    def kron(self, other):  # Kronecker product
        if self.__cuda:
            if cupy_is_available:
                result = cp.kron(self.__matrix, other.get())
            else:
                result = np.kron(self.__matrix, other.get())
        else:
            result = TensorProduct(self.__matrix, other.get())
        return Matrix(result, self.__cuda)

    def get(self):
        return self.__matrix

    def getAngles(self):
        angles = []
        if self.__cuda:
            if cupy_is_available:
                angles = cp.angle(self.__matrix)
            else:
                angles = np.angle(self.__matrix)
        else:
            print("This session is symbolic!")
        return angles

    def trace(self):
        result = self.__matrix.trace()
        return Matrix(result, self.__cuda)

    def adjoint(self):
        if self.__cuda:
            result = self.__matrix.transpose().conj()
        else:
            result = self.__matrix.transpose().conjugate()
        return Matrix(result, self.__cuda)
