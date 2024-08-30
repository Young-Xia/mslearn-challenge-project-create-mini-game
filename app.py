import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        return "win"
    else:
        return "lose"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    wins = 0
    rounds = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to stop playing: ").lower()
        
        if player_choice == 'quit':
            print(f"Thanks for playing! You won {wins} out of {rounds} rounds.")
            break
        elif player_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"The computer chose: {computer_choice}")

        result = get_winner(player_choice, computer_choice)
        rounds += 1

        if result == "win":
            wins += 1
            print("You win this round!")
        elif result == "lose":
            print("You lose this round.")
        else:
            print("It's a tie.")

        print(f"Current score: {wins} wins out of {rounds} rounds.\n")
        
        continue_playing = input("Do you want to continue playing? (yes/no): ").lower()
        if continue_playing != 'yes':
            print(f"Final score: You won {wins} out of {rounds} rounds.")
            print("Goodbye!")
            break

if __name__ == "__main__":
    play_game()