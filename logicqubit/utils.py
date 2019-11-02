#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

class Utils:

    @staticmethod
    def onehot(self, i, value):
        if(i == value):
            return 1
        else:
            return 0

    @staticmethod
    def getOrdListSimpleGate(self, p, Gate):
        list = []
        for i in range(1,self.num+1):
            if i == p:
                list.append(Gate)
            else:
                list.append(eye(2))
        return list

    @staticmethod
    def getOrdListCtrlGate(self, p1, p2, Gate):
        ketbra0 = Matrix([[1, 0], [0, 0]]) # |0><0|
        ketbra1 = Matrix([[0, 0], [0, 1]]) # |1><1|
        list1 = []
        list2 = []
        for i in range(1,self.num+1):
            if i == p1:
                list1.append(ketbra0)
                list2.append(ketbra1)
            elif i == p2:
                list1.append(eye(2))
                list2.append(Gate)
            else:
                list1.append(eye(2))
                list2.append(eye(2))
        return list1, list2