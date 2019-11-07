from funciones import *
import sys
import pandas as pd
f = f(raw_input("Please enter the function f to use: "))
x0 = float(raw_input("Please enter the starting value of x: "))
tolerancia = float(raw_input("Please enter the value of the maximum tolerance: "))
niter = int(raw_input("Please enter the maximum number of iterations: "))
fx = evalfunct(f,x0)
dfx = evalfunct(f1(f),x0)
x0List = []
fxList = []
dfxList = []
eAbList = []
eRList = []
contador = 0
eAb = tolerancia + 1
eR = eAb/x0
while eAb > tolerancia and fx != 0 and dfx != 0 and contador < niter:
    x1 = x0 - (fx/dfx)
    fx = evalfunct(f,x1)
    dfx = evalfunct(f1(f),x1)
    eAb = abs(x1 - x0)
    eR = eAb/x1
    x0 = x1
    contador = contador + 1
    pandas = {'Xn':x0List,'fx':fxList,'dfx':dfxList,'Absolute Error':eAbList,'Relative Error':eRList}
print(pd.DataFrame(data=pandas))
if fx == 0:
    print(x0," its a root")
elif eAb < tolerancia:
    print(x1, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a absolute error of: ", eAb)
elif eR < tolerancia:
    print(x1, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a relative error of: ", eR)
elif dfx == 0:
    print("its possible that ", x1, "is a multiple root")
else:
    print("Failed with ", niter, " iterations")