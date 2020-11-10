import tkinter as tk

def Increase():
    val = int(label1["text"])
    label1["text"] = "{}".format(val + 1)
    
def Decrease():
    val = int(label1["text"])
    label1["text"] = "{}".format(val - 1)

window = tk.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

label1 = tk.Label(master=window,
                  text="0")
incButton = tk.Button(text="++",
                      width=50,
                      height=50,
                      fg="blue",
                      command=Increase)
decrButton = tk.Button(text="--",
                      width=50,
                      height=50,
                      fg="blue",
                      command=Decrease)

label1.grid(row=0, column=1)
incButton.grid(row=0, column=0, sticky="nsew")
decrButton.grid(row=0, column=2, sticky="nsew")
window.mainloop()