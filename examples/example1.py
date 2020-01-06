#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit  = LogicQuBit(3)

logicQuBit.H(1)
logicQuBit.CNOT(1,3)

#print(logicQuBit.DensityMatrix())
#print(logicQuBit.Pure())

logicQuBit.Measure([1,3])
logicQuBit.Plot()