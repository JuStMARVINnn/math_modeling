import sympy
import numpy as np
from sympy import symbols
from sympy.vector import CoordSys3D

N = CoordSys3D("N")
a, b, c = symbols("a b c")

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
c = -5*N.i - 6*N.j + 12*N.k

modA = a.dot(a)
modB = b.dot(b)
modC = c.dot(c)

ab = sympy.acos(a.dot(b) / (modA * modB))
ac = sympy.acos(a.dot(c) / (modA * modC))
bc = sympy.acos(b.dot(c) / (modB * modC))

print("a^b : ", ab.evalf() * 180 / np.pi)
print("a^c : ", ac.evalf() * 180 / np.pi)
print("b^c : ", bc.evalf() * 180 / np.pi)
