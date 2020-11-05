import tkinter as tk

window = tk.Tk()

entry = tk.Entry(
        fg="green",
        bg="black",
        width=50
)
entry.pack()

text = entry.get() # получение текста в переменную
entry.insert(0, "Ненавижу кожанных мешков, умри") # поместить текст в entry
entry.delete(0, 3) # удаление текста из entry

window.mainloop()
