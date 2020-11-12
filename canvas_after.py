import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(bg="green")
circle = canvas.create_oval(10, 10, 30, 30,
                            fill="red")
#canvas.after_idle(move)
button = tk.Button(master=window, text="Press me!", command=move)

canvas.pack()
button.pack()
window.mainloop()

def move():
    x = 10
    y = 10
    canvas.move(circle, x, y)
#    window.after(1000, move)