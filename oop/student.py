class Student:
   # name= "Lydia"
    #age = 20
    #country= "Rwanda"
    school = "Akirachix"
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country
    def introduce(self):
        print(f"I am{self.name}.I am {self.age} years old. my country is {self.country}. I am a student of{self.school}")
        