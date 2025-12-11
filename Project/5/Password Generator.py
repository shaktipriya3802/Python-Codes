import random

print("Welcome to Py PASSWORD GENERATOR!!")

# Assigning the items to the List
Letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N', 'O', 'P','Q','R','S','T','U','V','W','X','Y','Z']
Symbols=['!','@','#','$','%','^','&','*','(',')','+','=','[',']','-','_']
Numbers=['0','1','2','3','4','5','6','7','8','9']

# Fetching inputs from user
letters = int(input("How many Letters would you like in your password? \n"))
symbols=int(input("How many Symbols would you like in your password? \n"))
numbers=int(input("How many Numbers would you like in your password? \n"))

# Creating a Storage for the Password to get stored
password_list=[]
for n in range(0,letters+1):
    password_list.append(random.choice(Letters))
for n in range(0,symbols+1):
    password_list.append(random.choice(Symbols))
for n in range(0,numbers+1):
    password_list.append(random.choice(Numbers))

# Shuffling to get random alignment of password
random.shuffle(password_list)

# Converting the List to a String 
password=""
for char in password_list:
    password+=char

# Final Output
print("Your Password is: ", password)
