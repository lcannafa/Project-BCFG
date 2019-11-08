import math as m
import numpy as np
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
def regresiva(a,b):
    n = len(b)
    x = [0 for i in range(n)]
    x[n-1] = b[n-1,0]/a[n-1,n-1]
    for i in reversed(range(0,n-1)):
        suma = 0
        for j in range((i+1),n):
            suma = suma + a[i,j]*x[j]
        x[i] = (b[i,0] - suma)/a[i,i]
    return x