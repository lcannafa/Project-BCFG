import numpy as np
from funciones import *
import sys
#strx = str(raw_input("Please enter the vector of x: "))
#strfx = str(raw_input("Please enter the vector of Fx: "))
#strval = str(raw_input("Please enter the value to interpolate"))
strx = '4.0 4.1 4.2 4.3 4.4'
x = np.fromstring(strx, dtype=float, sep=' ')
strfx = '-10 15 7 11 32'
fx = np.fromstring(strfx, dtype=float, sep=' ')
strval = '0.1'
val = float(strval)
if (round(x[1]-x[0],2)) != val:
    print("Please enter the real value of h")
else:
    fprimX0 = (1/(12*val))*(-25*fx[0]+48*fx[1]-36*fx[2]+16*fx[3]-3*fx[4])
    print(fprimX0)
