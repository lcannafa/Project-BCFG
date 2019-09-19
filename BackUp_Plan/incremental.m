function incremental(x0, delta, niter)
fx0 = f(x0)
if(fx0 == 0)
    disp(x0 + " es raiz")
else
    x1 = x0 + delta
    contador = 1
    fx1 = f(x1)
    while((fx0*fx1) > 0 & contador < niter)
        x0 = x1
        fx0 = fx1
        x1 = x0 + delta
        fx1 = f(x1)
        contador = contador + 1
        vcount(contador) = contador
        vx0(contador) = x0
        vx1(contador) = x1
        vfx0(contador) = fx0
        vfx1(contador) = fx1
        assignin('base','contador',vcount)
        assignin('base','x0',vx0)
        assignin('base','x1',vx1)
        assignin('base','fx0',vfx0)
        assignin('base','fx1',vfx1)
    end
    if(fx1 == 0)
        disp(x1 + " es raiz")
    elseif((fx0*fx1) < 0)
        disp("Hay una raiz entre " + x0 + " y " + x1)
    else
        disp("Fracasó en " + niter + " iteraciones")
    end
end   