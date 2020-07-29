#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *
from logicqubit.oracle import *

logicQuBit = LogicQuBit(8)

x1 = Qubit()
x2 = Qubit()
x3 = Qubit()

y1 = Qubit()
y2 = Qubit()

x1.H()
x2.H()
x3.H()

oracle = Oracle([x1, x2, x3])
oracle.addTable(y1, ['000', '001', '010', '011'])
oracle.addTable(y2, ['000', '001', '010', '100'])

logicQuBit.addOracle(oracle)

res = logicQuBit.Measure([y1, y2], True)
logicQuBit.PrintOperations()

logicQuBit.Plot()