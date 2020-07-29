#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit = LogicQuBit(2, symbolic=False)

a = Qubit()
b = Qubit()

a.H()
a.PrintLastOperator()
b.CNOT(a)

#logicQuBit.H(a)
#logicQuBit.CNOT(a,b)

print(a.getName())
print(b.getName())

logicQuBit.setSymbolValuesForAll(1,0)

print(logicQuBit.DensityMatrix())
print(logicQuBit.Pure())

logicQuBit.PlotDensityMatrix()

logicQuBit.Measure([a, b])
logicQuBit.PrintOperations()
logicQuBit.Plot()