
from logicqubit.logic import *
from logicqubit.gates import *
from logicqubit.synthesis import *

A = Matrix([[15, 9, 5, -3],[9, 15, 3, -5],[5, 3, 15, -9],[-3, -5, -9, 15]])*(1/4)
dep = PauliDecomposition(A)
print(dep.get_a())

ket0 = Hilbert.ket(0)
ket1 = Hilbert.ket(1)

ket00 = Hilbert.kronProduct([ket0, ket0])
ket01 = Hilbert.kronProduct([ket0, ket1])
ket10 = Hilbert.kronProduct([ket1, ket0])
ket11 = Hilbert.kronProduct([ket1, ket1])

value = ket11.adjoint() * A * ket11
print(value.get()[0])