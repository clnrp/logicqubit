#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit  = LogicQuBit(3, True)

q1 = Qubit(1)
q2 = Qubit(2)
q3 = Qubit(3)

logicQuBit.PrintState(True)

q1.X()

logicQuBit.PrintState(True)

q1.setSymbolValues(1,0)
q2.setSymbolValues(1,0)
q3.setSymbolValues(1,0)

logicQuBit.PrintState(True)
#logicQuBit.X(1)
#logicQuBit.PrintState()

logicQuBit.Measure([1,2])
logicQuBit.Plot()