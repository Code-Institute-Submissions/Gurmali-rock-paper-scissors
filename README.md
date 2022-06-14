# Rock Paper scissors

Rock paper scissors is a game originating from china. It's is usualy played by hand between two people.
Rock smashes scissors, scissors cuts paper and paper covers rock.

It's a simple game any two people can play.
And if you dont have a friend to play with, this Program allows you to play against a cumputer.

[This is a link to the live version of my project](https://rock-paper-scissors-gurmali.herokuapp.com/)

<img src="assets/images/responsive.jpg">

## Features

The main feature is a working game that runs on an Heroku mock terminal.

### Features left to implement

 - A scoreboard for keeping track of how many times the user and the computer has won. Or as an alternative, showing the percentages of wins and losses.

## Game play

- The game starts by telling you to choose a hand.
- Rock, Paper or Scissors

<img src="assets/images/game-start.jpg">

- Lets say you chose Rock.
- The application tells the user the option they chose.

<img src="assets/images/the-choice.jpg">

- Randomly selects and option for the computer.
- Tells the user what option the computer has chosen.

<img src="assets/images/computer-choice.jpg">

- Specifies which of the two options beats the other.

<img src="assets/images/beating.jpg">

- And Tells the user who won.

<img src="assets/images/winner.jpg">

- Finaly asking the user if they want to play again.

<img src="assets/images/in-game.jpg">

- Would the user want to play again, the game restarts.

### User errors

- If the user tries to choose anything other than the three options provided, they get an error message prompting them to try again.

<img src="assets/images/wrong-choice.jpg">

- Similarly if the user does not write y or n(upper or lower case, doesn't matter) when asked if they want to play again, the user gets an error message asking them to try again.

<img src="assets/images/try-again.jpg">