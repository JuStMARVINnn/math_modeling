import sympy
from sympy import symbols
from sympy.vector import CoordSys3D

N = CoordSys3D("N")
x, y, z = symbols("x y z")

q1 = 1
q2 = -0.5

E1 = (((q1 * x) / (sympy.sqrt((x**2 + y**2 + z**2)**3))) * N.i +
     ((q1 * y) / (sympy.sqrt((x**2 + y**2 + z**2)**3))) * N.j + 
     ((q1 * z) / (sympy.sqrt((x**2 + y**2 + z**2)**3))) * N.k)
     
E2 = (((q1 * (x - 1)) / (sympy.sqrt(((x - 1)**2 + (y - 1)**2 + (z - 1)**2)**3))) * N.i +
     ((q1 * (y - 1)) / (sympy.sqrt(((x - 1)**2 + (y - 1)**2 + (z - 1)**2)**3))) * N.j +
     ((q1 * (z - 1)) / (sympy.sqrt(((x - 1)**2 + (y - 1)**2 + (z - 1)**2)**3))) * N.k)

rawResult = E1 + E2
result = rawResult.subs([(x, 3), (y, 4), (z, 5)])
result = result.evalf();
print(result)

mod = result.dot(result)
print(mod)

