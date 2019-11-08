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
def progresiva(a,b):
    n = len(b)
    x = [0 for i in range(n)]
    x[0] = b[0,0]/a[0,0]
    for i in range(1,n):
        suma = 0
        for j in range(0,(i-1)):
            suma = suma + a[i,j]*x[j]
        x[i] = (b[i,0] - suma)/a[i,i]
    return x
def intercambioFila(a,fi1,fi2):
    f = np.copy(a)
    f[fi1,:] = a[fi2,:]
    f[fi2,:] = a[fi1,:]
    return f
def intercambioColumna(a,c1,c2):
    f = np.copy(a)
    f[:,c1] = a[:,c2]
    f[:,c2] = a[:,c1]
    return f
def pivoteoParcial(a,b,k):
    s = np.hstack(((a,b)))
    n = len(a) - 1
    mayor = abs(k)
    filaMayor = k
    for t in range(k,n):
        if abs(s[t,k]) > mayor:
            mayor = abs(s[t,k])
            filaMayor = t
    if mayor == 0:
        print("The system doesnt have a unique solution")
    elif filaMayor != k :
        s = intercambioFila(s,filaMayor,k)
    return s
def pivoteoTotal(a,b,k):
    s = np.hstack(((a,b)))
    n = len(a) - 1
    mayor = 0
    filaMayor = k
    columnaMayor = k
    for r in range(k,n):
        for t in range(k,n):
            if(abs(s[r,t]) >  mayor):
                mayor = abs(s[r,t])
                filaMayor = r
                columnaMayor = t
    if mayor == 0:
        print("The system doesnt have a unique solution")
    elif filaMayor != k:
        s = intercambioFila(s,filaMayor,k)
    elif columnaMayor != k:
        s = intercambioColumna(s,columnaMayor,k)
        print("The columns ", columnaMayor, " and ", k, " were swaped")
