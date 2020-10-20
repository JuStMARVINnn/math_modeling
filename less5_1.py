import math
import sympy

x, y = sympy.symbols("x y")
expr = x + 2*y

print(sympy.sin(x**2) - sympy.exp(-2*x) + sympy.cos(sympy.pi / x))