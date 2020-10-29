import sympy
import numpy as np
from sympy import symbols
from sympy.vector import CoordSys3D

def CheckVector(v1, v2):
    modV1 = v1.dot(v1)
    modV2 = v2.dot(v2)
    angle = sympy.acos(v1.dot(v2) / (modV1 * modV2))
    
    if angle.evalf() == (90 * np.pi / 180):
        return True
    else:
        return False
    

N = CoordSys3D("N")
a, b, c = symbols("a b c")

a = 7*N.i + 2*N.j - 8*N.k
b = -4*N.i + 50*N.j + 9*N.k

print(CheckVector(a, b))
