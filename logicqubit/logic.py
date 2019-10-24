#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

class LogicQuBit:

    def __init__(self, num = 3):
        self.num = num
        self.phi = self.product([self.ket(0) for i in range(num)])

    def onehot(self, i, value):
        if(i == value):
            return 1
        else:
            return 0

    def ket(self, value, d = 2):
        return Matrix([[self.onehot(i, value)] for i in range(d)])

    def product(self, list):
        A = list[0]
        for M in list[1:]:
            A = TensorProduct(A, M)
        return A

    def getOrdListSimpleGate(self, p, Gate):
        list = []
        for i in range(1,self.num+1):
            if i == p:
                list.append(Gate)
            else:
                list.append(eye(2))
        return list

    def getOrdListCtrlGate(self, p1, p2, Gate):
        kb0 = Matrix([[1, 0], [0, 0]]) # |0><0|
        kb1 = Matrix([[0, 0], [0, 1]]) # |1><1|
        list1 = []
        list2 = []
        for i in range(1,self.num+1):
            if i == p1:
                list1.append(kb0)
                list2.append(kb1)
            elif i == p2:
                list1.append(eye(2))
                list2.append(Gate)
            else:
                list1.append(eye(2))
                list2.append(eye(2))
        return list1, list2

    def X(self, p):
        X = Matrix([[0, 1], [1, 0]])
        list = self.getOrdListSimpleGate(p, X)
        self.phi = self.product(list)*self.phi

    def Y(self, p):
        Y = Matrix([[0, -I], [I, 0]])
        list = self.getOrdListSimpleGate(p, Y)
        self.phi = self.product(list)*self.phi

    def Z(self, p):
        Z = Matrix([[1, 0], [0, -1]])
        list = self.getOrdListSimpleGate(p, Z)
        self.phi = self.product(list)*self.phi

    def H(self, p):
        M = 1 / sqrt(2) * Matrix([[1, 1], [1, -1]])
        list = self.getOrdListSimpleGate(p, M)
        self.phi = self.product(list)*self.phi

    def CNOT(self, p1, p2):
        X = Matrix([[0, 1], [1, 0]])
        list1,list2 = self.getOrdListCtrlGate(p1, p2, X)
        product = self.product(list1) + self.product(list2)
        self.phi = product*self.phi
        return self.phi

    def DensityMatrix(self):
        density_m = self.phi*self.phi.adjoint() # |phi><phi|
        return density_m

    def Measure(self, p):
        kb0 = Matrix([[1, 0], [0, 0]]) # |0><0|
        kb1 = Matrix([[0, 0], [0, 1]]) # |1><1|
        density_m = self.DensityMatrix()
        list = self.getOrdListSimpleGate(p, kb0)
        P0 = self.product(list)
        list = self.getOrdListSimpleGate(p, kb1)
        P1 = self.product(list)
        measure_0 = (density_m*P0).trace()
        measure_1 = (density_m*P1).trace()
        return measure_0, measure_1

    def Pure(self):
        density_m = self.DensityMatrix()
        pure = (density_m*density_m).trace()
        return pure

    def _print(self):
        #"{0:b}".format(5).zfill(3)
        print(self.phi)