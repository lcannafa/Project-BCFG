function puntofijo(xa, tolerancia, niter)
fx = f(xa)
contador = 0
error = tolerancia + 1
while(fx ~= 0 & error > tolerancia & contador < niter)
    xn = g(xa)
    fx = f(xn)
    error = abs(xn - xa) %Error depende del que te pida pacho
    xa = xn
    contador = contador + 1
    vcount(contador) = contador
    vxa(contador) = xa
    vxn(contador) = xn
    vfx(contador) = fx
    verror(contador) = error
    assignin('base','contador',vcount)
    assignin('base','xa',vxa)
    assignin('base','xn',vxn)
    assignin('base','error',verror)
    assignin('base','fx',vfx)
end
if(fx == 0)
    disp(xa + " es raiz")
elseif(error < tolerancia)
    disp(xa + " es aproximación con una tolerancia de: " + tolerancia)
else
    disp("El método fracasó en " + niter + " iteraciones")
end
end
    