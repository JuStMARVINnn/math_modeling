import tkinter as tk

X = 10
Y = 50
vx = 0.5
vy = 0.5

def move(obj, x, y, vx, vy):
    x_new = x + vx
    y_new = y + vy
    if x_new > 13 or y_new > 40:
        x_new = 10
        y_new = 50
    canvas.move(obj, x_new, y_new)
    return x_new, y_new

def spawn(x, y, _canvas, R=5):
    obj = _canvas.create_oval(x, y, x+R, y+R, 
                              outline="black",
                              fill="black",
                              width=2)
    return obj

def update():
    global X
    global Y
    X, Y = move(circle, X, Y, vx, vy)
    window.after(100, update)

window = tk.Tk()

canvas = tk.Canvas()
circle = spawn(vx, vy, canvas)
canvas.after_idle(update)

canvas.pack()
window.mainloop()
    