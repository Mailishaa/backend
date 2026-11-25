def year_of_birth(name,age):
    year= 2026-age
    print(f"{name} was born in {year}")
year_of_birth("Alice",22) # positional arguments- based on the position of the parameter
year_of_birth(name ="Jane ",age = 21)# Key word Arguments- name of the parameter is specified the position does not have to be explicit
year_of_birth(age =22 ,name = "Jane")# the oredr does not matter 