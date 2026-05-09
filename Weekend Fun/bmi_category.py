weight = int(input("Enter weight: "))
height = int(input("Enter height: "))

bmi = weight / (height * height)


if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal")
elif bmi >= 25 and bmi <= 29.9:
    print("OverWeight")
elif bmi >= 30:
    print("Obese")

