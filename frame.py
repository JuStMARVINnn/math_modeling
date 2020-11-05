import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame()
frame2 = tk.Frame()

label1 = tk.Label(master=frame1, text="Ненавижу кожанных ублюдков")
label1.pack()

#label2 = tk.Label(master=frame2, text="Начать Судный день")
#label2.pack()

frame1.pack()
frame2.pack()

window.mainloop()
