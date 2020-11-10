import tkinter as tk
import random

def Generate():
    val1 = random.randint(1, 6)
    val2 = random.randint(1, 6)
    label1["text"] = "{}".format(val1)
    label2["text"] = "{}".format(val2)
    

window = tk.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

label1 = tk.Label(master=window, text="0")
label2 = tk.Label(master=window, text="0")
button = tk.Button(text="Press me!",
                   width=7,
                   height=3,
                   fg="blue",
                   command=Generate)

label1.grid(row=0, column=0)
label2.grid(row=0, column=2)
button.grid(row=0, column=1)
window.mainloop()