import numpy as np
from funciones import *
import sys
#strx = str(raw_input("Please enter the vector of x: "))
#strfx = str(raw_input("Please enter the vector of Fx: "))
#strval = str(raw_input("Please enter the value to interpolate"))
strx = '3.8 3.9 4.0 4.1 4.2'
#sneo = strx[:5]+strx[9:]
x = np.fromstring(strx, dtype=float, sep=' ')
strfx = '-10 15 1 7 11'
#strfxneo = strfx[:5]+strfx[9:]
fx = np.fromstring(strfx, dtype=float, sep=' ')
strval = '0.1'
val = float(strval)
x0 = x[2]
fx0 = fx[2]
x = np.delete(x,2)
fx = np.delete(fx,2)

if (round(x[1]-x[0],2)) != val:
    print("Please enter the real value of h")
else:
    fprimX0 = (fx[0]- 8*fx[1] + 8*fx[2] - fx[3])/(12*val)
    print(fprimX0)
