# НЕРАВЕНСТВА

import sympy
from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities

x, y, z = symbols("x y z")

solve = reduce_abs_inequality(sympy.Abs(x - 5) - 3, "<", x) # неравентва строгие
solve = reduce_rational_inequalities([[y**2 <= 0]], y) # неравентства нестрогие

print(solve)