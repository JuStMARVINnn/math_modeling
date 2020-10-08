import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 100

fig, ax = plt.subplots()
ax = plt.axes(xlim=(-0.2, 0.4), ylim=(-0, 0.8))
point, = ax.plot([], [], 'o')

x, y = [], []
def GetPoints(n, x0=0.1, y0=0.1):
    x.append(x0)
    y.append(y0)
    
    C = 0.3
    D = 0.33
    
    for i in range(n):
        x_last = x[-1]
        y_last = y[-1]
        x.append(x_last**2 - y_last**2 + C)
        y.append(2 * x_last * y_last + D)

xdata, ydata = [], []
def update(i):    
    xdata.append(x[i])
    ydata.append(y[i])
    point.set_data(xdata, ydata)
    return point,

GetPoints(N)
plt.title("5")
anim = FuncAnimation(fig, update, frames=N, interval=100, blit=True)
anim.save("task5.gif")
    