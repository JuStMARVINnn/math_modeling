# tkinter labels
import tkinter as tk

window = tk.Tk()

text = tk.Label(
        text="Hello, World!", # текст
        bg="#5e0a58", # цвет фона
        fg="#71bfcf", # цвет шрифта
        width=20, # ширина в символах
        height=20 # высота в символах
) # создание label
text.pack() # размещение label

window.mainloop()
