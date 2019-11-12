import numpy as np
from funciones import *
import sys
from scipy import interpolate
from scipy.interpolate import CubicSpline

strx = '0 1 2 3 4 5'
x_points = np.fromstring(strx, dtype=float, sep=' ')
strfx = '12 14 22 39 58 77'
y_points = np.fromstring(strfx, dtype=float, sep=' ')
strval = '1.25'
val = float(strval)
#x_points = [ 0, 1, 2, 3, 4, 5]
#y_points = [12,14,22,39,58,77]
tck = interpolate.splrep(x_points, y_points)
a = interpolate.splev(val, tck)
print(a)
cs = CubicSpline(x_points,y_points,bc_type='natural')
print(cs(val))