number = int(input("Enter a number: "))
add = 0

while number > 0:
    rem = number % 10
    if rem % 2 == 0:
        add = add + rem
    number = int(number / 10)
print(add)
