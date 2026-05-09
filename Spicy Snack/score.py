#1. collect three scores from terminal
#2. add it together and divide buy three to get average
#3. set score to condition if it is A, B, C, D, or F


score_one = int(input("Enter your score: "))
score_two = int(input("Enter your score: "))
score_three = int(input("Enter your score: "))

average = (score_one + score_two + score_three) / 3

if average >= 90 and average <= 100:
    print("A")
elif average >= 80 and average < 90:
    print("B")
elif average >= 70 and average < 80:
    print("C")
elif average >= 60 and average < 70:
    print("D")
else:
    print("F")
