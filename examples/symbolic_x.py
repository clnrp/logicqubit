#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit = LogicQuBit(2, symbolic=True, first_left=False)
#logicQuBit = LogicQuBit(3)

q1 = Qubit()
q2 = Qubit()
#q3 = Qubit()

logicQuBit.PrintState(True)

q1.X()

logicQuBit.PrintState(True)

q1.setSymbolValues(1, 0)
q2.setSymbolValues(1, 0)
#q3.setSymbolValues(1, 0)

logicQuBit.PrintState(True)

logicQuBit.Measure([q1, q2])
logicQuBit.Plot()