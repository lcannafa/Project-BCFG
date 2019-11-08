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
for i in range (0,max(len(d),len(d.T))):
    print(d[0,i],'pene', i)
l1 = len(d)
l2 = len(d.T)
print('l1 ', l1)
print('l2 ', l2)
aaaa = b[l1-1,0]
bbbb = a[l1-1,l1-1]
c = aaaa/bbbb
print("aaaa ", bbbb)
print("bbbb", aaaa)
print("pene loreno ",c)
print(max(l1,l2))
s = d[:,:-1]
print(s)
g = d[:,min(l1,l2)]
print(g)
print("Guachin",regresiva(a,b))