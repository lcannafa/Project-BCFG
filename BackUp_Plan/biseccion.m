function biseccion(xi, xs, tolerancia, niter)
fxi = f(xi)
fxs = f(xs)
if(fxi == 0)
    disp(xi + " es raiz")
elseif(fxs == 0)
    disp(xs + " es raiz")
elseif((fxi*fxs) < 0)
    xm = (xi + xs)/2
    fxm = f(xm)
    contador = 1
    error = tolerancia + 1
    while(error > tolerancia & fxm ~= 0 & contador < niter)
        if((fxi*fxm) < 0)
            xs = xm
            fxs = fxm
        else
            xi = xm
            fx1 = fxm
        end
        aux = xm
        xm = (xi + xs)/2
        fxm = f(xm)
        error = abs(xm - aux) %Error depende del que te pida pacho
        contador = contador + 1
        vcount(contador) = contador
        verror(contador) = error
        vxi(contador) = xi
        vxs(contador) = xs
        vxm(contador) = xm
        vfxi(contador) = fxi
        vfxs(contador) = fxs
        vfxm(contador) = fxm
        assignin('base','contador',vcount)
        assignin('base','xi',vxi)
        assignin('base','xs',vxs)
        assignin('base','xm',vxm)
        assignin('base','error', verror)
        assignin('base','fxi',vfxi)
        assignin('base','fxs',vfxs)
        assignin('base','fxm',vfxm)
    end
    if(fxm == 0)
        disp(xm + " es raiz")
    elseif(error < tolerancia)
        disp(xm + " es aproximación a una raiz con una tolerancia de: " + tolerancia)
    else
        disp("Fracasó en " + niter + (" iteraciones"))
    end
else
    disp("El intervalo es inadecuado")
end
end
