import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=150, height=150, bg="#f33e2c")
frame1.pack() # размещает примитивно по очереди

label1 = tk.Label(master=frame1, text="Ненавижу людей", bg="#f33e2c")
label1.place(x=0, y=0) # размещает по известным координатам

frame2 = tk.Frame(master=window, width=150, height=150, bg="#49c45a")
frame2.pack()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75) # растягивание по сеточке
    window.rowconfigure(i, weight=1, minsize=50) # растягивание по сеточке
    for j in range(3):
        tmpFrame = tk.Frame(master=frame2,
                            relief=tk.RAISED, # выпуклые, tk.SUNKEN - утопленнные
                            borderwidth=1,
                            )
        
        tmpFrame.grid(row=i, column=j) # размещает по сеточке
        tmpLabel = tk.Label(master=tmpFrame,
                            text=f"row {i}, col {j}")
        tmpLabel.pack()
                  
window.mainloop()