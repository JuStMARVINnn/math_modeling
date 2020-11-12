import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

image = Image.open("image.jpg")
img = ImageTk.PhotoImage(image)
canvas = tk.Canvas(width=image.size[0]+20,
                   height=image.size[1]+20)
canvas.create_image(342, 480, image=img)

canvas.pack()
window.mainloop()