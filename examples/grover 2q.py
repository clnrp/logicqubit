#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit = LogicQuBit(2)

q_reg = QubitRegister(2)

q_reg.H()

q_reg[1].X()
#q_reg[2].X()
q_reg[2].CZ(q_reg[1])
q_reg[1].X()
#q_reg[2].X()

# Grover 1x
q_reg.H()
q_reg.X()

q_reg[2].H()
q_reg[2].CX(q_reg[1])
q_reg[2].H()

q_reg.X()
q_reg.H()

logicQuBit.Measure(q_reg.getQubits())
logicQuBit.Plot()