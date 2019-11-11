import numpy as np
from funciones import *
import sys
#strx = str(raw_input("Please enter the vector of x: "))
#strfx = str(raw_input("Please enter the vector of Fx: "))
#strval = str(raw_input("Please enter the value to interpolate"))
strx = '2 2.2 2.4 2.6 2.8'
x = np.fromstring(strx, dtype=float, sep=' ')
strfx = '-4.6109 -4.1749 -3.3768 -2.1362 -0.3553'
fx = np.fromstring(strfx, dtype=float, sep=' ')
strval = '2.5'
val = float(strval)
n = len(x)
a = []
for i in range(n):
    a.append(fx[i])
for j in range(1, n):
    for i in range(n-1, j-1, -1):
        a[i] = (a[i]-a[i-1])/(x[i]-x[i-j])
a = np.array(a)
n = len( a ) - 1
temp = a[n] + (val - x[n])
for i in range( n - 1, -1, -1 ):
    temp = temp * ( val - x[i] ) + a[i]
result = temp
print(a)
print(result)