import numpy as np
import matplotlib.pyplot as plt

def Lissagu(time, a, b, A, B):
    delta = np.pi / 2
    
    t = np.arange(0, time, 0.001)
    
    x = A * np.sin(a * t + delta)
    y = B * np.sin(b * t)
    
    plt.plot(x, y)
    plt.savefig("fig1.png")
    
Lissagu(12*np.pi, 1, 2, 1, 7)