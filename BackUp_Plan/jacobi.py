import numpy as np
from funciones import *
import sys
#matrix = str(raw_input("Please enter the coefficient matrix of the system: "))
#vector = str(raw_input("Please enter the independent terms of the system: "))
#x0vector = str(raw_input("Please enter the starting values of x: "))
#tolerancia = float(raw_input("Please enter the value of the maximum tolerance: "))
#niter = int(raw_input("Please enter the maximum number of iterations: "))
matrix = '9 2 -3;-3 -3 8;3 2 -7'
vector = '27 -61 -21'
x0vector = '2 4 5'
a = np.matrix(matrix).astype(float)
b = np.matrix(vector).astype(float)
x0 = np.matrix(x0vector).astype(float)
n = len(np.hstack(((a,b.T))))
tol = 5e-6
niter = 20
cont = 0
dispersion = tol + 1
x1 = np.zeros(n)
while dispersion > tol and cont < niter :
    #x1 = calcularNuevoJacobi(a,b,x0)
    dispersion = abs(x1-x0)
    x = x1
    cont = cont + 1
if dispersion < tol:
    print("This is a aproximation with a tolerance of" + str(tol))
    print(x1)
else:
    print("Failed at "+str(niter)+" iterations")