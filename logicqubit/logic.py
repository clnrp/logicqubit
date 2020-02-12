#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp
from sympy.physics.quantum import TensorProduct
from cmath import *
import matplotlib.pyplot as plt

from logicqubit.qubits import *
from logicqubit.gates import *
from logicqubit.circuit import *
from logicqubit.utils import *

class LogicQuBit(Qubits, Gates, Circuit):

    def __init__(self, qubits_number = 3, **kwargs):
        self.__cuda = kwargs.get('cuda', True)
        self.__symbolic = kwargs.get('symbolic', False)
        self.__qubits_number = qubits_number
        if(self.__symbolic):
            self.__cuda = False
        super().setCuda(self.__cuda)
        super().__init__(qubits_number, self.__symbolic)
        Gates.__init__(self, qubits_number)
        Circuit.__init__(self)

    def X(self, target):
        self.addOp("X", self.qubitsToList([target]))
        operator = super().X(target)
        self.setOperation(operator)

    def Y(self, target):
        self.addOp("Y", self.qubitsToList([target]))
        operator = super().Y(target)
        self.setOperation(operator)

    def Z(self, target):
        self.addOp("Z", self.qubitsToList([target]))
        operator = super().Z(target)
        self.setOperation(operator)

    def V(self, target):
        self.addOp("V", self.qubitsToList([target]))
        operator = super().V(target)
        self.setOperation(operator)

    def S(self, target):
        self.addOp("S", self.qubitsToList([target]))
        operator = super().S(target)
        self.setOperation(operator)

    def T(self, target):
        self.addOp("T", self.qubitsToList([target]))
        operator = super().T(target)
        self.setOperation(operator)

    def H(self, target):
        self.addOp("H", self.qubitsToList([target]))
        operator = super().H(target)
        self.setOperation(operator)

    def U1(self, target, _lambda):
        self.addOp("U1", self.qubitsToList([target, _lambda]))
        operator = super().U1(target, _lambda)
        self.setOperation(operator)

    def U2(self, target, phi, _lambda):
        self.addOp("U2", self.qubitsToList([target, phi, _lambda]))
        operator = super().U2(target, phi, _lambda)
        self.setOperation(operator)

    def U3(self, target, theta, phi, _lambda):
        self.addOp("U3", self.qubitsToList([target, theta, phi, _lambda]))
        operator = super().U3(target, theta, phi, _lambda)
        self.setOperation(operator)

    def RX(self, target, theta):
        self.addOp("RX", self.qubitsToList([target, theta]))
        operator = super().RX(target, theta)
        self.setOperation(operator)

    def RY(self, target, theta):
        self.addOp("RY", self.qubitsToList([target, theta]))
        operator = super().RY(target, theta)
        self.setOperation(operator)

    def RZ(self, target, phi):
        self.addOp("RZ", self.qubitsToList([target, phi]))
        operator = super().RZ(target, phi)
        self.setOperation(operator)

    def CX(self, control, target):
        self.addOp("CX", self.qubitsToList([control, target]))
        operator = super().CX(control, target)
        self.setOperation(operator)

    def CNOT(self, control, target):
        self.CX(control, target)

    def CY(self, control, target):
        self.addOp("CY", self.qubitsToList([control, target]))
        operator = super().CY(control, target)
        self.setOperation(operator)

    def CZ(self, control, target):
        self.addOp("CZ", self.qubitsToList([control, target]))
        operator = super().CZ(control, target)
        self.setOperation(operator)

    def CU1(self, control, target, _lambda):
        self.addOp("CU1", self.qubitsToList([control, target, _lambda]))
        operator = super().CU1(control, target, _lambda)
        self.setOperation(operator)

    def CCX(self, control1, control2, target):
        self.addOp("CCX", self.qubitsToList([control1, control2, target]))
        operator = super().CCX(control1, control2, target)
        self.setOperation(operator)

    def Toffoli(self, control1, control2, target):
        self.CCX(control1, control2, target)

    def DensityMatrix(self):
        density_m = self.getPsi() * self.getPsiAdjoint()
        return density_m

    def Measure_One(self, target):
        if(self.isNotMeasured(target)):
            self.addOp("Measure", self.qubitsToList([target])[0])
            density_m = self.DensityMatrix()
            list = self.getOrdListSimpleGate(target, super().P0())
            P0 = self.kronProduct(list)
            list = self.getOrdListSimpleGate(target, super().P1())
            P1 = self.kronProduct(list)
            measure_0 = (density_m*P0).trace()
            measure_1 = (density_m*P1).trace()
            self.setMeasuredQubits(target)
            self.setMeasuredValues([measure_0, measure_1])
            return [measure_0, measure_1]
        else:
            print("qubit already measured!")

    def Measure(self, target):
        self.addOp("Measure", self.qubitsToList(target))
        #target.sort()
        self.setMeasuredQubits(target)
        density_m = self.DensityMatrix()
        size_p = len(target)  # número de bits a ser medidos
        size = 2 ** size_p
        result = []
        for i in range(size):
            tlist = [self.ID() for tl in range(self.__qubits_number)]
            blist = [i >> bl & 0x1 for bl in range(size_p)] # bits de cada i
            cnt = 0
            for j in range(self.__qubits_number):
                if j + 1 == target[cnt]:
                    if blist[cnt] == 0:
                        tlist[j] = super().P0()
                    else:
                        tlist[j] = super().P1()
                    cnt += 1
                    if (cnt >= size_p):
                        break
            M = self.kronProduct(tlist)
            measure = (density_m * M).trace()
            if(self.__cuda):
                measure = measure.item().real
            result.append(measure)
        self.setMeasuredValues(result)
        return result

    def Plot(self):
        size_p = len(self.getMeasuredQubits())  # número de bits medidos
        size = 2 ** size_p
        names = ["|" + "{0:b}".format(i).zfill(size_p) + ">" for i in range(size)]
        values = self.getMeasuredValues()
        plt.bar(names, values)
        plt.suptitle('')
        plt.show()

    def Pure(self):
        density_m = self.DensityMatrix()
        pure = (density_m*density_m).trace()
        return pure