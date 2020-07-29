#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from logicqubit.hilbert import *
from logicqubit.gates import *
from logicqubit.circuit import *
from logicqubit.utils import *
from logicqubit.zhegalkin import *

class Oracle:
    def __init__(self, input_qubits=[], type="truth_table"):
        self.__type = type
        self.__input_qubits = input_qubits
        self.__targets = []
        self.__truth_table = []

    def addInputQubits(self, values):
        self.__input_qubits = values

    def addTargets(self, values):
        self.__targets = values

    def addTable(self, target, values):
        self.__targets.append(target)
        self.__truth_table.append(values)

    def get(self):
        return self.__targets, self.__input_qubits, self.__truth_table
