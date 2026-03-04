from random import randint
import rules
choices = ["rock", "paper", "scissors", "lizard", "spock"]
def displayInstructions():
    if not displayInstructions.called:
        print("This is the game rock, paper, scissors, lizard, spock.")
        print(
"""
These are the rules:

Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
(and as it always has) Rock crushes Scissors
"""
            )
        print("You are playing against the computer.")
        displayInstructions.called = True

def getUserChoice():
    choice = ""

    while choice not in choices:
        choice = input("Choose either Rock, Paper, Scissors, or Spock: ").lower()
        if choice not in choices:
            print("Invalid Choice. Try again.")
    return choice

def getComputerChoice():
    return choices[randint(0,4)]

def getWinner(comp, player):
    if comp in rules.wins_against[player]:
        print("Player Wins!")
        print("This is because: " + rules.explanation[(player,comp)])
    elif comp == player:
        print("It's a tie!")
    else:
        print("Computer Wins!")
        print("This is because: " + rules.explanation[(comp,player)])

