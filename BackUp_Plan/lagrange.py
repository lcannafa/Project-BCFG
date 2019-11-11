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
strval = '2.45'
val = float(strval)
n = len(x)
l = [0.0 for i in range(n)]
acum = 0.0
valorfx = 0
for i in range(n):
    prod = 1.0
    for j in range(n):
        if(j != i):
            prod *= (val - x[j])/(x[i] - x[j])
    l[i] = prod
    valorfx = (l[i]*fx[i]) 
    acum += (l[i]*fx[i])
    print ("L",i," f(x",i,"): ",l[i]," ", valorfx)
print("acum: ", acum)
