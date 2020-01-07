#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

def iqft(logicQuBit, n): # transformada quântica de Fourier inversa
    for i in range(1,n+1):
        for j in range(1,i+1):
            logicQuBit.CU1(j, i, -pi/float(2**(i-j)))
        logicQuBit.H(i)

logicQuBit  = LogicQuBit(4)

n = 4
phase = 11.0*pi/8.0

logicQuBit.H(1)
logicQuBit.H(2)
logicQuBit.H(3)
logicQuBit.H(4)

logicQuBit.U1(4, 1*phase)
logicQuBit.U1(3, 2*phase)
logicQuBit.U1(2, 4*phase)
logicQuBit.U1(1, 8*phase)

iqft(logicQuBit, n)

logicQuBit.Measure([1,2,3,4])
logicQuBit.Plot()