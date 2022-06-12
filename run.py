import random
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('played')

Blad1 = SHEET.worksheet('Blad1')

data = Blad1.get_all_values()

print(data)


def game():
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
    play_again = input("Do you want to play again?  y/n\n")

    if play_again == "y":
        print(data)
        print(game())
        replay()
    elif play_again == "n":
        None
    else:
        print(f"{play_again} is not an option, try again!\n")
        replay()


def winner(user, computer):
    if (user == 'rock' and computer == 'scissors' or
        user == 'scissors' and computer == 'paper') \
            or (user == 'paper' and computer == 'rock'):
        return True


print(game())
print(replay())
