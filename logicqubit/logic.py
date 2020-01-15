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
        self.qubits_number = qubits_number
        self.symbolic = symbolic
        self.measured_qubits = []
        self.measured_values = []

    def X(self, target):
        self.addOp("X", [target])
        list = self.getOrdListSimpleGate(target, super().X())
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def Y(self, target):
        self.addOp("Y", [target])
        list = self.getOrdListSimpleGate(target, super().Y())
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def Z(self, target):
        self.addOp("Z", [target])
        list = self.getOrdListSimpleGate(target, super().Z())
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def H(self, target):
        self.addOp("H", [target])
        list = self.getOrdListSimpleGate(target, super().H())
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def U1(self, target, _lambda):
        self.addOp("U1", [target, _lambda])
        list = self.getOrdListSimpleGate(target, super().U1(_lambda))
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def U2(self, target, phi, _lambda):
        self.addOp("U2", [target, phi, _lambda])
        list = self.getOrdListSimpleGate(target, super().U2(phi,_lambda))
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def U3(self, target, theta, phi, _lambda):
        self.addOp("U3", [target, theta, phi, _lambda])
        list = self.getOrdListSimpleGate(target, super().U3(theta, phi, _lambda))
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def RX(self, target, theta):
        self.addOp("RX", [target, theta])
        list = self.getOrdListSimpleGate(target, super().RX(theta))
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def RY(self, target, theta):
        self.addOp("RY", [target, theta])
        list = self.getOrdListSimpleGate(target, super().RY(theta))
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def RZ(self, target, phi):
        self.addOp("RZ", [target, phi])
        list = self.getOrdListSimpleGate(target, super().RZ(phi))
        Gates.operator = self.product(list)
        Qubits.psi = Gates.operator * Qubits.psi

    def CX(self, control, target):
        self.addOp("CX", [control, target])
        list1,list2 = self.getOrdListCtrlGate(control, target, super().X())
        Gates.operator = self.product(list1) + self.product(list2)
        Qubits.psi = Gates.operator * Qubits.psi

    def CNOT(self, control, target):
        self.CX(control, target)

    def CU1(self, control, target, _lambda):
        self.addOp("CU1", [control, target, _lambda])
        list1,list2 = self.getOrdListCtrlGate(control, target, super().U1(_lambda))
        Gates.operator = self.product(list1) + self.product(list2)
        Qubits.psi = Gates.operator * Qubits.psi

    def CCX(self, control1, control2, target):
        self.addOp("CCX", [control1, control2, target])
        Gate = super().X()-eye(2)
        list1,list2 = self.getOrdListCtrl2Gate(control1, control2, target, Gate)
        Gates.operator = self.product(list1) + self.product(list2)
        Qubits.psi = Gates.operator * Qubits.psi

    def Toffoli(self, control1, control2, target):
        self.CCX(control1, control2, target)

    def DensityMatrix(self):
        density_m = Qubits.psi * Qubits.psi.adjoint()
        return density_m

    def Measure_One(self, target):
        self.addOp("Measure", [target])
        density_m = self.DensityMatrix()
        list = self.getOrdListSimpleGate(target, super().P0())
        P0 = self.product(list)
        list = self.getOrdListSimpleGate(target, super().P1())
        P1 = self.product(list)
        measure_0 = (density_m*P0).trace()
        measure_1 = (density_m*P1).trace()
        self.measured_qubits = target
        self.measured_values = [measure_0, measure_1]
        return [measure_0, measure_1]

    def Measure(self, target):
        self.addOp("Measure", target)
        #target.sort()
        self.measured_qubits = target
        density_m = self.DensityMatrix()
        size_p = len(target)  # número de bits a ser medidos
        size = 2 ** size_p
        result = []
        for i in range(size):
            tlist = [eye(2) for tl in range(self.qubits_number)]
            blist = [i >> bl & 0x1 for bl in range(size_p)] # bits de cada i
            cnt = 0
            for j in range(self.qubits_number):
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
        self.measured_values = result
        return result

    def Plot(self):
        size_p = len(self.measured_qubits)  # número de bits a ser medidos
        size = 2 ** size_p
        names = ["|" + "{0:b}".format(i).zfill(size_p) + ">" for i in range(size)]
        values = self.measured_values
        plt.bar(names, values)
        plt.suptitle('')
        plt.show()

    def Pure(self):
        density_m = self.DensityMatrix()
        pure = (density_m*density_m).trace()
        return pure