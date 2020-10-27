from sympy import symbols
from sympy import sin, cos, exp

def  ch(angle):
    alpha = symbols("alpha")
    alpha = (exp(angle) + exp(-angle)) / 2
    return alpha

def  sh(angle):
    alpha = symbols("alpha")
    alpha = (exp(angle) - exp(-angle)) / 2
    return alpha   

ro, sigma, x, y = symbols("ro sigma x y")

ro_val = float(input("ro : "))
sigma_val = float(input("sigma : "))
a_val = float(input("a : "))

x = (a * sh(ro)) / (ch(ro) - cos(sigma))
y = (a * sin(ro)) / (ch(ro) - cos(sigma))

x = x.subs([(ro, ro_val), (sigma, sigma_val), (a, a_val)])
y = y.subs([(ro, ro_val), (sigma, sigma_val), (a, a_val)])

print("x = ", x)
print("y = ", y)