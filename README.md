
### Features

- Numerical and symbolic simulation of quantum algorithms
- Plot states and current operation, density matrix and measurement graphs
- The state values can be represented as angles, which helps in the analysis of the fourrier quantum transform.
- Operations can be performed directly on the instantiated qubit object or using qubit indices.
- Support GPU


**Table of Contents**

[TOC]

#Installation

pip install logicqubit

#Startup

logicQuBit  = LogicQuBit(n_qubits, symbolic = True)

Where n_qubits is the number of qubits, and symbolic defines whether the values a and b of the qubits will be symbolic or not, if the symbolic input is omitted the calculation will be numeric.

##To instantiate a qubit

q  = Qubit()

##To instantiate a qubit register

reg = QubitRegister(num_qubits)

#Operations

##Operations on one qubit

The operation can be performed as q.Gate(parameters) or logicQuBit.Gate(id_qubit, parameters).

##Operations on two qubits

In this case, the operation can be performed as q.Gate(control_qubit, parameters) or logicQuBit.Gate(control_qubit, target qubit, parameters).

*The need for parameters depends on the type of gate.

## List of available gates

Single-qubit gates: X, Y, Z, V, S, T, H, RX, RY, RZ, U, U1, U2, U3.
Two-qubits gates: CX or CNOT, CY, CZ, CV, CS, CT, CRX, CRY, CRZ, CU, CU1, CU2, CU3, SWAP.
Three-qubits gates: CCX or Toffoli, Fredkin.

#Code sample


	from logicqubit.logic import *

	logicQuBit  = LogicQuBit(3)

	a = Qubit()
	b = Qubit()
	c = Qubit()

	a.H()
	b.H()

	c.CCX(a,b) # and operation

