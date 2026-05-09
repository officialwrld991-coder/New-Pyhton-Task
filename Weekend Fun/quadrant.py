number_one = int(input("Enter your First Number: "))
number_two = int(input("Enter your Second Number: "))


if number_one > 0 and number_two > 0:
    print("Q1")
elif number_one < 0 and number_two > 0:
    print("Q2")
elif number_one < 0 and number_two < 0:
    print("Q3")
elif number_one > 0 and number_two < 0:
    print("Q4")
elif number_one = 0 and number_two = 0:
    print("Origin")
elif number_one == 0 and number_two != 0:
    print("X-axis")
elif number_one != 0 and number_two == 0:
    print("Y-axis")



