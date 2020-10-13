import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax = plt.axes(xlim=(-25, 25), ylim=(-25, 25))
star, = ax.plot([], [])
    
t = np.arange(0, 4*np.pi, 0.01)
x = 12 * np.cos(t) + 8 * np.cos(1.5*t)
y = 12 * np.sin(t) - 8 * np.sin(1.5*t)

def update(i):
    alpha = 0.1 * i

    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = y * np.cos(alpha) + x * np.sin(alpha)

    star.set_data(X, Y)
    return star,

anim = FuncAnimation(fig, update, frames=100, interval=20, blit=True)
anim.save("task4_1.gif")