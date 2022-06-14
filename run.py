import random


USER_CHOICES = """
Make a choice:
  * rock
  * paper
  * scissors:
"""


YES_OR_NO = "Do you want to play again?  y/n\n"


def game():
    """
    Implements the main game functionality.
        1. Accepts user choice
        2. Generate random choice for computer
        3. Check if it is a tie or user won the game.
    """
    player_input = input(USER_CHOICES).lower()
    print(f"\nYou chose {player_input}.\n")

    if player_input == "rock":
        pass
    elif player_input == "paper":
        pass
    elif player_input == "scissors":
        pass
    else:
        print(f"{player_input} is not an option. Try again!\n\n")
        print(game())

    ai_input = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {ai_input}.\n")

    if player_input == ai_input:
        return "Its a tie.\n"
    if winner_is(player_input, ai_input):
        return f"{player_input} beats {ai_input}.\n" "\nYou win! :)\n"
    else:
        return f"{ai_input} beats {player_input}.\n" "\nComputer won :(\n"


def replay_game():
    """
    Prompts the user to restart the game.
    """
    play_again = input(YES_OR_NO).lower()

    if play_again == "y":
        print(game())
        replay_game()
    elif play_again == "n":
        None
    else:
        print(f"{play_again} is not an option, try again!\n")
        replay_game()


def winner_is(user, computer):
    """
    Function for determining who Won the game.
    """
    if (
        user == "rock"
        and computer == "scissors"
        or user == "scissors"
        and computer == "paper"
    ) or (user == "paper" and computer == "rock"):
        return True


def main():
    print(game())
    print(replay_game())


if __name__ == "__main__":
    (main())
