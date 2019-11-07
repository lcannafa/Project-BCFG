from funciones import *
import sys
import pandas as pd
f = f(raw_input("Please enter the function to use: "))
xi = float(raw_input("Please enter the value of the limit inferior of the interval: "))
xs = float(raw_input("Please enter the value of the limit superior of the interval: "))
tolerancia = float(raw_input("Please enter the value of the maximum tolerance: "))
niter = int(raw_input("Please enter the maximum number of iterations: "))
fxi = evalfunct(f,xi)
fxs = evalfunct(f,xs)
xiList = []
xsList = []
xmList = []
fxmList = []
eAbList = []
eRList = []
if fxi == 0:
    print(xi," its a root")
elif fxs == 0:
    print(xs, " its a root")
elif (fxi*fxs) < 0:
    xm = xi - (fxi*(xs-xi))/(fxs-fxi)
    fxm = evalfunct(f,xm)
    contador = 1
    eAb = 1
    eR = 1
    while eAb > tolerancia and fxm != 0 and contador < niter:
        xiList.append(xi)
        xsList.append(xs)
        xmList.append(xm)
        fxmList.append(fxm)
        if (fxi*fxm) < 0:
            xs = xm
            fxs = fxm
        else:
            xi = xm
            fxi = fxm
        xaux = xm
        xm = xi - (fxi*(xs-xi))/(fxs-fxi)
        fxm = evalfunct(f,xm)
        eAb = abs(xm - xaux)
        eR = eAb/xm
        eAbList.append(eAb)
        eRList.append(eR)
        contador = contador + 1
        pandas = {'Xinf':xiList,'Xsup':xsList,'Xm':xmList,'f(xm)':fxmList,'Absolute Error':eAbList,'Relative Error':eRList}
    print(pd.DataFrame(data=pandas))
    if fxm == 0:
        print(xm, " its a root")
    elif eAb < tolerancia:
        print(xm, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a absolute error of: ", eAb)
    elif eR < tolerancia:
        print(xm, "its a aproximation of a root with a tolerance of: ", tolerancia, " and a relative error of: ", eR)
    else:
        print("Failed with ", niter, " iterations")
else:
    print("This interval is inadequate")        