function secante(x0,x1,tolerancia,niter)
fx0 = f(x0)
if(fx0 == 0)
    disp(x0 + " es raiz")
else
    fx1 = f(x1)
    contador = 0
    error = tolerancia + 1
    den = fx1 - fx0
    while(error > tolerancia & fx1 ~= 0 & den ~= 0 & contador < niter)
        x2 = x1 - (fx1*(x1-x0))/den
        error = abs(x2-x1) %Error depende del que te pida pacho
        x0 = x1
        fx0 = fx1
        x1 = x2
        fx1 = f(x2)
        den = fx1 - fx0
        contador = contador + 1
        vcount(contador) = contador
        vx0(contador) = x0
        vx1(contador) = x1
        vfx0(contador) = fx0
        vfx1(contador) = fx1
        verror(contador) = error
        assignin('base','contador',vcount)
        assignin('base','x0',vx0)
        assignin('base','x1',vx1)
        assignin('base','error',verror)
        assignin('base','fx',vfx0)
        assignin('base','fx1',vfx1)
    end
    if(fx1 == 0)
        disp(x1 + " es raiz")
    elseif(error < tolerancia)
        disp(x1 + " es aproximación a una raiz con una tolerancia de: " + tolerancia)
    elseif(den == 0)
        disp("Hay una posible raiz multiple")
    else
        disp("Fracasó en " + niter + " iteraciones")
    end
end
end