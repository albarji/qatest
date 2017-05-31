"""
calc.py

Implements a very simple calculator
"""
import math

def sum(a, b):
    return a + b # Superarreglado!!

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        raise ValueError
    return a / b

def exp(a, b):
    return math.pow(a, b)

def fibonacci(i):
    if i < 0:
        raise ValueError
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i == 2:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)
