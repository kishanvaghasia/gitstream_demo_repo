import random

top_of_range = input("Enter the limit of random the Number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # converting it to an integer
    if top_of_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please enter a number greater zero!")
    quit()

random_number = random.randrange(0, top_of_range)
guesses = 0
while True:
    guesses= guesses+1
    user_guess = input("Enter a number to guess:")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time!")
        continue

    if user_guess == random_number:
        print("Your guess is correct, after",guesses,"guessess" )
        break
    else:
        if user_guess < random_number:
            lower_higher_sring = "higher"
        else:
            lower_higher_sring = "lower"
        print("Incorrect guessed nummber, please try guessing",lower_higher_sring)


