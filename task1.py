import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def solver(h, t, mu):
    dhdt = - (4 * s * mu * (2 * g * h)**0.5)  / (np.pi * D**2)
    return dhdt

mu_1 = 0.97
g = 9.8
s = 0.0002
D = 0.2

t = np.arange(0, 50, 1)
h_0 = 0.5

solve = odeint(solver, h_0, t)
plt.plot(t, solve[:, 0], "g")

plt.show()