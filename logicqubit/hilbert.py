#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

from .utils import *

class Hilbert():

    def __init__(self):
        self.d = 1

    def ket(self, value, d = 2):
        return Matrix([[self.onehot(i, value)] for i in range(d)])

    def bra(self, value, d = 2):
        return Matrix([self.onehot(i, value) for i in range(d)])