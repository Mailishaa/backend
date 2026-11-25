# a function thet accept any number of arguments and returns the sum # when the arguments are passed python puts them in a tuple
def sum(*numbers):
    total=0
    for number in numbers:
        total+=number
    print(f"the sum of {numbers} is {total}")

sum (1,2,3,4,5,6,7,8,9)
sum(1,2,3,4)
sum()
sum(45,56,78,90)