# Rock-Paper-Scissors Console Game

A simple Python minigame where a player competes against the computer through the terminal. The computer randomly chooses rock, paper, or scissors on each round, and the player can choose to continue or quit after any round.

## Features

- Console-based gameplay
- Validates user input and warns on invalid selections
- Supports `rock`, `paper`, `scissors`, and `quit` / `exit`
- Displays round results: win, lose, or tie
- Tracks player and computer scores
- Shows final score summary when the game ends

## Files

- `app.py` — main Python script for the game

## How to run

1. Open a terminal in the repository folder.
2. Run:

```bash
python app.py
```

3. Follow the prompts:
   - Enter `rock`, `paper`, or `scissors` to play a round.
   - Enter `quit` or `exit` to stop the game immediately.
   - After each completed round, choose whether to play again.

## Example session

```text
Welcome to Rock, Paper, Scissors!
Choose rock, paper, scissors, or quit: rock
You chose: rock
Computer chose: scissors
You win this round!
Play again? (yes/no): yes
Choose rock, paper, scissors, or quit: exit

Goodbye!
```

## Notes

- The game converts input to lowercase and trims extra whitespace.
- Invalid entries are handled gracefully with an error message.
- The final summary shows rounds played and the final winner.
