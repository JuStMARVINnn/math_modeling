class Ball:
    def __init__(self):
        self.name = "Oval"    # public
        self._radius = 50    # private
        self.__color = "red"    # protected
        
    def func(self):    # public method
        print("self.name")
        
    def _SetRdius(self, newRadius):    # private method
        self._radius = newRadius
    
    def __SetColor(self, newColor):    # protected method
        self.__color = newColor
        
        
        
ball = Ball()
# print(ball._radius) # можно, но не надо
# print(ball.__color) # Error
# print(ball._Ball__color) # Pizdec


# ball._SetRdius(1) # можно, но очень не надо
# ball._Ball__SetColor("blue") # Again Pizdec
