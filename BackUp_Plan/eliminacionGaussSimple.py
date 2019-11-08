import numpy as np
from funciones import *
import sys
#matrix = str(raw_input("Please enter the coefficient matrix of the system: "))
#vector = str(raw_input("Please enter the independent terms of the system: "))
matrix = '2.0 -3.0 4.0 1.0;-4.0 2.0 1.0 -2.0;1.0 3.0 -5.0 3.0;-3.0 -1.0 1.0 -1.0'
vector = '10.0 -10.0 32.0 -21.0'
a = np.matrix(matrix)
b = np.matrix(vector)
b = b.T
s = np.hstack(((a,b)))
n = len(s) 
print(n)
for k in range (0,(n-1)):
    for i in range ((k+1),n):
        multiplicador = s[i,k]/s[k,k]
        print('m ', multiplicador)
        for j in range (k,(n+1)):
            s[i,j] -= multiplicador*s[k,j]
a = s[:,:-1]
b = s[:,min(len(s),len(s.T))]
print(s)
print(a)
print(b)
#print(regresiva(a,b))