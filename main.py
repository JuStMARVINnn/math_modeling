from tkinter import *

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()
    
    def build(self):
        self.formula = "0"
        self.label = Label(
          text=self.formula, 
          font=("Times New Roman", 21, "bold"),
          bg="#000", 
          foreground="#FFF"
        )
        self.label.place(x=11, y=11)
        
        buttons = [
          "+", "-", "*", "/", "DEL", "C", "X^2", "=",
          "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"
        ]
        x = 10
        y = 140
        for btn in buttons:
            com = lambda x=btn: self.logicalc(x)
            Button(text=btn, bg="#FFF", font=("Times New Roman", 21, "bold"), command = com).place(x=x, y=y, width=115, height=70)
            x += 117
            if x > 400:
                y += 81
                x = 10    
    
    def logicalc(self, operation):
        if operation == "C":
          self.formula = ""
        elif operation == "DEL":
          self.formula = self.formula[0: -1]
        elif operation == "X^2":
          self.formula = str((eval(self.formula))**2)
        elif operation == "=":
          self.formula = str(eval(self.formula))
        else:
          if self.formula == "":
              self.formula = "0"
          self.formula = operation
        
        self.update()
        
    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.label.configure(text=self.formula)


root = Tk()
root["bg"] = "#000"
root.geometry("485x550+200+200")
root.title("calculator")
root.resizable(False, False)
app = Main(root)
app.pack()
root.mainloop()
