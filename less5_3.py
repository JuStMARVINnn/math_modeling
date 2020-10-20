from sympy import symbols
from sympy import sin, cos
from sympy import simplify, expand, factor, trigsimp

x, y, z = symbols("x y z")

sExpr = simplify((x**3 + x**2 - x - 1) / (x**2 + 2*x + 1)) # упрощение
eExpr = expand((x + 2) * (x - 3)) # выполнение действий
fExpr = factor(x**3 - x**2 + x- 1) # свернуть в скобки
tExpr = trigsimp(sin(x)**4 - 2*cos(x)**2*sin(x)**2 - cos(x)**4)

#expend() и factor() обратны и обратимы

