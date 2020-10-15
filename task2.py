import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def solver(h, t):
    dhdt = - (mu * (2 * g * h)**0.5 * np.pi * d**2 * H) / (6 * h**2 * D)
    return dhdt

mu = 0.62
g = 9.8
H = 0.11
d = 0.003
D = 0.08

t = np.arange(0, 100, 0.01)
h_0 = H

solve = odeint(solver, h_0, t)
plt.plot(t, solve[:, 0])

plt.show()