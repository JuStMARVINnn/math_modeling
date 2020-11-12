import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(bg="green")
canvas.create_oval(10, 10, 80, 80, 
                   outline="#f11",
                   fill="red",
                   width=5)
canvas.create_arc(10, 10, 80, 80,
                  outline="#f11",
                  fill="red", 
                  width=5)
canvas.create_rectangle(150, 150, 180, 180,
                        outline="#f11",
                        fill="red",
                        width=5)
points = [150, 123, 241, 160, 108, 325, 212, 63]
canvas.create_polygon(points, width=5)

canvas.pack()
window.mainloop()