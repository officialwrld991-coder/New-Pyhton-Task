user_input = int(input("Enter a number: "))
count = 0
for number in range(1, user_input):
    if user_input % number == 0:  
        count += 1
    else: continue
print(count)
