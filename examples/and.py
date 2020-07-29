#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit = LogicQuBit(3)

logicQuBit.H(1)
logicQuBit.PrintLastOperator()

logicQuBit.H(2)

logicQuBit.CCX(1,2,3)

logicQuBit.Measure([3])
logicQuBit.Plot()