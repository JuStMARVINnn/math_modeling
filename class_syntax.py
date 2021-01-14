class Ball:
    color = 'red'
    
    def __init__(self, x, y, Vx, Vy):
        print('constructor called!')
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
    
    def Move(self, t):
        self.x = self.x + self.Vx*t
        self.y = self.y + self.Vy*t
    
    def SetCoord(self, x, y):
        self.x = x
        self.y = y
    def GetCoord(self):
        print(self.x, self.y)
        
    def SetColor(self, color):
        Ball.color = color
        
        
ball1 = Ball(0, 0, 1, 1)
ball2 = Ball(2, 3, 7, 6)
print(type(ball1))

ball2.Move(6)
print(ball2.GetCoord())

print(ball2.color)

ball1.SetColor('blue')
print(ball1.color)
print(ball2.color)

