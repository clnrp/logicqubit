#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *
from logicqubit.zhegalkin import *

# H|x1,x2>|00>
# x1 x2 y1 y2
# 0  0  1  1
# 0  1  0  0
# 1  0  1  1
# 1  1  1  0

# 1 x 00, 1 x 10, 2 x 11

poly = Zhegalkin_Poly()
poly.addTable(['00', '10', '11'])
poly.addTable(['00', '10'])
poly.Compute()
poly.ShowPolynomial()


logicQuBit = LogicQuBit(5)

x1 = Qubit()
x2 = Qubit()

y1 = Qubit()
y2 = Qubit()

x1.H()
x2.H()

# pol = x1^0x2^0 + x1^0x2^1 + x1^1x2^0 + x1^1x2^1, onde x1^0x2^0 = 1

# p/ y1
#p00+p10+p11 = (1,1,0,1)
#y1.CCX(x1, x2)
#y1.CX(x2)
#y1.X()

# p/ y2
#p00+p10 = (1,1,0,0)
#y2.CX(x2)
#y2.X()

oracle = Oracle([x1, x2])
oracle.addTable(y1, ['00', '10', '11'])
oracle.addTable(y2, ['00', '10'])
logicQuBit.addOracle(oracle)

res = logicQuBit.Measure([y1, y2], True)

logicQuBit.Plot()