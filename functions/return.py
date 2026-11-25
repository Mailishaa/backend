def add(a,b):
    answer= a+b
    return answer                         # the results are returned but not printed in the terminal
answer= add (4,5) 
print(f" 4 plus 5 is {answer}")  #  4 plus 5 is 9     # the purppose is to re assign the value
#if it was print it would be  4 plus 5 is None this is because the value has nor been re assigned 

def my_func (**kwargs):
        print(kwargs)
my_func(name="Python", version=3.12)

def build_cars(brand,model,*,electric=false,**extra_features):
      print(f"car:{brand}{model} (electric:{electric})")
      print(f"extras:{extra_features}")
build_cars("Tesla","Model3",electric=True, autopilot=True,color="red") 

def year_of_birth (**kwargs):
        year=2026 - age
        print(kwargs)
my_func(name="Python", ag5e=21)
