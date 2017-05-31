"""
Tests for the calc module
"""
import calc

def test_sum():
    assert(calc.sum(2,3) == 5)
    
def test_sub():
    assert(calc.sub(5, 1) == 4)
    
def test_div():
    assert(calc.div(8, 2) == 4)
    
def test_exp():
    assert(calc.exp(2,3) == 8)

def test_fibonacci1():
    assert(calc.fibonacci(1) == 1)

def test_fibonacci2():
    assert(calc.fibonacci(2) == 1)

def test_fibonacci5():
    assert(calc.fibonacci(5) == 5)

