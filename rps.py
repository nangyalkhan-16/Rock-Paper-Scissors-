import random


def get_winner(player, computer):
    """Return who won the round: 'player', 'computer', or 'tie'."""
    if player == computer:
        return "tie"

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if winning_moves[player] == computer:
        return "player"
    return "computer"


def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will play 5 rounds against the computer.\n")

    player_score = 0
    computer_score = 0
    ties = 0

    for round_num in range(1, 6):
        while True:
            player = input(f"Round {round_num}: Choose rock, paper, or scissors: ").strip().lower()
            if player in {"rock", "paper", "scissors"}:
                break
            print("Invalid choice. Please type rock, paper, or scissors.")

        computer = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            ties += 1
            print("It's a tie!")

        print(f"Score: You {player_score} - {computer_score} Computer | Ties: {ties}\n")

    print("Game over!")
    if player_score > computer_score:
        print("You are the champion!")
    elif computer_score > player_score:
        print("Computer is the champion!")
    else:
        print("It's a tie game!")


if __name__ == "__main__":
    main()
