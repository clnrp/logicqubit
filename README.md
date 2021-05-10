# Features

- Numerical and symbolic simulation of quantum algorithms
- Plot state and current operation, density matrix and measurement graphs
- The state values can be represented as angles, which helps in the analysis of the fourrier quantum transform.
- Operations can be performed directly on the instantiated qubit object or using qubit indices.
- Support GPU

# Table of Contents
- [Installation](#installation)
- [Startup](#startup)
  * [To instantiate a qubit](#to-instantiate-a-qubit)
  * [To instantiate a qubit register](#to-instantiate-a-qubit-register)
- [Operations](#operations)
  * [Operations on one qubit](#operations-on-one-qubit)
  * [Operations on two qubits](#operations-on-two-qubits)
  * [List of available gates](#list-of-available-gates)
- [Measure](#Measure)
  * [Measure the expected value of one or more qubits](#Measure-the-expected-value-of-one-or-more-qubits)
  * [Measure one shot on a qubit](#Measure-one-shot-on-a-qubit)
- [Plot graphs and print state](#Plot-graphs-and-print-state)
  * [Plot expected values](#Plot-expected-values)
  * [Plot the density matrix](#Plot-the-density-matrix)
  * [Print the current state](#Print-the-current-state)
  * [Print the current state as angles](#Print-the-current-state-as-angles)
- [Code sample](#code-sample)
- [Other code samples](#other-code-samples)

# Installation

pip install logicqubit

# Startup

logicQuBit  = LogicQuBit(n_qubits, symbolic = True)

Where n_qubits is the number of qubits, and symbolic defines whether the values a and b of the qubits will be symbolic or not, if the symbolic input is omitted the calculation will be numeric.

## To instantiate a qubit

q  = Qubit()

## To instantiate a qubit register

reg = QubitRegister(num_qubits)

# Operations

## Operations on one qubit

The operation can be performed as q.Gate(parameters) or logicQuBit.Gate(id_qubit, parameters).

## Operations on two qubits

In this case, the operation can be performed as q.Gate(control_qubit, parameters) or logicQuBit.Gate(control_qubit, target_qubit, parameters).

*The need for parameters depends on the type of gate.


## List of available gates

Single-qubit gates: X, Y, Z, V, S, T, H, RX, RY, RZ, U, U1, U2, U3.

Two-qubits gates: CX or CNOT, CY, CZ, CV, CS, CT, CRX, CRY, CRZ, CU, CU1, CU2, CU3, SWAP.

Three-qubits gates: CCX or Toffoli, Fredkin.

# Measure

## Measure the expected value of one or more qubits

result = logicQuBit.Measure([q1,q2,..,qn])

## Measure one shot on a qubit

value = logicQuBit.Measure_One(qubit)

# Plot graphs and print state

## Plot expected values

logicQuBit.plot()

Generate a graph of the values obtained by the Measure([...]).

## Plot the density matrix

logicQuBit.PlotDensityMatrix()

## Print the current state

logicQuBit.PrintState()

## Print the current state as angles

logicQuBit.getPsiAtAngles(degree=True)

The degree variable defines whether the result will be displayed in degrees or radians.

# Code sample

```python
from logicqubit.logic import *

logicQuBit  = LogicQuBit(3)

a = Qubit()
b = Qubit()
c = Qubit()

a.H()
b.H()

c.CCX(a,b) # and operation

logicQuBit.Measure([c])
logicQuBit.Plot()
```
![](https://github.com/clnrp/logicqubit/blob/master/images/1620579394.png)

# Other code samples

https://github.com/clnrp/logicqubit-algorithms

