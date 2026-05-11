name = input("Enter a name: ")
backward = ""
for letters in name:
    backward = letters + backward 
print(backward)
