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
import matplotlib.pyplot as plt

from logicqubit.qubits import *
from logicqubit.gates import *
from logicqubit.circuit import *
from logicqubit.utils import *

class LogicQuBit(Qubits, Gates, Circuit):

    def __init__(self, qubits_number = 3, symbolic=False):
        super().__init__(qubits_number, symbolic)
        Gates.__init__(self, qubits_number)
        Circuit.__init__(self)
        self.__qubits_number = qubits_number
        self.__symbolic = symbolic
        self.__measured_qubits = []
        self.__measured_values = []

    def X(self, target):
        self.addOp("X", self.qubitsToList([target]))
        list = self.getOrdListSimpleGate(target, super().X())
        operator = self.product(list)
        self.setOperation(operator)

    def Y(self, target):
        self.addOp("Y", self.qubitsToList([target]))
        list = self.getOrdListSimpleGate(target, super().Y())
        operator = self.product(list)
        self.setOperator()
        self.setOperation(operator)

    def Z(self, target):
        self.addOp("Z", self.qubitsToList([target]))
        list = self.getOrdListSimpleGate(target, super().Z())
        operator = self.product(list)
        self.setOperation(operator)

    def H(self, target):
        self.addOp("H", self.qubitsToList([target]))
        list = self.getOrdListSimpleGate(target, super().H())
        operator = self.product(list)
        self.setOperation(operator)

    def U1(self, target, _lambda):
        self.addOp("U1", self.qubitsToList([target, _lambda]))
        list = self.getOrdListSimpleGate(target, super().U1(_lambda))
        operator = self.product(list)
        self.setOperation(operator)

    def U2(self, target, phi, _lambda):
        self.addOp("U2", self.qubitsToList([target, phi, _lambda]))
        list = self.getOrdListSimpleGate(target, super().U2(phi,_lambda))
        operator = self.product(list)
        self.setOperation(operator)

    def U3(self, target, theta, phi, _lambda):
        self.addOp("U3", self.qubitsToList([target, theta, phi, _lambda]))
        list = self.getOrdListSimpleGate(target, super().U3(theta, phi, _lambda))
        operator = self.product(list)
        self.setOperation(operator)

    def RX(self, target, theta):
        self.addOp("RX", self.qubitsToList([target, theta]))
        list = self.getOrdListSimpleGate(target, super().RX(theta))
        operator = self.product(list)
        self.setOperation(operator)

    def RY(self, target, theta):
        self.addOp("RY", self.qubitsToList([target, theta]))
        list = self.getOrdListSimpleGate(target, super().RY(theta))
        operator = self.product(list)
        self.setOperation(operator)

    def RZ(self, target, phi):
        self.addOp("RZ", self.qubitsToList([target, phi]))
        list = self.getOrdListSimpleGate(target, super().RZ(phi))
        operator = self.product(list)
        self.setOperation(operator)

    def CX(self, control, target):
        self.addOp("CX", self.qubitsToList([control, target]))
        list1,list2 = self.getOrdListCtrlGate(control, target, super().X())
        operator = self.product(list1) + self.product(list2)
        self.setOperation(operator)

    def CNOT(self, control, target):
        self.CX(control, target)

    def CU1(self, control, target, _lambda):
        self.addOp("CU1", self.qubitsToList([control, target, _lambda]))
        list1,list2 = self.getOrdListCtrlGate(control, target, super().U1(_lambda))
        operator = self.product(list1) + self.product(list2)
        self.setOperation(operator)

    def CCX(self, control1, control2, target):
        self.addOp("CCX", self.qubitsToList([control1, control2, target]))
        Gate = super().X()-eye(2)
        list1,list2 = self.getOrdListCtrl2Gate(control1, control2, target, Gate)
        operator = self.product(list1) + self.product(list2)
        self.setOperation(operator)

    def Toffoli(self, control1, control2, target):
        self.CCX(control1, control2, target)

    def DensityMatrix(self):
        density_m = self.getPsi() * self.getPsi().adjoint()
        return density_m

    def Measure_One(self, target):
        self.addOp("Measure", self.qubitsToList([target])[0])
        density_m = self.DensityMatrix()
        list = self.getOrdListSimpleGate(target, super().P0())
        P0 = self.product(list)
        list = self.getOrdListSimpleGate(target, super().P1())
        P1 = self.product(list)
        measure_0 = (density_m*P0).trace()
        measure_1 = (density_m*P1).trace()
        self.__measured_qubits = target
        self.__measured_values = [measure_0, measure_1]
        return [measure_0, measure_1]

    def Measure(self, target):
        self.addOp("Measure", self.qubitsToList(target))
        #target.sort()
        self.__measured_qubits = target
        density_m = self.DensityMatrix()
        size_p = len(target)  # número de bits a ser medidos
        size = 2 ** size_p
        result = []
        for i in range(size):
            tlist = [eye(2) for tl in range(self.__qubits_number)]
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
            M = self.product(tlist)
            measure = (density_m * M).trace()
            result.append(measure)
        self.__measured_values = result
        return result

    def Plot(self):
        size_p = len(self.__measured_qubits)  # número de bits a ser medidos
        size = 2 ** size_p
        names = ["|" + "{0:b}".format(i).zfill(size_p) + ">" for i in range(size)]
        values = self.__measured_values
        plt.bar(names, values)
        plt.suptitle('')
        plt.show()

    def Pure(self):
        density_m = self.DensityMatrix()
        pure = (density_m*density_m).trace()
        return pure