import random


def game():
    """
    Function for game mechanics.
    """
    player = input("Make a choice:\n rock, paper or scissors?\n")
    print(f"You chose {player}\n")

    if player == "rock":
        pass
    elif player == "paper":
        pass
    elif player == "scissors":
        pass
    else:
        print(f"{player} is not an option. Try again!\n")
        print(game())

    ai = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose {ai}\n")

    if player == ai:
        return "Its a tie.\n"
    
    if winner(player, ai):
        return "You win! :)\n"
    else:
        return "Computer won :(\n"


def replay():
    """
    Function for Restarting the game.
    """
    play_again = input("Do you want to play again?  y/n\n")

    if play_again == "y":
        print(game())
        replay()
    elif play_again == "n":
        None
    else:
        print(f"{play_again} is not an option, try again!\n")
        replay()


def winner(user, computer):
    """
    Function for determining who Won the game.
    """
    if (user == 'rock' and computer == 'scissors' or
        user == 'scissors' and computer == 'paper') \
            or (user == 'paper' and computer == 'rock'):
        return True


def main():
    print(game())
    print(replay())


(main())