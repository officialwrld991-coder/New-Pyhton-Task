passed = 0
fail = 0
for _ in range(15):
    score = int(input("Enter your score: "))
    if score < 45:
        fail += 1
    if score >= 45:
        passed += 1
        
print("Number of Students that passed is:  ", passed)
print("Number of Students that failed is:  ", fail)
        
    
