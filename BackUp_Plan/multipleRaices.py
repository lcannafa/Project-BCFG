from funciones import *
import sys
import pandas as pd
f = f(raw_input("Please enter the function f to use: "))
x0 = float(raw_input("Please enter the starting value of x: "))
tolerancia = float(raw_input("Please enter the value of the maximum tolerance: "))
niter = int(raw_input("Please enter the maximum number of iterations: "))
fx = evalfunct(f,x0)
dfx = evalfunct(f1(f),x0)
d2fx = evalfunct(f2(f),x0)
contador = contador + 1
eAb = tolerancia + 1
eR = eAb/x0
while eAb > tolerancia and fx != 0 and dfx != 0 and contador < niter:
    x1 = x0 - (fx*dfx)/((dfx**2)-(fx*d2fx))
    fx = evalfunct(f,x1)
    dfx = evalfunct(f1(f),x1)
    d2fx = evalfunct(f2(f),x1)
    eAb = abs(x1 - x0)
    eR = eAb/x1
    x0 = x1
    contador = contador + 1
if fx == 0:
    print(x1, " its a root")
elif eAb < tolerancia:
    print(x1, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a absolute error of: ", eAb)
elif eR < tolerancia:
    print(x1, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a relative error of: ", eR)
elif dfx == 0:
    print(x1," has more than one root")
elif d2fx == 0:
    print(x1, "has more than two roots")
else:
    print("Failed with ", niter, " iterations")