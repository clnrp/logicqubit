#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp

class Utils:

    @staticmethod
    def onehot(i, value):
        if(i == value):
            return 1
        else:
            return 0

    @staticmethod
    def texfix(value, number, left=False):
        tex = sp.latex(value).replace(' \cdot ', '')
        tex = Utils.textSymbolfix(tex, number, left)
        return tex

    @staticmethod
    def textSymbolfix(value, number, left=False):
        text = value
        for i in range(1, number+1):
            if(left):
                text = text.replace(str(i) + 'a', 'a')
                text = text.replace(str(i) + 'b', 'b')
            else:
                text = text.replace(str(number+1-i) + 'a', 'a')
                text = text.replace(str(number+1-i) + 'b', 'b')
        return text

    @staticmethod
    def vec2tex(vector):
        tex = "\\begin{pmatrix}"+"{:g}".format(vector[0].item()).replace("+0j","")
        for value in vector[1:]:
            tex += ' \\\\ '+"{:g}".format(value.item()).replace("+0j","")
        tex += " \\end{pmatrix}"
        return tex

    @staticmethod
    def BinList(n):
        blist = []
        for i in iter(range(2 ** n)):
            b = bin(i)[2:].zfill(n)  # value in binary, ex: i=1, n=4 -> '0001'
            blist.append(b)
        return Utils.Text2List(blist)

    @staticmethod
    def Text2List(table):
        list = [int(i, base=2) for i in table]
        size = len(table[0])
        tmp = sorted(list, key=int, reverse=False)  # values in ascending order
        result = [[int(bin(j)[2:].zfill(size)[i]) for i in range(size)] for j in tmp]
        return result