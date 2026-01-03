print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

price = 0

if size == "S":
    price +=15
elif size == "M":
    price +=20
elif size == "L":
    price +=25
else:
    print("You have entered an invalid size.")
    

if pepperoni == "Y" and size == "S":
    price += 2
elif pepperoni == "Y":
    price += 3

if extra_cheese == "Y":
    price += 1

print(f"Your final bill is: ${price}.")


