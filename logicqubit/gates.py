#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp
import cupy as cp
from cmath import *

from logicqubit.hilbert import *

class Gates(Hilbert):

    def __init__(self, qubits_number):
        Gates.__qubits_number = qubits_number

    def Matrix(self, input):
        if(self.getCuda()):
            M = cp.array(input)
        else:
            M = sp.Matrix(input)
        return M

    def ID(self):
        M = self.Matrix([[1, 0], [0, 1]])
        return M

    def P0(self):
        M = self.Matrix([[1, 0], [0, 0]])  # |0><0|
        return M

    def P1(self):
        M = self.Matrix([[0, 0], [0, 1]])  # |1><1|
        return M

    def X(self, target):
        M = self.Matrix([[0, 1], [1, 0]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def Y(self, target):
        M = self.Matrix([[0, -1j], [1j, 0]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def Z(self, target):
        M = self.Matrix([[1, 0], [0, -1]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronkronProduct(list)
        return operator

    def V(self, target):
        M = (sp.I+1)/2*self.Matrix([[1, -1j], [-1j, 1]]) # sqrt(X) ou sqrt(NOT)
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def S(self, target):
        M = self.Matrix([[1, 0], [0, 1j]])  # sqrt(Z)
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def T(self, target):
        M = self.Matrix([[1, 0], [0, (1+I)/sqrt(2)]]) # sqrt(S)
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def H(self, target):
        M = 1 / sqrt(2) * self.Matrix([[1, 1], [1, -1]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U1(self, target, _lambda):
        M = self.Matrix([[1, 0], [0, exp(1j * _lambda)]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U2(self, target, phi, _lambda):
        M = self.Matrix([[1, -exp(1j * _lambda)], [exp(1j * phi), exp(1j * (phi + _lambda))]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U3(self, target, theta, phi, _lambda):
        M = self.Matrix([[cos(theta/2), -exp(1j*_lambda)*sin(theta/2)],
                    [exp(1j*phi)*sin(theta/2), exp(1j*(phi+_lambda))*cos(theta/2)]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def RX(self, target, theta):
        M = self.Matrix([[cos(theta/2), -1j*sin(theta/2)],
                    [-1j*sin(theta/2), cos(theta/2)]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def RY(self, target, theta):
        M = self.Matrix([[cos(theta/2), -sin(theta/2)],
                    [sin(theta/2), cos(theta/2)]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def RZ(self, target, phi):
        M = self.Matrix([[exp(-1j * phi / 2), 0], [0, exp(1j * phi / 2)]])
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def CX(self, control, target):
        M = self.Matrix([[0, 1], [1, 0]]) # X
        list1,list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CNOT(self, control, target):
        return self.CX(control, target)

    def CY(self, control, target):
        M = self.Matrix([[0, -1j], [1j, 0]])
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CZ(self, control, target):
        M = self.Matrix([[1, 0], [0, -1]])
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CU1(self, control, target, _lambda):
        M = self.Matrix([[1, 0], [0, exp(1j * _lambda)]])
        list1,list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CU2(self, control, target, phi, _lambda):
        M = self.Matrix([[1, -exp(1j * _lambda)], [exp(1j * phi), exp(1j * (phi + _lambda))]])
        list1,list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CU3(self, control, target, theta, phi, _lambda):
        M = self.Matrix([[cos(theta/2), -exp(1j*_lambda)*sin(theta/2)],
                    [exp(I*phi)*sin(theta/2), exp(1j*(phi+_lambda))*cos(theta/2)]])
        list1,list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CCX(self, control1, control2, target):
        Gate = self.Matrix([[0, 1], [1, 0]])-self.ID()
        list1,list2 = self.getOrdListCtrl2Gate(control1, control2, target, Gate)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def SWAP(self):
        M = self.Matrix([[1, 0, 0, 0], [0, 0, 1, 0],
                    [0, 1, 0, 0], [0, 0, 0, 1]])
        return M

    def Toffoli(self, control1, control2, target):
        return self.CCX(control1, control2, target)

    def getOrdListSimpleGate(self, target, Gate):
        list = []
        for i in range(1, Gates.__qubits_number+1):
            if i == target:
                list.append(Gate)
            else:
                list.append(self.Matrix([[1, 0],[0, 1]]))
        return list

    def getOrdListCtrlGate(self, control, target, Gate):
        list1 = []
        list2 = []
        for i in range(1, Gates.__qubits_number+1):
            if i == control:
                list1.append(self.P0())
                list2.append(self.P1())
            elif i == target:
                list1.append(self.ID())
                list2.append(Gate)
            else:
                list1.append(self.ID())
                list2.append(self.ID())
        return list1, list2

    def getOrdListCtrl2Gate(self, control1, control2, target, Gate):
        list1 = []
        list2 = []
        for i in range(1, Gates.__qubits_number+1):
            if i == control1 or i == control2:
                list1.append(self.ID())
                list2.append(self.P1())
            elif i == target:
                list1.append(self.ID())
                list2.append(Gate)
            else:
                list1.append(self.ID())
                list2.append(self.ID())
        return list1, list2