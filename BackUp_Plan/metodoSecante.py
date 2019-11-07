from funciones import *
import sys
import pandas as pd
f = f(raw_input("Please enter the function f to use: "))
x0 = float(raw_input("Please enter the starting value of x: "))
x1 = float(raw_input("Please enter a continuous value for x: "))
tolerancia = float(raw_input("Please enter the value of the maximum tolerance: "))
niter = int(raw_input("Please enter the maximum number of iterations: "))
fx0 = evalfunct(f,x0)
xList = []
fxList = []
eAbList = []
eRList = []
if fx0 == 0:
    print(x0, " its a root")
else:
    fx1 = evalfunct(f,x1)
    contador = 0
    eAb = tolerancia + 1
    eR = eAb/x0
    den = fx1 - fx0
    while eAb > tolerancia and fx1 != 0 and contador < niter:
        xList.append(x0)
        fxList.append(fx0)
        x2 = x1 - fx1*(x1-x0)/den
        eAb = abs(x2-x1)
        eR = eAb/x2
        eAbList.append(eAb)
        eRList.append(eR)
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = evalfunct(f,x1)
        den = fx1 - fx0
        contador = contador + 1
        pandas = {'Xn':xList,'fx':fxList,'Absolute Error':eAbList,'Relative Error':eRList}
    print(pd.DataFrame(data=pandas))
    if fx1 == 0:
        print(x1," its a root")
    elif eAb < tolerancia:
        print(x1, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a absolute error of: ", eAb)
    elif eR < tolerancia:
        print(x1, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a relative error of: ", eR)
    elif den == 0:
        print("Its possible that a multiple root exist")
    else:
        print("Failed with ", niter, " iterations")

