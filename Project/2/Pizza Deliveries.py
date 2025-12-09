print("Welcome to McD Pizza Deliveries")
size = input("Enter the Size you want S or L or M: ").upper()
bill=0
extra_pep=0
extra_cheese=0
if size=="S":
    print("The Small Pizza costs 15$")
    bill=15
elif size=="M":
    print("The Medium Pizza costs 20$")
    bill = 20
elif size=="L":
    print("The Large Pizza costs 25$")
    bill = 25
else:
    print("Please enter the size correctly")

pepperoni=input("Do you want Extra Pepperoni? Type Y for Yes and N for No: ").upper()
if pepperoni=="Y" and size=="S":
    print("It costs 2$")
    extra_pep=2
elif pepperoni=="Y" and size=="M" or size=="L":
    print("It costs 3$")
    extra_pep=3
elif pepperoni=="N":
    print("You have selected No for Extra Pepperoni")
    extra_pep=0
else:
    print("Please Enter the Option correctly")

cheese=input("Do you want Extra Cheese? Type Y for Yes and N for No: ").upper()
if cheese=="Y":
    print("The extra cheese costs 1$")
    extra_cheese=1
elif cheese=="N":
    print("You have selected No for Extra Cheese")
    extra_cheese=0
else:
    print("Please Enter the Option correctly")

Total_Bill = bill + extra_pep + extra_cheese
print("", size, " size Pizza costs", bill, "$", "\n Extra Pepperoni costs ", extra_pep, "$", "\n Extra Cheese costs ", extra_cheese, "$")
print("And Your Total Bill is: ", Total_Bill, "$")