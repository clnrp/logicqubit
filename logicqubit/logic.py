#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import random
import matplotlib.pyplot as plt
from matplotlib import cm

from logicqubit.qubits import *
from logicqubit.oracle import *
from logicqubit.utils import *

"""
Main class that allows you to create the circuit.
In this class the quantum gates methods perform and record the type of operation.
It is necessary to enter the qubit id as an input parameter.
"""
class LogicQuBit(Qubits, Gates, Circuit):

    def __init__(self, number_of_qubits = 3, **kwargs):
        symbolic = kwargs.get('symbolic', False)
        first_left = kwargs.get('first_left', True)  # qubit 1 is the left most
        super().setCuda(not symbolic)
        super().setFirstLeft(first_left)
        super().setNumberOfQubits(number_of_qubits)
        Qubits.__init__(self)
        Gates.__init__(self, number_of_qubits)
        Circuit.__init__(self)

    # One qubit gates
    # input parameters: target
    # .......................................
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

    def U(self, target, *argv):
        self.addOp("U", self.qubitsToList([target, argv]))
        operator = super().U(target, argv)
        self.setOperation(operator)

    def U3(self, target, theta, phi, _lambda):
        self.addOp("U3", self.qubitsToList([target, theta, phi, _lambda]))
        operator = super().U3(target, theta, phi, _lambda)
        self.setOperation(operator)

    def U2(self, target, phi, _lambda):
        self.addOp("U2", self.qubitsToList([target, phi, _lambda]))
        operator = super().U2(target, phi, _lambda)
        self.setOperation(operator)

    def U1(self, target, _lambda):
        self.addOp("U1", self.qubitsToList([target, _lambda]))
        operator = super().U1(target, _lambda)
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

    # Two qubit gates
    # input parameters: control and target
    # .......................................
    def CH(self, control, target):
        self.addOp("CH", self.qubitsToList([control, target]))
        operator = super().CH(control, target)
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

    def CRX(self, control, target, theta):
        self.addOp("CRX", self.qubitsToList([control, target, theta]))
        operator = super().CRX(control, target, theta)
        self.setOperation(operator)

    def CRY(self, control, target, theta):
        self.addOp("CRY", self.qubitsToList([control, target, theta]))
        operator = super().CRY(control, target, theta)
        self.setOperation(operator)

    def CRZ(self, control, target, phi):
        self.addOp("CRZ", self.qubitsToList([control, target, phi]))
        operator = super().CRZ(control, target, phi)
        self.setOperation(operator)

    def CU(self, control, target, *argv):
        self.addOp("CU", self.qubitsToList([control, target]))
        operator = super().CU(control, target, argv)
        self.setOperation(operator)

    def CU3(self, control, target, theta, phi, _lambda):
        self.addOp("CU3", self.qubitsToList([control, target, theta, phi, _lambda]))
        operator = super().CU3(control, target, theta, phi, _lambda)
        self.setOperation(operator)

    def CU2(self, control, target, phi, _lambda):
        self.addOp("CU2", self.qubitsToList([control, target, phi, _lambda]))
        operator = super().CU2(control, target, phi, _lambda)
        self.setOperation(operator)

    def CU1(self, control, target, _lambda):
        self.addOp("CU1", self.qubitsToList([control, target, _lambda]))
        operator = super().CU1(control, target, _lambda)
        self.setOperation(operator)

    # Three qubit gates
    # input parameters: control1, control2, and target
    # .......................................
    def CCX(self, control1, control2, target):
        self.addOp("CCX", self.qubitsToList([control1, control2, target]))
        operator = super().CCX(control1, control2, target)
        self.setOperation(operator)

    def Toffoli(self, control1, control2, target):
        self.CCX(control1, control2, target)

    def SWAP(self, target1, target2):
        self.addOp("SWAP", self.qubitsToList([target1, target2]))
        operator = super().SWAP(target1, target2)
        self.setOperation(operator)

    def Fredkin(self, control, target1, target2):
        self.addOp("Fredkin", self.qubitsToList([control, target1, target2]))
        operator = super().Fredkin(control, target1, target2)
        self.setOperation(operator)

    # adds oracle through Zhegalkin polynomials
    def addOracle(self, oracle):
        targets, input_qubits, truth_table = oracle.get()
        poly = Zhegalkin_Poly()
        for bits in truth_table:
            poly.addTable(bits)
        result = poly.Compute()
        for target, p in enumerate(result):
            for i, value in reversed(list(enumerate(p))):
                if(value==1):
                    blist = [int(i, base=2) for i in bin(i)[2:].zfill(len(input_qubits))]
                    if(bin(i).count("1") == 2):  # use Toffoli gate
                        try:
                            q1 = blist.index(1)
                            q2 = blist[q1+1:].index(1)+q1+1
                            self.CCX(input_qubits[q1], input_qubits[q2], targets[target])
                        except Exception as e:
                            print(e)
                    elif(bin(i).count("1")==1):  # use controlled not gate
                        try:
                            q = blist.index(1)
                            self.CX(input_qubits[q], targets[target])
                        except Exception as e:
                            print(e)
                    elif(i==0):  # use not gate
                        self.X(targets[target])

    # calculate the density matrix
    def DensityMatrix(self):
        density_m = self.getPsi() * self.getPsiAdjoint()
        return density_m

    # purity of state
    def Pure(self):
        density_m = self.DensityMatrix()
        pure = (density_m*density_m).trace()
        return pure

    # choose a state among many others
    def get_shot(self, measured, shots):
        max_set = shots*100
        if not self.getCuda():
            list_all = [int(value * max_set) * [i] for i, value in enumerate(measured)]
        else:
            list_all = [int(value.real * max_set) * [i] for i, value in enumerate(measured)]
        list_all_values = []
        for list_values in list_all:
            list_all_values += list_values
        values = [random.choice(list_all_values) for i in range(shots)]  # choose a state
        return values

    # measure only one qubit
    def Measure_One(self, target, shots=1):
        self.addOp("Measure", self.qubitsToList([target]))
        density_m = self.DensityMatrix()
        list = self.getOrdListSimpleGate(target, super().P0())
        P0 = self.kronProduct(list)
        list = self.getOrdListSimpleGate(target, super().P1())
        P1 = self.kronProduct(list)
        measure_0 = (density_m*P0).trace().get()  # expected value for 0
        measure_1 = (density_m*P1).trace().get()  # expected value for 1
        value = self.get_shot([measure_0, measure_1], shots)  # measure values without averaging
        if(value[0] == 0):
            new_state = self.product(P0, self.getPsi())/sqrt(measure_0)  # collapse of the state after the measure
        else:
            new_state = self.product(P1, self.getPsi())/sqrt(measure_1)  # collapse of the state after the measure
        self.setPsi(new_state)
        return value

    # measure a list of qubits
    def Measure(self, target, fisrt_msb = False):  # ex: measure 3 qubits of 5: 2,1,4 of state "010" -> M010 = |1><1| x |0><0| x 1 x |0><0| x 1
        target = self.qubitsToList(target)
        if(fisrt_msb):  # if fisrt_msb=True -> the first on the list will be the most significant
            target.reverse()
        self.setMeasuredQubits(target)
        self.addOp("Measure", target)
        density_m = self.DensityMatrix()
        size_p = len(target)  # number of qubits to be measured
        size = 2 ** size_p  # number of possible states
        result = []
        for i in range(size):
            tlist = [self.ID() for tl in range(self.getNumberOfQubits())]
            blist = [i >> bl & 0x1 for bl in range(size_p)]  # bit list, bits de cada i
            for j, value in enumerate(target):
                if blist[j] == 0:  # most significant first
                    tlist[value-1] = super().P0()
                else:
                    tlist[value-1] = super().P1()
            if not self.isFirstLeft():
                tlist.reverse()
            M = self.kronProduct(tlist)
            measure = (density_m * M).get().trace()  # expected value
            if self.getCuda() and cupy_is_available:
                measure = measure.get().item().real
            result.append(measure)
        self.setMeasuredValues(result)
        return result

    # plot state probability distribution
    def Plot(self, big_endian=False):
        size_p = len(self.getMeasuredQubits())  # number of bits measured
        if(size_p > 0):
            size = 2 ** size_p
            if(big_endian):
                names = ["|" + ''.join(list(reversed("{0:b}".format(i).zfill(size_p)))) + ">" for i in range(size)]
            else:
                names = ["|" + "{0:b}".format(i).zfill(size_p) + ">" for i in range(size)]
            values = self.getMeasuredValues()
            #plt.figure(figsize = (5, 3))
            plt.bar(names, values)
            plt.xticks(rotation=50)
            plt.suptitle('')
            plt.show()
        else:
            print("No qubit measured!")

    # plot the density matrix
    def PlotDensityMatrix(self, imaginary=False, decimal=False):
        size_p = self.getNumberOfQubits()  # number of qubits
        mRho = [[0]*2**size_p for i in range(2**size_p)]
        rho = self.DensityMatrix().get()
        for id1 in range(2**size_p):
            for id2 in range(2**size_p):
                if self.getCuda():
                    value = rho[id1][id2]
                    if(not imaginary):
                        value = value.item().real
                    else:
                        value = value.item().imag
                else:
                    value = rho[id1,id2]
                    if(not imaginary):
                        value = sp.re(value)
                    else:
                        value = sp.im(value)
                mRho[id1][id2] = value

        result = np.array(mRho, dtype=float)
        fig = plt.figure(figsize=(5, 5), dpi=150)
        ax1 = fig.add_subplot(111, projection='3d')

        size = 2 ** size_p
        if(not decimal):
            labels = ["|" + "{0:b}".format(i).zfill(size_p) + ">" for i in range(size)]
        else:
            labels = [i for i in range(size)]
        xlabels = np.array(labels)
        xpos = np.arange(xlabels.shape[0])
        ylabels = np.array(labels)
        ypos = np.arange(ylabels.shape[0])

        xpos_mesh, ypos_mesh = np.meshgrid(xpos, ypos, copy=False)

        zpos = result
        zpos = zpos.ravel()

        dx = 0.5
        dy = 0.5
        dz = zpos

        ax1.set_xticks(xpos + dx / 2.)
        ax1.set_xticklabels(xlabels)
        ax1.set_yticks(ypos + dy / 2.)
        ax1.set_yticklabels(ylabels)

        values = np.linspace(0.2, 1., xpos_mesh.ravel().shape[0])
        colors = cm.rainbow(values)
        ax1.bar3d(xpos_mesh.ravel(), ypos_mesh.ravel(), dz * 0, dx, dy, dz, color=colors)
        plt.show()
