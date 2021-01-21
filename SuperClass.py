import numpy as np

class SuperClass:
    def __init__(self, color, end_time):
     self.color = color
     self.time = np.arange(0, end_time, 0.01)
     
     def Move(self, vx, vy):
         self.x = vx * self.time
         self.y = vy * self.time
         

class SubClass(SuperClass):
    def __init__(self, aerodymanics, color):
        super().__init__(color, 10)
        self.aerodynamics = aerodymanics
        
    def Fly(self):
        if self.aerodynamics == "circle":
            print("Flyable")
        else:
            print("Non flyable")
            
            
            
ball = SubClass("Oval", "Green")
ball.Fly()
ball.Move(3, 5)