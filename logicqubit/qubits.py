#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from IPython.display import display, Math, Latex

from logicqubit.hilbert import *
from logicqubit.gates import *
from logicqubit.circuit import *
from logicqubit.utils import *

class Qubits(Hilbert):

    def __init__(self):
        Qubits.__number = 0
        Qubits.__used_qubits = []
        Qubits.__measured_qubits = []
        Qubits.__measured_values = []
        if self.getCuda():
            Qubits.__psi = self.kronProduct([self.ket(0) for i in range(self.getNumberOfQubits())])
        else:
            if self.isFirstLeft():  # qubit 1 is the first on the left
                a = sp.symbols([str(i) + "a" + str(i) + "_0" for i in range(1, self.getNumberOfQubits() + 1)])
                b = sp.symbols([str(i) + "b" + str(i) + "_1" for i in range(1, self.getNumberOfQubits() + 1)])
            else:
                a = sp.symbols([str(self.getNumberOfQubits()+1-i) + "a" + str(i) + "_0" for i in reversed(range(1, self.getNumberOfQubits() + 1))])
                b = sp.symbols([str(self.getNumberOfQubits()+1-i) + "b" + str(i) + "_1" for i in reversed(range(1, self.getNumberOfQubits() + 1))])
            Qubits.__psi = self.kronProduct([self.ket(0)*a[i]+self.ket(1)*b[i] for i in range(self.getNumberOfQubits())])

    def addQubit(self, id=None):
        if(len(Qubits.__used_qubits) < self.getNumberOfQubits()):
            if(id != None):
                if(not id in Qubits.__used_qubits):
                    Qubits.__used_qubits.append(id)
                else:
                    print("Qubit already used!")
            else:
                id = self.getLowestIdAvailable()
                Qubits.__used_qubits.append(id)
            return id
        else:
            print("All qubits have already been used!")
            return None

    def getLowestIdAvailable(self):
        all = list(range(1, self.getNumberOfQubits() + 1))
        for i in Qubits.__used_qubits:
            all.remove(i)
        return min(all)

    def getBiggestIdAvailable(self):
        all = list(range(1, self.getNumberOfQubits() + 1))
        for i in Qubits.__used_qubits:
            all.remove(i)
        return max(all)

    def getQubitsNumber(self):
        return self.getNumberOfQubits()

    def getUsedQubits(self):
        return len(Qubits.__used_qubits)

    def setMeasuredQubits(self, target):
        if(isinstance(target, list)):
            for id in target:
                Qubits.__measured_qubits.append(id)
        else:
            Qubits.__measured_qubits.append(target)

    def getMeasuredQubits(self):
        return Qubits.__measured_qubits

    def isMeasured(self, target):
        if (isinstance(target, list)):
            for id in target:
                if(id in Qubits.__measured_qubits):
                    print("Qubit "+str(id)+" alredy measured!")
                    return True
        else:
            if(target in Qubits.__measured_qubits):
                return True
        return False

    def setMeasuredValues(self, value):
        Qubits.__measured_values = value

    def getMeasuredValues(self):
        return Qubits.__measured_values

    def setPsi(self, psi):
        Qubits.__psi = psi

    def getPsi(self):
        return Qubits.__psi

    def getDictPsi(self):
        size_p = self.getQubitsNumber()
        size = 2 ** size_p
        labels = ["{0:b}".format(i).zfill(size_p) for i in range(size)]
        if not self.getCuda():
            value_l = [Utils.textSymbolfix(str(value), self.getQubitsNumber(), self.isFirstLeft()) for value in Qubits.__psi.get()]
            dictPsi = {label: value_l[i] for i, label in enumerate(labels)}
        else:
            dictPsi = {label: Qubits.__psi.get()[i].item() for i, label in enumerate(labels)}
        return dictPsi

    def getPsiAtAngles(self, degree=False):
        angles = Qubits.__psi.getAngles()
        if(degree):
            angles = angles*180/pi
            angles = (angles + 360)%360
        return angles

    def getPsiAdjoint(self):
        result = Qubits.__psi.adjoint()
        return result

    def setOperation(self, operator):
        Qubits.__psi = self.product(operator, Qubits.__psi)
        Qubits.__last_operator = operator

    def qubitsToList(self, values):
        result = []
        for value in values:
            if (isinstance(value, Qubit)):
                result.append(value.getId())
            else:
                result.append(value)
        return result

    def setSymbolValuesForAll(self, a, b):  # replace all symbols with real values
        if not self.getCuda():
            for i in range(1, self.getNumberOfQubits()+1):
                if (self.isFirstLeft()):
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"a"+str(i)+"_0", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"a"+str(i)+"_1", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"b"+str(i)+"_0", b), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"b"+str(i)+"_1", b), False)
                else:
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"a"+str(i)+"_0", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"a"+str(i)+"_1", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"b"+str(i)+"_0", b), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"b"+str(i)+"_1", b), False)
        else:
            print("This session is not symbolic!")

    def setSymbolValuesForListId(self, id, a, b):  # replace symbols with real values using a list of qubit ids
        if not self.getCuda():
            list_id = self.qubitsToList(id)
            for i in list_id:
                if (self.isFirstLeft()):
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"a"+str(i)+"_0", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"a"+str(i)+"_1", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"b"+str(i)+"_0", b), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+"b"+str(i)+"_1", b), False)
                else:
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"a"+str(i)+"_0", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"a"+str(i)+"_1", a), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"b"+str(i)+"_0", b), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+"b"+str(i)+"_1", b), False)
        else:
            print("This session is not symbolic!")

    def setSymbolValue(self, id, symbol, value):  # replace symbols with real values by id of qubit
        if not self.getCuda():
            list_id = self.qubitsToList(id)
            for i in list_id:
                if self.isFirstLeft():
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+symbol+str(i)+"_0", value), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(i)+symbol+str(i)+"_1", value), False)
                else:
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+symbol+str(i)+"_0", value), False)
                    Qubits.__psi = Matrix(Qubits.__psi.get().subs(str(self.getNumberOfQubits()+1-i)+symbol+str(i)+"_1", value), False)
        else:
            print("This session is not symbolic!")

    def PrintState(self, simple = False):
        if self.getCuda():
            value = Utils.vec2tex(Qubits.__psi.get())
        else:
            value = Utils.texfix(Qubits.__psi.get(), self.getNumberOfQubits(), self.isFirstLeft())

        if(not simple):
            display(Math(value))
        else:
            print(value)

    def PrintLastOperator(self, tex = True):
        if(tex):
            value = sp.latex(Qubits.__last_operator.get())
            display(Math(value))
        else:
            print(Qubits.__last_operator.get())


"""
Allows to handle qubits without having to pass the id.
In this class the quantum gates methods perform and record the type of operation
"""
class Qubit(Qubits, Gates, Circuit):
    def __init__(self, id = None):
        self.__id = self.addQubit(id)
        self.__name = "q"+str(self.__id)
        Gates.__init__(self, self.getQubitsNumber())

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

    # One qubit gates
    # .......................................
    def X(self):
        self.addOp("X", [self.__id])
        operator = super().X(self.__id)
        self.setOperation(operator)

    def Y(self):
        self.addOp("Y", [self.__id])
        operator = super().Y(self.__id)
        self.setOperation(operator)

    def Z(self):
        self.addOp("Z", [self.__id])
        operator = super().Z(self.__id)
        self.setOperation(operator)

    def V(self, adjoint = False):
        self.addOp("V", [self.__id])
        operator = super().V(self.__id, adjoint)
        self.setOperation(operator)

    def S(self, adjoint = False):
        self.addOp("S", [self.__id])
        operator = super().S(self.__id, adjoint)
        self.setOperation(operator)

    def T(self, adjoint = False):
        self.addOp("T", [self.__id])
        operator = super().T(self.__id, adjoint)
        self.setOperation(operator)

    def H(self):
        self.addOp("H", [self.__id])
        operator = super().H(self.__id)
        self.setOperation(operator)

    def U(self, *argv):
        self.addOp("U", self.qubitsToList([self.__id, argv]))
        operator = super().U(self.__id, argv)
        self.setOperation(operator)

    def U3(self, theta, phi, _lambda):
        self.addOp("U3", self.qubitsToList([self.__id, theta, phi, _lambda]))
        operator = super().U3(self.__id, theta, phi, _lambda)
        self.setOperation(operator)

    def U2(self, phi, _lambda):
        self.addOp("U2", self.qubitsToList([self.__id, phi, _lambda]))
        operator = super().U2(self.__id, phi, _lambda)
        self.setOperation(operator)

    def U1(self, _lambda):
        self.addOp("U1", self.qubitsToList([self.__id, _lambda]))
        operator = super().U1(self.__id, _lambda)
        self.setOperation(operator)

    def RX(self, theta):
        self.addOp("RX", self.qubitsToList([self.__id, theta]))
        operator = super().RX(self.__id, theta)
        self.setOperation(operator)

    def RY(self, theta):
        self.addOp("RY", self.qubitsToList([self.__id, theta]))
        operator = super().RY(self.__id, theta)
        self.setOperation(operator)

    def RZ(self, phi):
        self.addOp("RZ", self.qubitsToList([self.__id, phi]))
        operator = super().RZ(self.__id, phi)
        self.setOperation(operator)

    # Two qubit gates
    # .......................................
    def CH(self, control):
        self.addOp("CH", self.qubitsToList([control, self.__id]))
        operator = super().CH(control, self.__id)
        self.setOperation(operator)

    def CX(self, control):
        self.addOp("CX", self.qubitsToList([control, self.__id]))
        operator = super().CX(control, self.__id)
        self.setOperation(operator)

    def CNOT(self, control):
        self.CX(control)

    def CY(self, control):
        self.addOp("CY", self.qubitsToList([control, self.__id]))
        operator = super().CY(control, self.__id)
        self.setOperation(operator)

    def CZ(self, control):
        self.addOp("CZ", self.qubitsToList([control, self.__id]))
        operator = super().CZ(control, self.__id)
        self.setOperation(operator)

    def CV(self, control, adjoint = False):
        self.addOp("CV", self.qubitsToList([control, self.__id]))
        operator = super().CV(control, self.__id, adjoint)
        self.setOperation(operator)

    def CS(self, control, adjoint = False):
        self.addOp("CS", self.qubitsToList([control, self.__id]))
        operator = super().CS(control, self.__id, adjoint)
        self.setOperation(operator)

    def CT(self, control, adjoint = False):
        self.addOp("CT", self.qubitsToList([control, self.__id]))
        operator = super().CT(control, self.__id, adjoint)
        self.setOperation(operator)

    def CRX(self, control, theta):
        self.addOp("CRX", self.qubitsToList([control, self.__id, theta]))
        operator = super().CRX(control, self.__id, theta)
        self.setOperation(operator)

    def CRY(self, control, theta):
        self.addOp("CRY", self.qubitsToList([control, self.__id, theta]))
        operator = super().CRY(control, self.__id, theta)
        self.setOperation(operator)

    def CRZ(self, control, phi):
        self.addOp("CRZ", self.qubitsToList([control, self.__id, phi]))
        operator = super().CRZ(control, self.__id, phi)
        self.setOperation(operator)

    def CU(self, control, *argv):
        self.addOp("CU", self.qubitsToList([control, self.__id]))
        operator = super().CU(control, self.__id, argv)
        self.setOperation(operator)

    def CU3(self, control, theta, phi, _lambda):
        self.addOp("CU3", self.qubitsToList([control, self.__id, theta, phi, _lambda]))
        operator = super().CU3(control, self.__id, theta, phi, _lambda)
        self.setOperation(operator)

    def CU2(self, control, phi, _lambda):
        self.addOp("CU2", self.qubitsToList([control, self.__id, phi, _lambda]))
        operator = super().CU2(control, self.__id, phi, _lambda)
        self.setOperation(operator)

    def CU1(self, control, _lambda):
        self.addOp("CU1", self.qubitsToList([control, self.__id, _lambda]))
        operator = super().CU1(control, self.__id, _lambda)
        self.setOperation(operator)

    def SWAP(self, target):
        self.addOp("SWAP", self.qubitsToList([self.__id, target]))
        operator = super().SWAP(self.__id, target)
        self.setOperation(operator)

    def Controlled(self, name, control, target, adjoint = False):
        self.addOp(name, self.qubitsToList([control, self.__id]))
        functions = {'X': super().CX, 'Y': super().CY, 'Z': super().CZ}
        operator = functions[name](control[0], control[1], self.__id)
        self.setOperation(operator)

    # Three qubit gates
    # .......................................
    def CCX(self, control1, control2):
        self.addOp("CCX", self.qubitsToList([control1, control2, self.__id]))
        operator = super().CCX(control1, control2, self.__id)
        self.setOperation(operator)

    def Toffoli(self, control1, control2):
        self.CCX(control1, control2)

    def Fredkin(self, target1, target2):
        self.addOp("Fredkin", self.qubitsToList([self.__id, target1, target2]))
        operator = super().Fredkin(self.__id, target1, target2)
        self.setOperation(operator)


"""
Registering qubits allows you to perform the same operation on several quibts at the same time.
In this class the quantum gates methods perform and record the type of operation.
"""
class QubitRegister(Qubit):
    def __init__(self, number = 3):
        self.__number = number
        if(self.getUsedQubits() < self.getQubitsNumber()):
            self.__reg = [Qubit() for i in range(1, number+1)]

    def __getitem__(self, key):
        return self.__reg[key-1]

    def getQubits(self):
        return self.__reg

    def X(self):
        for qubit in self.__reg:
            qubit.X()

    def Y(self):
        for qubit in self.__reg:
            qubit.Y()

    def Z(self):
        for qubit in self.__reg:
            qubit.Z()

    def V(self, target):
        for qubit in self.__reg:
            qubit.V()

    def S(self, target):
        for qubit in self.__reg:
            qubit.S()

    def T(self, target):
        for qubit in self.__reg:
            qubit.T()

    def H(self):
        for qubit in self.__reg:
            qubit.H()
