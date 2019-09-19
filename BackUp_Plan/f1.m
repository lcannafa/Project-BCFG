function y = f1(x)
%y = - sin(2*x + 3) - 2*x*cos(2*x + 3) - 2*x*exp(1 - x^2) - 4;
%y = 49/(4*x^(2/3)) - 7/x^(1/3) + 1
y = (4*x^3)/(x^4 + 3) - 7*exp(4 - x^2)*sin(7*x - 8) - 2*x*exp(4 - x^2)*cos(7*x - 8) - 1
end