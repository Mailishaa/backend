class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        pass # means  the behavour cannot be implemented because the animal is not known yet therefor we implemenet polymorphism
class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        return "wooff"
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def make_sound(self):
        return "meow"

    
        
    
   
