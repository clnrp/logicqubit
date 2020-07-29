#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from logicqubit.utils import *

from IPython.display import display, Math, Latex

# Zhegalkin polynomial
class Zhegalkin_Poly:
    def __init__(self):
        self.truth_table = []
        self.e = []
        self.p = []
        self.e.append(sp.Matrix([[1], [0]]))  # e0 = x+1
        self.e.append(sp.Matrix([[0], [1]]))  # e1 = x
        self.p.append(sp.Matrix([[1], [1]]))  # p0
        self.p.append(sp.Matrix([[0], [1]]))  # p1
        self.elist = []
        self.plist = []
        self.simplified_elist = []
        self.simplified_plist = []

    def kronProduct(self, list): # produto de Kronecker
        A = list[0]
        for M in list[1:]:
            A = TensorProduct(A, M)
        return A

    def addTable(self, table):
        self.truth_table.append(table)

    def SumPoly(self, poly1, poly2):
        poly = [0] * len(poly1)
        for i in range(len(poly)):
            poly[i] = int(poly1[i]) ^ int(poly2[i])  # p_ij * p_kl
        return poly

    def Compute(self):
        for i in range(len(self.truth_table)):
            self.elist.append([])
            self.plist.append([])
            for value in Utils.Text2List(self.truth_table[i]):
                t_elist = []
                t_plist = []
                for j in value:
                    t_elist.append(self.e[j])
                    t_plist.append(self.p[j])
                self.elist[i].append(self.kronProduct(t_elist))
                self.plist[i].append(self.kronProduct(t_plist))

        for i in range(len(self.truth_table)):
            _poly = self.plist[i][0]
            for poly in self.plist[i][1:]:
                _poly = self.SumPoly(_poly, poly)
            self.simplified_plist.append(_poly)
        return self.simplified_plist

    def ShowPolynomial(self, short = True):
        poly = []
        x = ["x_"+str(i+1) for i in range(len(self.truth_table[0][0]))]
        size_p = len(x)
        binlist = Utils.BinList(len(x))
        for p in self.simplified_plist:
            terms = ''
            for i in range(2**size_p):  # todos estados possíveis
                if(short):
                    if(p[i]==1):
                        if(len(terms) > 0):
                            terms += "\\oplus "
                        for j in range(len(x)):
                            terms += x[j]+"^"+str(binlist[i][j])
                else:
                    if (i == 0):
                        terms += str(p[i])
                    else:
                        terms += "\\oplus "+str(p[i])
                    for j in range(len(x)):
                        terms += x[j]+"^"+str(binlist[i][j])
            poly.append(terms)
            display(Math(terms))
        #expand = sp.expand((1 + x1) * (1 + x2))