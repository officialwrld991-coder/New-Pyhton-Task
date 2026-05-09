#1. collect password from terminal
#2. condition the password to check if it strong, medium or weak


password = input("Enter  your password: ")
password = len(password)


if password > 1 and password < 6:
    print("Weak")
elif password >= 6 and password <= 10:
    print("Medium")
elif password > 10:
    print("Strong")
elif password <= 1:
    print("Invalid")

