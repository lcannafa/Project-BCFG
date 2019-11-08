import numpy as np
from funciones import *
import sys
#matrix = str(raw_input('mete la matriz guachin '))
#vector = str(raw_input('mete el vector guachin '))
#b = np.array([1,2,3])
matrix = '2 -3 4 1;-4 2 1 -2;1 3 -5 3;-3 -1 1 -1'
vector = '10 -10 32 -21'
b = np.matrix(vector)
print(b)
b = b.T
print(b)
print('saep', b[3,0])
a = np.matrix(matrix)
print(a)
d = np.hstack((a,b))
print(d)
f = intercambioFila(d,3,1)
print(f)
g = intercambioColumna(f,3,1)
print(g)