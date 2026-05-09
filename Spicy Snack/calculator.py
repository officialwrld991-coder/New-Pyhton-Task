#1. collect two numbers from terminal
#2. collect operator to use from user
#3. deliver output based from operator given


number_one = int(input("Enter  Number: "))
operator = input("Enter Opetaror: ")
number_two = int(input("Enter Number: "))



if operator == "+":
    sum = number_one + number_two
    print(sum)
elif operator == "-":
    minus = number_one - number_two
    print(minus)
elif operator == "*":
    multiply = number_one * number_two
    print(multiply)
elif operator == "/":
    divide = number_one / number_two
    print(divide)

