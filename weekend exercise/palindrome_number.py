numbers = input("Enter a number: ")
backward = ""
for number in numbers:
    backward = number + backward
if numbers == backward:
    print("It is a palindrome")
else: print("It is not a palindrome") 

