number_one = int(input("Enter first Number: "))
number_two = int(input("Enter  second Number: "))
number_three = int(input("Enter third Number: "))

largest = number_one 

if number_two > largest:
    largest = number_two
if number_three > largest:
    largest = number_three
    
print(largest)
