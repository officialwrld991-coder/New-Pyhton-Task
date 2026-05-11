user_input = int(input("Enter a number: "))

for number in range(1, user_input):
    if user_input % number == 0:  
        print(number)
    else: continue
