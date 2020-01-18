#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger
from IPython.display import display, Math, Latex

from logicqubit.hilbert import *
from logicqubit.gates import *
from logicqubit.circuit import *
from logicqubit.utils import *

class Qubits(Hilbert):

    def __init__(self, qubits_number, symbolic):
        Qubits.__q_number = qubits_number
        Qubits.__symbolic = symbolic
        Qubits.__number = 0
        if(not Qubits.__symbolic):
            Qubits.__psi = self.product([self.ket(0) for i in range(Qubits.__q_number)]) # o qubit 1 é o primeiro a esquerda
        else:
            a = symbols([str(i) + "a" + str(i) + "_0" for i in range(1, Qubits.__q_number + 1)])
            b = symbols([str(i) + "b" + str(i) + "_1" for i in range(1, Qubits.__q_number + 1)])
            Qubits.__psi = self.product([a[i]*self.ket(0)+b[i]*self.ket(1) for i in range(Qubits.__q_number)])

    def addQubit(self):
        if(Qubits.__number+1 <= Qubits.__q_number):
            Qubits.__number += 1

    def getAddQubitNumber(self):
        return Qubits.__number

    def getQubitsNumber(self):
        return Qubits.__q_number

    def isSymbolic(self):
        return Qubits.__symbolic == True

    def getPsi(self):
        return Qubits.__psi

    def setPsi(self,psi):
        Qubits.__psi = psi

    def setOperation(self, operator):
        Qubits.__psi = operator * Qubits.__psi
        Qubits.__last_operator = operator

    def qubitsToList(self, values):
        result = []
        for value in values:
            if (isinstance(value, Qubit)):
                result.append(value.getId())
            else:
                result.append(value)
        return result

    def setSymbolValuesForAll(self, a, b):
        if(Qubits.__symbolic):
            for i in range(1, Qubits.__q_number+1):
                Qubits.psi = Qubits.psi.subs(str(i)+"a"+str(i)+"_0", a)
                Qubits.psi = Qubits.psi.subs(str(i)+"a"+str(i)+"_1", a)
                Qubits.psi = Qubits.psi.subs(str(i)+"b"+str(i)+"_0", b)
                Qubits.psi = Qubits.psi.subs(str(i)+"b"+str(i)+"_1", b)
        else:
            print("This session is not symbolic!")

    def setSymbolValuesForListId(self, id, a, b):
        if(Qubits.__symbolic):
            list_id = self.qubitsToList(id)
            for i in list_id:
                Qubits.psi = Qubits.psi.subs(str(i)+"a"+str(i)+"_0", a)
                Qubits.psi = Qubits.psi.subs(str(i)+"a"+str(i)+"_1", a)
                Qubits.psi = Qubits.psi.subs(str(i)+"b"+str(i)+"_0", b)
                Qubits.psi = Qubits.psi.subs(str(i)+"b"+str(i)+"_1", b)
        else:
            print("This session is not symbolic!")

    def PrintState(self, simple = False):
        if(not self.__symbolic):
            value = latex(Qubits.__psi)
        else:
            value = Utils.texfix(Qubits.__psi, self.__q_number)

        if(not simple):
            display(Math(value))
        else:
            print(value)

    def PrintLastOperator(self, tex = True):
        if(tex):
            value = latex(Qubits.__last_operator)
            display(Math(value))
        else:
            print(Qubits.__last_operator)


class Qubit(Qubits, Gates, Circuit):
    def __init__(self, id = None):
        if(id == None):
            self.addQubit()
            self.__id = self.getAddQubitNumber()
        else:
            self.__id = id
        self.__name = "q"+str(self.__id)

    def __eq__(self, other):
        return self.__id == other

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def getId(self):
        return self.__id

    def setSymbolValues(self, a, b):
        self.setSymbolValuesForListId([self.__id], a, b)

    def X(self):
        self.addOp("X", [self.__id])
        list = self.getOrdListSimpleGate(self.__id, super().X())
        operator = self.product(list)
        self.setOperation(operator)

    def Y(self):
        self.addOp("Y", [self.__id])
        list = self.getOrdListSimpleGate(self.__id, super().Y())
        operator = self.product(list)
        self.setOperation(operator)

    def Z(self):
        self.addOp("Z", [self.__id])
        list = self.getOrdListSimpleGate(self.__id, super().Z())
        operator = self.product(list)
        self.setOperation(operator)

    def H(self):
        self.addOp("H", [self.__id])
        list = self.getOrdListSimpleGate(self.__id, super().H())
        operator = self.product(list)
        self.setOperation(operator)

    def U1(self, _lambda):
        self.addOp("U1", self.qubitsToList([self.__id, _lambda]))
        list = self.getOrdListSimpleGate(self.__id, super().U1(_lambda))
        operator = self.product(list)
        self.setOperation(operator)

    def U2(self, phi, _lambda):
        self.addOp("U2", self.qubitsToList([self.__id, phi, _lambda]))
        list = self.getOrdListSimpleGate(self.__id, super().U2(phi,_lambda))
        operator = self.product(list)
        self.setOperation(operator)

    def U3(self, theta, phi, _lambda):
        self.addOp("U3", self.qubitsToList([self.__id, theta, phi, _lambda]))
        list = self.getOrdListSimpleGate(self.__id, super().U3(theta, phi, _lambda))
        operator = self.product(list)
        self.setOperation(operator)

    def RX(self, theta):
        self.addOp("RX", self.qubitsToList([self.__id, theta]))
        list = self.getOrdListSimpleGate(self.__id, super().RX(theta))
        operator = self.product(list)
        self.setOperation(operator)

    def RY(self, theta):
        self.addOp("RY", self.qubitsToList([self.__id, theta]))
        list = self.getOrdListSimpleGate(self.__id, super().RY(theta))
        operator = self.product(list)
        self.setOperation(operator)

    def RZ(self, phi):
        self.addOp("RZ", self.qubitsToList([self.__id, phi]))
        list = self.getOrdListSimpleGate(self.__id, super().RZ(phi))
        operator = self.product(list)
        self.setOperation(operator)

    def CX(self, control):
        self.addOp("CX", self.qubitsToList([control, self.__id]))
        list1,list2 = self.getOrdListCtrlGate(control, self.__id, super().X())
        operator = self.product(list1) + self.product(list2)
        self.setOperation(operator)

    def CNOT(self, control):
        self.CX(control)

    def CU1(self, control, _lambda):
        self.addOp("CU1", self.qubitsToList([control, self.__id, _lambda]))
        list1,list2 = self.getOrdListCtrlGate(control, self.__id, super().U1(_lambda))
        operator = self.product(list1) + self.product(list2)
        self.setOperation(operator)

    def CCX(self, control1, control2):
        self.addOp("CCX", self.qubitsToList([control1, control2, self.__id]))
        Gate = super().X()-eye(2)
        list1,list2 = self.getOrdListCtrl2Gate(control1, control2, self.__id, Gate)
        operator = self.product(list1) + self.product(list2)
        self.setOperation(operator)

    def Toffoli(self, control1, control2):
        self.CCX(control1, control2)

class QubitRegister(Qubit):
    def __init__(self, number = 3):
        self.number = number
        self.reg = [Qubit() for i in range(1,number+1)]

    def __getitem__(self, key):
        return self.reg[key]
