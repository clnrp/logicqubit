#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit  = LogicQuBit(3)

a = Qubit()
b = Qubit()

a.H()
a.PrintLastOperator()
b.CNOT(a)

#logicQuBit.H(a)
#logicQuBit.CNOT(a,b)

print(a.getName())
print(b.getName())

print(logicQuBit.DensityMatrix())
print(logicQuBit.Pure())

logicQuBit.Measure([a,b])
logicQuBit.PrintOperations()
logicQuBit.Plot()