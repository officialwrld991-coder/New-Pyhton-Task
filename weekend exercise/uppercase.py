name = input("Enter a name: ")
count = 0
for letters in name:
    if letters == letters.upper():
        count += 1
print(count)
