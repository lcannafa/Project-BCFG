from funciones import *
import sys
import pandas as pd
f = f(raw_input("Please enter the function f to use: "))
g = g(raw_input("Please enter the function g to use: "))
xa = float(raw_input("Please enter the starting value of x: "))
tolerancia = float(raw_input("Please enter the value of the maximum tolerance: "))
niter = int(raw_input("Please enter the maximum number of iterations: "))
fx = evalfunct(f,xa)
xnList = []
fxList = []
eAbList = []
eRList = []
contador = 0
eAb = tolerancia + 1
eR = eAb/xa
while fx != 0 and eAb > tolerancia and contador < niter:
    xn = evalfunct(g,xa)
    fx = evalfunct(f,xn)
    xnList.append(xn)
    fxList.append(fx)
    eAb = abs(xn - xa)
    eR = eAb/xn
    eAbList.append(eAb)
    eRList.append(eR)
    xa = xn
    contador = contador + 1
    pandas = {'Xn':xnList,'fx':fxList,'Absolute Error':eAbList,'Relative Error':eRList}
print(pd.DataFrame(data=pandas))
if fx == 0:
    print(xa, "its a root")
elif eAb < tolerancia:
    print(xa, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a absolute error of: ", eAb)
elif eR < tolerancia:
    print(xa, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a relative error of: ", eR)
else:
    print("Failed with ", niter, " iterations")    