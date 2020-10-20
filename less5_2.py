from sympy import symbols, sin, cos, exp, pi

x, y, z = symbols("x y z")

expr = x**3 + 4*x*y - z
expr_new = expr.subs([(x, 2), (y , 4), (z, 0)]) # подставить значения
expr_nums = expr.evalf() # приведение к числам


