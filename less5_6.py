# Векторы

import sympy
from sympy import symbols
from sympy.vector import CoordSys3D

N = CoordSys3D("N")
x, y, z = symbols("x y z")
a, b, c = symbols("a b c")

v1 = N.i - 2*N.j

v2 = 2*N.i + 3*N.j - N.k
v3 = N.i - 4*N.j + N.k
solve = v2.dot(v3)

v4 = (a*b + a*c + b**2 + b*c)*N.i + N.j
solve = v4.factor()

v5 = (sympy.sin(a)**2 + sympy.cos(a)**2)*N.i + (2 * sympy.cos(b)**2 - 1) * N.k
solve = sympy.trigsimp(v5)

print(solve)
