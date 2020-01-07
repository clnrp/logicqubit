#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

logicQuBit  = LogicQuBit(2)

logicQuBit.H(1)
logicQuBit.X(2)
logicQuBit.H(2) # |00> -|01> + |10> -|11>

logicQuBit.CX(1,2) # |00> -|01> - |10> +|11>

logicQuBit.H(1)
logicQuBit.H(2)

logicQuBit.Measure([1,2])
logicQuBit.Plot()