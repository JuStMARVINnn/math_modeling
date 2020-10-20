from sympy import symbols
from sympy import sin, cos, exp, pi
from sympy import Eq, solve, solveset, linsolve, nonlinsolve

x, y, z = symbols("x y z")

expr = sin(x**2) - exp(-2*x) + cos(pi / x)

#sExpr = solve(expr, x) # решает expr относительно x
                       # если корней нет - Runtime Error

eqExpr = Eq(x, y) # приравнивает x к у и/или проверяет на тождество

ssExpr = solveset(expr, x) # == solve(), но solve() хрень

lSystem = [x + y + z - 1, x + y + 2*z - 3, x - 2*y + z]
lsSystem = linsolve(lSystem, (x, y, z)) # решает линейную систему system относительно переменных в списке

nlSystem = [x**2 - 2*y**2, x*y - 2]
nlsSystem = nonlinsolve(nlSystem, [x, y]) # решает нелинейную систему system относительно переменных в списке

print(nlsSystem)