print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

'''
small pizza (S)= $15
medium pizza (M) = $20
large pizza (L) = $25
Add pepperoni for small pizza (Y or N) : $2
Add pepperoni for medium or large pizza (Y or N): +$3
Add extra cheese for any size pizza (Y or N): +1
'''
small_pizza = 15
medium_pizza = 20
large_pizza = 25
price = 0

if size == "S":
    price = small_pizza
elif size == "M":
   price = medium_pizza
else:
   price = large_pizza

# add pepperoni or not

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

# add extra cheese or not

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: {price}")