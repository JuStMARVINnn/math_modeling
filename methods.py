import numpy as np

class Ball:
    mass = 0   # Статические атрибуты класса
    radius = 0
    color = None
    
    # Методы экземпляры класса
    def __init__(self, end_time):
        self.time = np.arange(0, end_time, 0.01)    # Динамические атрибуты экземпляра
        
    def Move(self, vx, vy):
        self.x = vx * self.time
        self.y = vy * self.time
        
        # print(f"Coords : ({self.x}, {self.y})")
        
    # Статический метод
    @staticmethod
    def Helper(img):
        if img == "hex":
            color = "red"
        else:
            color = "blue"
        
        print(color)
        
    # Метод класса
    @classmethod
    def toy_ball(cls, end_time):
        toy_ball = cls(end_time)
        return toy_ball
        
    
ball = Ball(15)
ball.Move(1, 1)

Ball.Helper("lol_kek_cheburek")

toy = Ball.toy_ball(15)
print(type(toy))