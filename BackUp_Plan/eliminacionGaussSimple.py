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
print(n)
for k in range (0,(n-1)):
    for i in range ((k+1),n):
        multiplicador = s[i,k]/s[k,k]
        for j in range (k,(n+1)):
            s[i,j] -= multiplicador*s[k,j]
a = s[:,:-1]
b = s[:,min(len(s),len(s.T))]
print(s)
print(a)
print(b)
print(regresiva(a,b))