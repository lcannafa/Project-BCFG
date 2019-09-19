function y = f2(x)
%y = 4*x^2*exp(- x^2 - 1) - 2*exp(- x^2 - 1) - 4*cos(2*x + 3) + 4*x*sin(2*x + 3);
%y = 7/(3*x^(4/3)) - 49/(6*x^(5/3))
y = (12*x^2)/(x^4 + 3) - (16*x^6)/(x^4 + 3)^2 - 51*exp(4 - x^2)*cos(7*x - 8) + 28*x*exp(4 - x^2)*sin(7*x - 8) + 4*x^2*exp(4 - x^2)*cos(7*x - 8)
end