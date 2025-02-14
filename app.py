import random
import string

play = True
score = 0
round = 0

options = ["rock", "paper", "scissors"]

while play == True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user != "rock" and user != "paper" and user != "scissors":
        print("Invalid input. Please try again.")
        break
    print("You chose: " + user)

    round += 1
    comp = random.choice(options)
    print("Computer chose: " + comp)

    if user == comp:
        print("It's a tie!")
    elif user == "rock" and comp == "scissors":
        print("You win!")
        score += 1
    elif user == "paper" and comp == "rock":
        print("You win!")
        score += 1
    elif user == "scissors" and comp == "paper": 
        print("You win!")
        score += 1
    else: 
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        play = False

# print the number of rounds played and the score
print("You played " + str(round) + " rounds.")
print("Your score is: " + str(score))
print("Thanks for playing!")
