#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

import sympy as sp
from sympy.physics.quantum import TensorProduct

class Utils:

    @staticmethod
    def onehot(i, value):
        if(i == value):
            return 1
        else:
            return 0

    @staticmethod
    def texfix(value, number):
        tex = sp.latex(value).replace(' \cdot ', '')
        for i in range(1, number+1):
            tex = tex.replace(str(i) + 'a', 'a')
            tex = tex.replace(str(i) + 'b', 'b')
        return tex