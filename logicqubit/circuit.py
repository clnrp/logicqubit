#!/usr/bin/python
# encoding: utf-8

# Author Cleoner S. Pietralonga
# e-mail: cleonerp@gmail.com
# Apache License

class Circuit():

    def __init__(self):
        Circuit.operations = []

    def addOp(self, operation, values):
        op = str(operation)+"("+str(values[0])
        for value in values[1:]:
            op+=","+str(value)
        op += ")"
        Circuit.operations.append(op)

    def getOp(self):
        return Circuit.operations

    def PrintOperations(self):
        print(self.operations)