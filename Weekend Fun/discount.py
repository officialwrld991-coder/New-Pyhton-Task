total_bill = int(input("Enter your Total Bill: "))
member = input("Are you a member: ")


if total_bill >= 1000 and member =="yes":
    percent = total_bill - (0.1 * total_bill) 
    print(percent)
elif total_bill >= 1000 and member =="no":
    result =  total_bill - (0.5 * total_bill) 
    print(result)
else:
    print("No discount. Your bill is: " , total_bill)


