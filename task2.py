class Tomato:
    states = {0 : "None", 1 : "Blooms", 2 : "Green", 3 : "Red"}
    
    def __init__(self, index):
        self.index = index
        self.state = 0
    
    def grow(self):
        self.state += 1
        if self.state >= 3:
            self.state = 3
    
    def isRipe(self):
        if self.state == 3:
            return True
        else:
            return False
        

class TomatoBush:
    def __init__(self, tomatoes):
        self.tomatoes = []
        for i in range(tomatoes):
            self.tomatoes.append(Tomato(i))
    
    def grow_all(self):
        for i in self.tomatoes:
            i.grow()
        
    def all_are_ripe(self):
        for i in self.tomatoes:
            if i.isRipe() == False:
                return False
        return True
    
    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    def __init__(self, name, bush):
        self.name = name
        self.bush = bush
        
    def work(self):
        self.bush.grow_all()
        
    def harvest(self):
        if self.bush.all_are_ripe() == True:
            self.bush.give_away_all()
            print("Помидорки созрели и были собраны")
            return True
        else:
            print("Вы очень плохой садовник, ваш кут вас не любит, работайте лучше.")
            return False
            
    def knowledge_base(self):
        print("Садовник очень не любит работать. Но ему приходится окучивать куст помидорок")
        print("Метод .work() заставляет его работать")
        print("Успехи садовника можно узнать в методе .harvest()")
            
        
bush = TomatoBush(3)
gard = Gardener("Евгений", bush)
gard.knowledge_base()

while True:
    if gard.harvest() == True:
        break
    else:
        gard.work()
