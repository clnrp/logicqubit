#!/usr/bin/python
# -*- coding: UTF-8 -*-

from logicqubit.logic import *

def iqft(logicQuBit, n): # transformada quântica de Fourier inversa
    for i in range(1,n+1):
        for j in range(1,i+1):
            logicQuBit.CU1(j, i, -pi/float(2**(i-j)))
        logicQuBit.H(i)

logicQuBit  = LogicQuBit(5)

n = 4
phase = 11.0*pi/8.0

logicQuBit.H(1)
logicQuBit.H(2)
logicQuBit.H(3)
logicQuBit.H(4)

logicQuBit.X(5)
logicQuBit.CU1(4, 5, 1*phase) # cU^1
logicQuBit.CU1(3, 5, 2*phase) # cU^2
logicQuBit.CU1(2, 5, 4*phase) # cU^4
logicQuBit.CU1(1, 5, 8*phase) # cU^8

iqft(logicQuBit, n)

logicQuBit.Measure([1,2,3,4])
logicQuBit.Plot()