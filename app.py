import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    while True:
        choice = input("Choose rock, paper, scissors, or quit: ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        if choice in ["quit", "exit"]:
            return None
        print("Invalid option. Please enter rock, paper, scissors, or quit.")


def determine_winner(player, computer):
    if player == computer:
        return "tie"
    if (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        return "player"
    return "computer"


def play_round():
    player_choice = get_player_choice()
    if player_choice is None:
        return None

    computer_choice = get_computer_choice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
        return 0
    if result == "player":
        print("You win this round!")
        return 1
    print("You lose this round.")
    return -1


def main():
    print("Welcome to Rock, Paper, Scissors!")
    player_score = 0
    computer_score = 0
    rounds_played = 0

    while True:
        result = play_round()
        if result is None:
            print("\nGoodbye!")
            break

        rounds_played += 1
        if result == 1:
            player_score += 1
        elif result == -1:
            computer_score += 1

        play_again = input("Play again? (yes/no): ").strip().lower()
        while play_again not in ["yes", "no", "y", "n"]:
            print("Invalid answer. Please enter yes or no.")
            play_again = input("Play again? (yes/no): ").strip().lower()

        if play_again in ["no", "n"]:
            break

    print("\nGame over!")
    print(f"Rounds played: {rounds_played}")
    print(f"Your score: {player_score}")
    print(f"Computer score: {computer_score}")

    if player_score > computer_score:
        print("You won the game!")
    elif player_score < computer_score:
        print("The computer won the game.")
    else:
        print("The game ended in a tie.")


if __name__ == "__main__":
    main()
