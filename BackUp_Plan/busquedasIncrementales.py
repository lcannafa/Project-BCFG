from funciones import *
import sys
import pandas as pd
f = f(raw_input("Please enter the function to use: "))
x0 = float(raw_input("Please enter the starting value of x: "))
delta = float(raw_input("Please enter the value of delta: "))
niter = int(raw_input("Please enter the maximum number of iterations: "))
fx0 = evalfunct(f,x0)
fxList = []
xList = []
if fx0 == 0:
    print(x0," es raiz")
    sys.exit()
else:
    x1 = x0 + delta
    contador = 1
    fx1 = evalfunct(f,x1)
    while (fx0*fx1) > 0 and contador < niter:
        fxList.append(fx0)
        xList.append(x0)
        x0 = x1
        fx0 = fx1
        x1 = x0 + delta 
        fx1 = evalfunct(f,x1)
        contador = contador + 1
        pandas = {'x':xList,'fx':fxList}
    print(pd.DataFrame(data=pandas))
    if fx1 == 0:
        print(x1, " es raiz")
    elif fx0*fx1 < 0:
        print("Hay una raiz entre ", x0, " y ", x1)
    else:
        print("Fracaso en ", niter, " iteraciones")