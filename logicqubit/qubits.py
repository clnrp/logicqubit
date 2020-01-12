#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

from sympy import *
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum import tensor_product_simp
from sympy.physics.quantum import Dagger

class Qubits:
    def __init__(self, num = 3):
        self.num = num

class QubitRegister:
    def __init__(self, num = 3):
        self.num = num