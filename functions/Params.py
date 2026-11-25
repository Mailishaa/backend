# multiple paremeters
def calculate_total(price,quantity,discount):
    
    total = price*quantity
    if discount > 0:
        total-=discount
    print(f"the total price is {total}")
    
price= int(input("Enter the price: "))
quantity= int (input("Enter the quantity: "))
discount = int (input("Enter the discount: "))


calculate_total(price, quantity, discount)









    