class Car:
    def __init__(self,make,color,model):
        self.make= make
        self.model= model
        self.color=color
    def description(self):
        return f"{self.color} {self.make} {self.model}"
    def accelerate(self):
        return f"{self.description} is accelerating"
    def turn(self):
        return f"{self.description()}is turning"
class ElectricCar(Car): # inherits from car # should have a constructor similar to the parent constructor
    def __init__(self,make,color,model):
        super().__init__(make,color,model)
        self.battery_range="100 kilometers"
    def charge(self):
        return f"{self.description()} is charging"




