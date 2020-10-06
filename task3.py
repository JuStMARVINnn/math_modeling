import numpy as np
import matplotlib.pyplot as plt

def func(min, max, a, b, x):
    if (a <= min or a >= max or
        b <= min or b >= max):
        return -1
    
    if x < a:
        return a**2
    elif (a <= x and
          x <= b):
        return x**2
    elif x > b:
        return b**2
    
x = np.arange(0, 10 * np.pi, 0.01)
y = np.ndarray(len(x))
min = -3
max = 3
a = 0
b = 2

tmp = 0
for i in x:
    y[tmp] = func(min, max, a, b, i)
    tmp += 1
    
plt.plot(x, y)
plt.savefig("fig3.png")