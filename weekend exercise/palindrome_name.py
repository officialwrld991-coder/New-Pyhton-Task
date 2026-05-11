name = input("Enter a name: ")
backward = ""
for letters in name:
    backward = letters + backward
print(backward) 
if backward == name:
    print("Yes, It is a palindrome")
else: print("No, It is not a palindrome") 

