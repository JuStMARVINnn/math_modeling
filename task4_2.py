import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax = plt.axes(xlim=(-20, 20), ylim=(-20, 20))
line, = ax.plot([], [])

xdata, ydata = [], []

def update(i):
    t = 0.1 * i
    
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 *  np.cos(3*t) - np.cos(4*t)
    
    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
    return line,

plt.title("4_2")
anim = FuncAnimation(fig, update, frames=500, interval=20, blit=True)
anim.save("task4_2.gif")