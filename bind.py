import tkinter as tk

window = tk.Tk()

button = tk.Button(text="Press me!",
                   width=50,
                   height=50,
                   fg="blue")
button.pack()
button.bind("<Button-1>", OnLeftClick)
button.bind("<Button-3>", OnRightClick)

button.command()

window.mainloop()


def OnLeftClick(event):
    print("Left clicked")
    
def OnRightClick(event):
    print("Right clicked!")