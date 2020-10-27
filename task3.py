from sympy import symbols
from sympy import sin
from sympy import solveset

epsilon, E, M = symbols("epsilon E M")

#expr = E - epsilon * sin(E - M)
expr = E - 0.8 * sin(E - 9)
#expr.subs([(epsilon, 0.8), (M, 9)])

solve = solveset(expr, E)
print(solve)