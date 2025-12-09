weight = 85
height = 1.85

bmi = float(weight / (height ** 2))

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
    print("You are Underweight, \n try to gain some weight!")
elif 18.5<=bmi<25:
    print("Congratulations, You have a Normal Weight")
else:
    print("You are Overweight, \n try to lose some weight!")