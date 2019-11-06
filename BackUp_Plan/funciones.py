import math as m
from sympy import *
def f(f):
    x = Symbol("x")
    e = m.e
    pi = m.pi
    f = eval(f)
    return f
def g(g):
    x = Symbol("x")
    e = m.e
    pi = m.pi
    g = eval(g)
    return g
def f1(f):
    x = Symbol("x")
    e = m.e
    pi = m.pi
    f1 = diff(f)
    return f1
def f2(f1):
    x = Symbol("x")
    e = m.e
    pi = m.pi
    f2 = diff(f1)
    return f2
def evalfunct(f,y):
    x = Symbol("x")
    e = m.e
    pi = m.pi
    evalf = f.subs(x,y)
    return evalf