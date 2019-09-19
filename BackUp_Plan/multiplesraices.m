function multiplesraices(x0, tolerancia, niter)
fx = f(x0)
f1x = f1(x0)
f2x = f2(x0)
contador = 0
error = tolerancia + 1
while(error > tolerancia & fx ~= 0 & f1x ~= 0 & contador < niter)
    %den = (fx*f1x)/((f1x^2)-(fx*f2x))
    x1 = x0 - (fx*f1x)/((f1x^2)-(fx*f2x))
    fx = f(x1)
    f1x = f1(x1)
    f2x = f2(x1)
    error = abs(x1 - x0) %Error depende del que te pida pacho
    x0 = x1
    contador = contador + 1
    vx0(contador) = x0
    vx1(contador) = x1
    vfx(contador) = fx
    vf1x(contador) = f1x
    vf2x(contador) = f2x
    verror(contador) = error
    assignin('base','x0',vx0)
    assignin('base','x1',vx1)
    assignin('base','error',error)
    assignin('base','fx',vfx)
    assignin('base','f1x',vf1x)
    assignin('base','f2x',vf2x)
end
if(fx == 0)
    disp(x1 + " es raiz")
elseif(error < tolerancia)
    disp(x1 + " es aproximación a una raiz con una tolerancia de: " + tolerancia)
elseif(f1x == 0)
    disp(x1 + " tiene más de una raiz")
elseif(f2x == 0)
    disp(x1 + " tiene más de dos raices")
else
    disp("Fracasó en " + niter + " iteraciones")
end
end