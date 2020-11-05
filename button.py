import tkinter as tk

window = tk.Tk()

btn1 = tk.Button(
        text="Press me!",
        width=25,
        height=5,
        bg="blue",
        fg="white"
)
btn2 = tk.Button(
        text="Press me!",
        width=25,
        height=5,
        bg="yellow",
        fg="red"
)

btn1.pack()
btn2.pack()

window.mainloop()