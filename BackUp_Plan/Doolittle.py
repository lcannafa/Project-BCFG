import numpy as np
from funciones import *
import sys

#matrix = str(raw_input("Please enter the coefficient matrix of the system: "))
#vector = str(raw_input("Please enter the independent terms of the system: "))
matrix = '2 -3 4 1;-4 2 1 -2;1 3 -5 3;-3 -1 1 -1'
vector = '10 -10 32 -21'
a = np.matrix(matrix).astype(float)
b = np.matrix(vector).astype(float)
b = b.T
s = np.hstack(((a,b)))
n = len(s)
L = np.identity(n)
U = np.zeros((n,n))

for k in range(0,n):
    suma1 = 0.0
    for p in range(0,k):
        suma1 += (L[k,p] * U[p,k])
    L[k,k] = 1
    U[k,k] = a[k,k] - suma1
    for i in range (k+1,n):
        suma2 = 0.0
        for p in range (0,k):
            suma2 += (L[i,p] * U[p,k])
        if (L[k,k] != 0):
            L[i,k] = (a[i,k] - suma2)/U[k,k]
        else:
            print("Its possible that the system has no solution")
            break
    for j in range(k+1,n):
        suma3 = 0.0
        for p in range (0,k):
            suma3 += (L[k,p] * U[p,j])
        if(L[k,k] != 0):
            U[k,j] = (a[k,j]-suma3)/L[k,k]
        else:
            print("Its possible that the system has no solution")
            break
    print("L solution")
    print(L)
    print("U solution")
    print(U)
    z = np.matrix(progresiva(L,b)).T
    x = np.matrix(regresiva(U,z)).T
    print("z solution")
    print(z)
    print("x solution")
    print(x)