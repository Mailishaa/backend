def greet_student(name="Student"):
    print (f"Hello {name} welcome to the python class")
greet_student()# withouth an argument  it prints  Hello Studentwelcome to the python class
greet_student("Jane") #Hello Jane welcome to the python class

def delivery_fee(location= "Karen"):
    if location=="Karen":
        return 500
    elif location =="Kilimani":
        return 800
    else:
        return 1000
print(delivery_fee())
print(delivery_fee("Kilimani"))
#print(delivery_fee("Westlands"))
