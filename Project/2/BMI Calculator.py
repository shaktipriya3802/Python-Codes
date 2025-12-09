weight=float(input("Enter your Weight in Kgs: "))
height=float(input("Enter your Height in cms: "))

bmi = float(weight / (height ** 2))

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
    print("You are Underweight, \n try to gain some weight!")
elif 18.5<=bmi<25:
    print("Congratulations, You have a Normal Weight")
else:

    print("You are Overweight, \n try to lose some weight!")

