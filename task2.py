from sympy import symbols
from sympy import sqrt
from sympy import simplify, factor

a = symbols("a")

expr = ((sqrt(a) - a / (sqrt(a) + 1)) * (a - 1) / sqrt(a))
simp = simplify(expr)
fact = factor(expr)
print(simp)
print(fact)
