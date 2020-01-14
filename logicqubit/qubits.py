#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

from logicqubit.hilbert import *
from logicqubit.gates import *
from logicqubit.circuit import *
from logicqubit.utils import *

class Qubits(Hilbert):

    def __init__(self, qubits_number, symbolic):
        Qubits.full_number = qubits_number
        Qubits.symbolic = symbolic
        Qubits.number = 0
        if(not Qubits.symbolic):
            Qubits.psi = self.product([self.ket(0) for i in range(Qubits.full_number)]) # o qubit 1 é o primeiro a esquerda
        else:
            a = symbols([str(i) + "a" + str(i) + "_0" for i in range(1, Qubits.full_number + 1)])
            b = symbols([str(i) + "b" + str(i) + "_1" for i in range(1, Qubits.full_number + 1)])
            Qubits.psi = self.product([a[i]*self.ket(0)+b[i]*self.ket(1) for i in range(Qubits.full_number)])

    @staticmethod
    def addQubit():
        if(Qubits.number+1 <= Qubits.full_number):
            Qubits.number += 1

    @staticmethod
    def getQubitNumber():
        return Qubits.number

    @staticmethod
    def getPsi():
        return Qubits.psi

    @staticmethod
    def setPsi(psi):
        Qubits.psi = psi

class Qubit(Qubits, Gates, Circuit):
    def __init__(self, name = None):
        self.addQubit()
        self.id = self.getQubitNumber()
        if(name == None):
            self.name = "q"+str(self.id)
        else:
            self.name = name

    def __eq__(self, other):
        return self.id == other

    def __str__(self):
        return str(Qubits.psi)

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def X(self):
        self.addOp("X", [self.id])
        list = self.getOrdListSimpleGate(self.id, super().X())
        Qubits.psi = self.product(list)*Qubits.psi

    def Y(self):
        self.addOp("Y", [self.id])
        list = self.getOrdListSimpleGate(self.id, super().Y())
        Qubits.psi = self.product(list) * Qubits.psi

    def Z(self):
        self.addOp("Z", [self.id])
        list = self.getOrdListSimpleGate(self.id, super().Z())
        Qubits.psi = self.product(list) * Qubits.psi

    def H(self):
        self.addOp("H", [self.id])
        list = self.getOrdListSimpleGate(self.id, super().H())
        Qubits.psi = self.product(list)*Qubits.psi

    def U1(self, _lambda):
        self.addOp("U1", [self.id, _lambda])
        list = self.getOrdListSimpleGate(self.id, super().U1(_lambda))
        Qubits.psi = self.product(list) * Qubits.psi

    def U2(self, phi, _lambda):
        self.addOp("U2", [self.id, phi, _lambda])
        list = self.getOrdListSimpleGate(self.id, super().U2(phi,_lambda))
        Qubits.psi = self.product(list) * Qubits.psi

    def U3(self, theta, phi, _lambda):
        self.addOp("U3", [self.id, theta, phi, _lambda])
        list = self.getOrdListSimpleGate(self.id, super().U3(theta, phi, _lambda))
        Qubits.psi = self.product(list) * Qubits.psi

    def RX(self, theta):
        self.addOp("RX", [self.id, theta])
        list = self.getOrdListSimpleGate(self.id, super().RX(theta))
        Qubits.psi = self.product(list) * Qubits.psi

    def RY(self, theta):
        self.addOp("RY", [self.id, theta])
        list = self.getOrdListSimpleGate(self.id, super().RY(theta))
        Qubits.psi = self.product(list) * Qubits.psi

    def RZ(self, phi):
        self.addOp("RZ", [self.id, phi])
        list = self.getOrdListSimpleGate(self.id, super().RZ(phi))
        Qubits.psi = self.product(list) * Qubits.psi

    def CX(self, control):
        self.addOp("CX", [control, self.id])
        list1,list2 = self.getOrdListCtrlGate(control, self.id, super().X())
        product = self.product(list1) + self.product(list2)
        Qubits.psi = product * Qubits.psi

    def CNOT(self, control):
        self.CX(control)

    def CU1(self, control, _lambda):
        self.addOp("CU1", [control, self.id, _lambda])
        list1,list2 = self.getOrdListCtrlGate(control, self.id, super().U1(_lambda))
        product = self.product(list1) + self.product(list2)
        Qubits.psi = product * Qubits.psi

    def CCX(self, control1, control2):
        self.addOp("CCX", [control1, control2, self.id])
        Gate = super().X()-eye(2)
        list1,list2 = self.getOrdListCtrl2Gate(control1, control2, self.id, Gate)
        product = self.product(list1) + self.product(list2)
        Qubits.psi = product * Qubits.psi

    def Toffoli(self, control1, control2):
        self.CCX(control1, control2)

class QubitRegister(Qubit):
    def __init__(self, number = 3):
        self.number = number
        self.reg = [Qubit() for i in range(1,number+1)]

    def __getitem__(self, key):
        return self.reg[key]
