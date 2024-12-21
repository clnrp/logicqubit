#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from cmath import *
from logicqubit.hilbert import *


"""
In this class, the numerical definition of operators is performed,
and the quantum gates methods performs the tensor product with the matrices in the correct order.
It is necessary to enter the qubit id as an input parameter.
"""
class Gates(Hilbert):

    def __init__(self, number_of_qubits=1):
        self.__number_of_qubits = number_of_qubits

    # basic matrices for the generation of operators
    # .......................................
    def ID(self):
        M = Matrix([[1, 0], [0, 1]], self.getCuda())
        return M

    def P0(self):
        M = Matrix([[1, 0], [0, 0]], self.getCuda())  # |0><0|
        return M

    def P1(self):
        M = Matrix([[0, 0], [0, 1]], self.getCuda())  # |1><1|
        return M

    def L0(self):
        M = Matrix([[0, 1], [0, 0]], self.getCuda())  # |0><1|
        return M

    def L1(self):
        M = Matrix([[0, 0], [1, 0]], self.getCuda())  # |1><0|
        return M

    # One qubit gates
    # input parameters: target
    # .......................................
    def X(self, target=1):
        M = Matrix([[0, 1], [1, 0]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def Y(self, target=1):
        M = Matrix([[0, -1j], [1j, 0]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def Z(self, target=1):
        M = Matrix([[1, 0], [0, -1]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def V(self, target=1, adjoint=False):
        M = Matrix([[1, -1j], [-1j, 1]], self.getCuda()) * ((1j + 1) / 2)  # sqrt(X) ou sqrt(NOT)
        if adjoint:
            M = M.adjoint()
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def S(self, target=1, adjoint=False):
        M = Matrix([[1, 0], [0, 1j]], self.getCuda())  # sqrt(Z)
        if adjoint:
            M = M.adjoint()
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def T(self, target=1, adjoint=False):
        M = Matrix([[1, 0], [0, (1 + 1j) / sqrt(2)]], self.getCuda())  # sqrt(S)
        if adjoint:
            M = M.adjoint()
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def H(self, target=1):
        M = Matrix([[1, 1], [1, -1]], self.getCuda()) * (1 / sqrt(2))
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U(self, target, *argv):  # U or theta, phi and _lambda
        if len(argv) == 1:
            M = Matrix(argv[0][0], self.getCuda())
        else:
            theta = argv[0]
            phi = argv[1]
            _lambda = argv[2]
            M = Matrix(
                [[exp(-1j * (phi + _lambda) / 2) * cos(theta / 2), -exp(-1j * (phi - _lambda) / 2) * sin(theta / 2)],
                 [exp(-1j * (phi - _lambda) / 2) * sin(theta / 2), exp(1j * (phi + _lambda)) * cos(theta / 2)]],
                self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U3(self, target, theta, phi, _lambda):
        M = Matrix([[cos(theta / 2), -exp(1j * _lambda) * sin(theta / 2)],
                    [exp(1j * phi) * sin(theta / 2), exp(1j * (phi + _lambda)) * cos(theta / 2)]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U2(self, target, phi, _lambda):
        M = Matrix([[1, -exp(1j * _lambda)], [exp(1j * phi), exp(1j * (phi + _lambda))]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def U1(self, target, _lambda):
        M = Matrix([[1, 0], [0, exp(1j * _lambda)]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def RX(self, target, theta):
        M = Matrix([[cos(theta / 2), -1j * sin(theta / 2)],
                    [-1j * sin(theta / 2), cos(theta / 2)]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def RY(self, target, theta):
        M = Matrix([[cos(theta / 2), -sin(theta / 2)],
                    [sin(theta / 2), cos(theta / 2)]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    def RZ(self, target, phi):
        M = Matrix([[exp(-1j * phi / 2), 0], [0, exp(1j * phi / 2)]], self.getCuda())
        list = self.getOrdListSimpleGate(target, M)
        operator = self.kronProduct(list)
        return operator

    # Two qubit gates
    # input parameters: control and target
    # .......................................
    def CH(self, control, target):
        M = Matrix([[1, 1], [1, -1]], self.getCuda()) * (1 / sqrt(2)) # H
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator
    
    def CX(self, control, target):
        M = Matrix([[0, 1], [1, 0]], self.getCuda())  # X
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CNOT(self, control, target):
        return self.CX(control, target)

    def CY(self, control, target):
        M = Matrix([[0, -1j], [1j, 0]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CZ(self, control, target):
        M = Matrix([[1, 0], [0, -1]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CV(self, control, target, adjoint=False):
        M = Matrix([[1, -1j], [-1j, 1]], self.getCuda()) * ((1j + 1) / 2)  # sqrt(X) ou sqrt(NOT)
        if adjoint:
            M = M.adjoint()
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CS(self, control, target, adjoint=False):
        M = Matrix([[1, 0], [0, 1j]], self.getCuda())  # sqrt(Z)
        if adjoint:
            M = M.adjoint()
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CT(self, control, target, adjoint=False):
        M = Matrix([[1, 0], [0, (1 + 1j) / sqrt(2)]], self.getCuda())  # sqrt(S)
        if adjoint:
            M = M.adjoint()
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CRX(self, control, target, theta):
        M = Matrix([[cos(theta / 2), -1j * sin(theta / 2)],
                    [-1j * sin(theta / 2), cos(theta / 2)]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CRY(self, control, target, theta):
        M = Matrix([[cos(theta / 2), -sin(theta / 2)],
                    [sin(theta / 2), cos(theta / 2)]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CRZ(self, control, target, phi):
        M = Matrix([[exp(-1j * phi / 2), 0], [0, exp(1j * phi / 2)]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    # generic controlled gate
    def CU(self, control, target, *argv):  # U or theta, phi and _lambda
        if len(argv) == 1:
            M = Matrix(argv[0][0], self.getCuda())
        else:
            theta = argv[0]
            phi = argv[1]
            _lambda = argv[2]
            M = Matrix(
                [[exp(-1j * (phi + _lambda) / 2) * cos(theta / 2), -exp(-1j * (phi - _lambda) / 2) * sin(theta / 2)],
                 [exp(1j * (phi - _lambda) / 2) * sin(theta / 2), exp(1j * (phi + _lambda)) * cos(theta / 2)]],
                self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CU3(self, control, target, theta, phi, _lambda):
        M = Matrix([[cos(theta / 2), -exp(1j * _lambda) * sin(theta / 2)],
                    [exp(1j * phi) * sin(theta / 2), exp(1j * (phi + _lambda)) * cos(theta / 2)]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CU2(self, control, target, phi, _lambda):
        M = Matrix([[1, -exp(1j * _lambda)], [exp(1j * phi), exp(1j * (phi + _lambda))]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def CU1(self, control, target, _lambda):
        M = Matrix([[1, 0], [0, exp(1j * _lambda)]], self.getCuda())
        list1, list2 = self.getOrdListCtrlGate(control, target, M)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    # performs a state change of two qubits
    def SWAP(self, target1, target2):
        list1, list2, list3, list4 = self.getOrdListSWAP(target1, target2)
        operator = self.kronProduct(list1) + self.kronProduct(list2) + self.kronProduct(list3) + self.kronProduct(list4)
        return operator

    # Three qubit gates, which perform and record the operation
    # input parameters: control1, control2, and target
    # .......................................
    def CCX(self, control1, control2, target):
        Gate = Matrix([[0, 1], [1, 0]], self.getCuda()) - self.ID()
        list1, list2 = self.getOrdListCtrl2Gate(control1, control2, target, Gate)
        operator = self.kronProduct(list1) + self.kronProduct(list2)
        return operator

    def Toffoli(self, control1, control2, target):
        return self.CCX(control1, control2, target)

    # it's a controlled SWAP
    def Fredkin(self, control, target1, target2):
        list1, list2, list3, list4, list5, list6 = self.getOrdListFredkin(control, target1, target2)
        ID = self.kronProduct(list1)
        P1_SWAP = self.kronProduct(list2) + self.kronProduct(list3) + self.kronProduct(list4) + self.kronProduct(list5)
        P1_ID = self.kronProduct(list6)
        operator = ID + (P1_SWAP-P1_ID)
        return operator

    # orders the matrices for the tensor product of 1 qubit operations
    def getOrdListSimpleGate(self, target, Gate):
        list = []
        if self.isFirstLeft():
            plist = range(1, self.__number_of_qubits + 1)
        else:
            plist = reversed(range(1, self.__number_of_qubits + 1))
        for i in plist:
            if i == target:
                list.append(Gate)
            else:
                list.append(Matrix([[1, 0], [0, 1]], self.getCuda()))
        return list

    # orders the matrices for the tensor product of 2 qubits operations
    def getOrdListCtrlGate(self, control, target, Gate):
        list1 = []
        list2 = []
        if self.isFirstLeft():
            plist = range(1, self.__number_of_qubits + 1)
        else:
            plist = reversed(range(1, self.__number_of_qubits + 1))
        for i in plist:
            if i == control:
                list1.append(self.P0())  # |0><0|
                list2.append(self.P1())  # |1><1|
            elif i == target:
                list1.append(self.ID())
                list2.append(Gate)
            else:
                list1.append(self.ID())
                list2.append(self.ID())
        return list1, list2

    # orders the matrices for the tensor product of 3 qubits operations
    def getOrdListCtrl2Gate(self, control1, control2, target, Gate):
        list1 = []
        list2 = []
        if self.isFirstLeft():
            plist = range(1, self.__number_of_qubits + 1)
        else:
            plist = reversed(range(1, self.__number_of_qubits + 1))
        for i in plist:
            if i == control1 or i == control2:
                list1.append(self.ID())
                list2.append(self.P1())  # |1><1|
            elif i == target:
                list1.append(self.ID())
                list2.append(Gate)
            else:
                list1.append(self.ID())
                list2.append(self.ID())
        return list1, list2

    # orders the matrices for the tensor product of the SWAP gate operation
    def getOrdListSWAP(self, target1, target2):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        if self.isFirstLeft():
            plist = range(1, self.__number_of_qubits + 1)
        else:
            plist = reversed(range(1, self.__number_of_qubits + 1))
        for i in plist:
            if i == target1:
                list1.append(self.P0())  # |0><0|
                list2.append(self.L0())  # |0><1|
                list3.append(self.L1())  # |1><0|
                list4.append(self.P1())  # |1><1|
            elif i == target2:
                list1.append(self.P0())  # |0><0|
                list2.append(self.L1())  # |1><0|
                list3.append(self.L0())  # |0><1|
                list4.append(self.P1())  # |1><1|
            else:
                list1.append(self.ID())
                list2.append(self.ID())
                list3.append(self.ID())
                list4.append(self.ID())
        return list1, list2, list3, list4

    # orders the matrices for the tensor product of the Fredkin gate operation
    def getOrdListFredkin(self, control, target1, target2):
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        if self.isFirstLeft():
            plist = range(1, self.__number_of_qubits + 1)
        else:
            plist = reversed(range(1, self.__number_of_qubits + 1))
        for i in plist:
            if i == control:
                list1.append(self.ID())  # ID
                list2.append(self.P1())  # SWAP P0xP0
                list3.append(self.P1())  # SWAP L0xL1
                list4.append(self.P1())  # SWAP L1xL0
                list5.append(self.P1())  # SWAP P1xP1
                list6.append(self.P1())  # -ID
            elif i == target1:
                list1.append(self.ID())
                list2.append(self.P0())  # |0><0|
                list3.append(self.L0())  # |0><1|
                list4.append(self.L1())  # |1><0|
                list5.append(self.P1())  # |1><1|
                list6.append(self.ID())
            elif i == target2:
                list1.append(self.ID())
                list2.append(self.P0())  # |0><0|
                list3.append(self.L1())  # |1><0|
                list4.append(self.L0())  # |0><1|
                list5.append(self.P1())  # |1><1|
                list6.append(self.ID())
            else:
                list1.append(self.ID())
                list2.append(self.ID())
                list3.append(self.ID())
                list4.append(self.ID())
                list5.append(self.ID())
                list6.append(self.ID())
        return list1, list2, list3, list4, list5, list6
