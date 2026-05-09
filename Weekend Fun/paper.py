player_one = input("Player One: Enter rock, paper or scissors: ")
player_two = input("Player Two: Enter rock, paper or scissors: ")

if player_one == "rock" and player_two == "paper":
    print("Player Two Wins")
elif player_one == "paper" and player_two == "paper":
    print("Tie")    
elif player_one == "scissors" and player_two == "paper":
    print("Player One Wins")
elif player_one == "rock" and player_two == "rock":
    print("Tie")
elif player_one == "paper" and player_two == "rock":
    print("Player One Wins")
elif player_one == "scissors" and player_two == "rock":
    print("Player Two Wins")
elif player_one == "rock" and player_two == "scissors":
    print("Player One Wins")
elif player_one == "paper" and player_two == "scissors":
    print("Player Two Wins")
elif player_one == "scissors" and player_two == "scissors":
    print("Tie")

