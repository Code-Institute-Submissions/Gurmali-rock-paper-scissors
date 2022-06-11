import random


def game():
    player = input("Make a choice:\n rock, paper or scissors?\n")
    ai = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose {ai}")

    if player == ai:
        return "Its a tie"
    
    if winner(player, ai):
        return "You win! :)"
    else:
        return "Computer won :("


def winner(user, computer):
    if (user == 'rock' and computer == 'scissors' or
        user == 'scissors' and computer == 'paper') \
            or (user == 'paper' and computer == 'rock'):
        return True


print(game())
