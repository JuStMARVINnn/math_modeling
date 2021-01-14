import numpy as np
import tkinter as tk
import random

class Ball:
    def __init__(self, window, obj, canvas, x, y, Vx, Vy):
        self.window = window
        self.object = obj
        self.canvas = canvas
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        
    def GetTrajectory(self, time):
        t = np.arange(0, time, 0.01)
        
        x = self.x + self.Vx*t
        y = self.y + self.Vy*t - 9.8 * t**2 / x
        
        return x, y
        
    def Move(self, counter):
        if counter < len(self.counter[0]):
            self.canvas.move(self.object, 
                             self.GetTrajectory()[0][counter],
                             self.GetTrajectory()[1][counter])
            self.window.after(10, lambda: self.Move(counter+1))
            


window = tk.Tk()

canvas = tk.Canvas()
window.geometry(f'{1500}x{1500}')
canvas.configure(bg='black')
canvas.pack(fill='both', expand=True)

balls = []
for i in range(0, random.randint(3, 10)):
    x = random.randint(0, 400)
    y = random.randint(0, 400)
    radius = random.randint(0, 200)
    ball = canvas.create_oval(x-radius,
                              y-radius,
                              x+radius,
                              y+radius,
                              fill='blue')
    balls.append(Ball(window, ball, canvas, x, y, random.randint(10, 30), random.randint(10, 30)))
    
for i in balls:
    i.Move(0)
