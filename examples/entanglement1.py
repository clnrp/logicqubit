#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit  = LogicQuBit(3)

a = Qubit(1)
b = Qubit(3)

logicQuBit.H(a)
logicQuBit.CNOT(a,b)

print(a)
print(logicQuBit.DensityMatrix())
print(logicQuBit.Pure())

logicQuBit.Measure([a,b])
logicQuBit.Plot()