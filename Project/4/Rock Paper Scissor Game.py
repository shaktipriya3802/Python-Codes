import random
print("Welcome to Rock Paper Scissor Game Portal!")
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
gameImage=[Rock, Paper, Scissor]
game=["Rock", "Paper", "Scissors"]
User_Choice = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissor \n"))
Computer_Choice = random.randint(0,2)


if User_Choice>=0 and User_Choice<=2:
    print("You Chose: ", game[User_Choice], gameImage[User_Choice])
    print("Computer Chose: ", game[Computer_Choice], gameImage[Computer_Choice])

if User_Choice>=3 or User_Choice<0:
    print("You entered an Invalid Number!")
elif User_Choice==0 and Computer_Choice==2:
    print("You Win!")
elif Computer_Choice==0 and User_Choice==2:
    print("You Lose!")
elif Computer_Choice>User_Choice:
    print("You Lose!")
elif User_Choice>Computer_Choice:
    print("You Win!")
elif User_Choice==Computer_Choice:
    print("Its a Draw!")


