import numpy as np
import matplotlib.pyplot as plt

def func(e=0.8, p=3):
    phi = np.arange(0, 2 * np.pi, 0.001)    
    r = p / (1 + e * np.cos(phi))
    
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    
    plt.axis("equal")
    plt.plot(x, y)
    plt.savefig("fig2.png")
    
func()