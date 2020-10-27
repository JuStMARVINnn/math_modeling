import sympy
from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality

x = symbols("x")

expr = sympy.Abs(x**2 + 2*x -3) + 3*(x + 1)
solve = reduce_abs_inequality(expr, "<", x)

print(solve)