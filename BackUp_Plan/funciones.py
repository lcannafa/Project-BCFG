def f(f):
    x = sym.Symbol("x")
    return f
def g(g):
    x = sym.Symbol("x")
    return g
def f1(f):
    x = sym.Symbol("x")
    f1 = sym.diff(f)
    return f1
def f2(f1):
    x = sym.Symbol("x")
    f2 = sym.diff(f1)
    return f2


import sys
import sympy as sym
x = sym.Symbol("x")
f = f(sys.argv[1])
g = g(sys.argv[2])
print(f)
f1 = f1(f)
print(f1)
f2 = f2(f1)
print(f2)
print(g)