import tkinter as tk

def Convert():
    if degrees.get() == 1:
        raw = float(entry.get())
        val = str(raw + 273.15) + "°C"
        label["text"] = "{}".format(val)
    else:
        raw = float(entry.get())
        val = str(raw - 273.15) + "°K"
        label["text"] = "{}".format(val)

window = tk.Tk()
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

degrees = tk.IntVar()
degrees.set(0)

entry = tk.Entry(master=window,
                 fg="green",
                 bg="black",
                 width=10)
radioButtonsFrame = tk.Frame(master=window)
button = tk.Button(master=window,
                   text="Convert",
                   width=7,
                   height=3,
                   fg="blue",
                   command=Convert)
label = tk.Label(master=window, text="0")

radioButton1 = tk.Radiobutton(master=radioButtonsFrame, text="°K", variable=degrees, value=1)
radioButton2 = tk.Radiobutton(master=radioButtonsFrame, text="°C", variable=degrees, value=2)

entry.grid(row=0, column=0, sticky="nsew")
radioButtonsFrame.grid(row=0, column=1)
radioButton1.pack()
radioButton2.pack()
button.grid(row=0, column=2)
label.grid(row=0, column=3)
window.mainloop()