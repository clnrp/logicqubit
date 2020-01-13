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
from logicqubit.utils import *

class Qubits(Hilbert):

    def __init__(self, num = 3, symbolic = False):
        Qubits.full_number = num
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
    def getPsi():
        return Qubits.psi

    @staticmethod
    def setPsi(psi):
        Qubits.psi = psi

class Qubit(Qubits):
    def __init__(self, id = None, name = None):
        Qubit.addQubit()
        if(id == None):
            self.id = Qubits.number
        else:
            self.id = id
        if(name == None):
            self.name = "q"+str(self.id)
        else:
            self.name = name

    def __eq__(self, other):
        return self.id == other

    def __str__(self):
        return str(Qubits.psi)

class QubitRegister(Qubit):
    def __init__(self, number = 3):
        self.number = number
        self.reg = [Qubit() for i in range(1,number+1)]

    def __getitem__(self, key):
        return self.reg[key]
