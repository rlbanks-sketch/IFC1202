import random

print("Welcome to the Winners and Losers Game!")  # Title of the game
human_score = 0
computer_score = 0

for round_num in range(1, 6):  # Play 5 rounds
    print("\nRound {}".format(round_num))
    
    # Prompt human to enter a number between 1 and 5
    while True:
        try:
            human_guess = int(input("Enter a number between 1 and 5: "))
            if 1 <= human_guess <= 5:
                break
            else:
                print("Invalid input. Number must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 5.")
    
    # Computer generates a random number between 1 and 5
    computer_guess = random.randint(1, 5)
    
    sum_guesses = human_guess + computer_guess
    
    # Display guesses
    print("Human guess: {}".format(human_guess))
    print("Computer guess: {}".format(computer_guess))
    
    # Check if sum is even or odd and assign scores
    if sum_guesses % 2 == 0:
        print("Sum is Even")
        human_score += 1
    else:
        print("Sum is Odd")
        computer_score += 1
    
    # Display scores
    print("Human score: {}".format(human_score))
    print("Computer score: {}".format(computer_score))

# Final result
print("\nFinal Results:")
if human_score > computer_score:
    print("Human Wins!")
elif computer_score > human_score:
    print("Computer Wins!")
else:
    print("It's a Tie!")
