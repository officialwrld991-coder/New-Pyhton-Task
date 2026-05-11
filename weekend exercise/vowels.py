name = input("Enter a name: ")
count = 0
vowels = "aeiou"
for letters in name:
    if letters == vowels:
        count += 1
print(count)
