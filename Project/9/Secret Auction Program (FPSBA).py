# Prints the logo of Secret Bidding from the file art.py
from art import logo
print(logo)


print("Welcome to the SECRET AUCTION PROGRAM!!")

# Empty Dictionary to store the Name of the Bidder & their Amount
Bidders={}

# While loop to execute the Secret Bidding process till the user desires to do so
yes_or_no=False
while not yes_or_no:
    Name = input("What is your name?: ")
    Bid = int(input("What's your bid?: $ "))
    print("Thank you for Participating.")

    # Asks if the user wants to bid anymore or not
    Question = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if Question == "yes":
        print("\n" * 100,)
    else:
        yes_or_no = True
        print("The Bid is Over. Thank you for Participating.")
    Bidders[Name] = Bid                

# Prints the Dictionary 
print("\n",Bidders)

print("Highest Bid is:",Bidders[max(Bidders,key=Bidders.get)] , "\nThe winner is:",max(Bidders,key=Bidders.get), "and their bidding amount is:$",Bidders[max(Bidders,key=Bidders.get)])
