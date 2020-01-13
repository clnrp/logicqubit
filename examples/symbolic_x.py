#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit  = LogicQuBit(3, True)

logicQuBit.PrintTex()
#logicQuBit.X(1)
#logicQuBit.PrintTex()

logicQuBit.Measure([1,2])
logicQuBit.Print()