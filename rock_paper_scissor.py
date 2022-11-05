import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
while True:
    user_input = input("Please enter rock/paper/scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #rock:0, paper:1, scissors: 2

    computer_guess = options[random_number]
    print("Computer guess: ",computer_guess)

    if user_input == "rock" and computer_guess == "paper":
        print("Computer Wins!")
        computer_wins += 1
        continue
    elif user_input == "rock" and computer_guess == "scissors":
        print("User Wins!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_guess == "rock":
        print("User Wins!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_guess == "rock":
        print("Computer Wins!")
        computer_wins += 1
        continue
    elif user_input == "paper" and computer_guess == "scissors":
        print("Computer Wins!")
        computer_wins += 1
        continue
    elif user_input == "scissors" and computer_guess == "paper":
        print("User Wins!")
        user_wins += 1
        continue
    elif user_input == computer_guess:
        print("Draw!")
        continue
    else:
        print("You Lost!")
        continue

print("User score: ", user_wins, "Computer score:" ,computer_wins)