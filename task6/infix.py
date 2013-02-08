#!/usr/bin/python

def func1(a, b):
    return a + b

def func2(a, b):
    return a * b

def func3(a, b):
    return a ** b

def getOpDict():
    dictOp = {}
    dictOp["op1"] = func1
    dictOp["op2"] = func2
    dictOp["op3"] = func3
    return dictOp
