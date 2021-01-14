import tkinter as tk
import numpy as np
from scipy.integrate import odeint

def Loop():
    global ball
    if 'ball' in globals():
        canvas.delete(ball)
    ball = SetBall(X, Y)

    # z0 = x0, v_x0, y0, v_y0
    z0 = X, SpeedX, Y, SpeedY
    sol = odeint(Move, z0, t)

    x = sol[:, 0]
    y = sol[:, 2]

    i = 1
    while i < len(t)-1:
        canvas.move(ball, x[i]- x[i-1], y[i]-y[i-1])
        window.update()
        window.after(int(frameTime))
        i += 1


def SetBall(x0, y0, radius=10):
    ball = canvas.create_oval(x0-radius,
                            y0-radius,
                            x0+radius,
                            y0+radius,
                            fill='blue',
                            outline='green',
                            width=2)
    return ball


def Move(z, t):
    x, v_x, y, v_y = z

    dxdt = v_x
    dv_xdt = 0

    dydt = v_y
    dv_ydt = - g

    return dxdt, dv_xdt, dydt, dv_ydt


window = tk.Tk()

canvas = tk.Canvas()
window.geometry(f'{1500}x{1500}')
canvas.configure(bg='black')
canvas.pack(fill='both', expand=True)

g = - 0.1
t = np.arange(0, 100, 0.01)

X = 400
Y = 250
SpeedX = 1
SpeedY = - 1

fps = 25
frameTime = 1 / fps

tk.Button(window, text='Start', command=Loop).pack()
Loop()

window.mainloop()
