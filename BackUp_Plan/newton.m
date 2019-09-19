function newton(x0, tolerancia, niter)
fx = f(x0)
f1x = f1(x0)
contador = 0
error = tolerancia + 1
while(error > tolerancia & fx ~= 0 & f1x ~= 0 & contador < niter)
    x1 = x0 -(fx/f1x)
    fx = f(x1)
    f1x = f1(x1)
    error = abs((x1 - x0)/x1) %Error depende del que te pida pacho
    x0 = x1
    contador = contador + 1
    vcount(contador) = contador
    vx0(contador) = x0
    vx1(contador) = x1
    vfx(contador) = fx
    vf1x(contador) = f1x
    verror(contador) = error
    assignin('base','contador',vcount)
    assignin('base','x0',vx0)
    assignin('base','x1',vx1)
    assignin('base','error',verror)
    assignin('base','fx',vfx)
    assignin('base','f1x',vf1x)
end
if(fx == 0)
    disp(x1 + " es raiz")
elseif(error < tolerancia)
    disp(x1 + " es aproximación a una raiz con una tolerancia de: " + tolerancia)
elseif(f1x == 0)
    disp(x1 + " es una posible raiz múltiple")
else
    disp("Fracasó en " + niter + " iteraciones")
end
end