import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(bg="green")
canvas.create_line(15, 25, 200, 25, dash=(4, 2))
canvas.pack()

window.mainloop()