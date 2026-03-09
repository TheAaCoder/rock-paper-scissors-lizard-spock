from random import randint
from time import sleep

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
        choice = input("Choose either Rock, Paper, Scissors, Lizard, or Spock: ").lower()
        if choice not in choices:
            print("Invalid Choice. Try again.")
    return choice

def getComputerChoice():
    return choices[randint(0,4)]

def getWinner(comp, player):
    if comp in rules.wins_against[player]:
        print("Player Wins!")
        print("This is because: " + rules.explanation[(player,comp)])
        return "Player"
    elif comp == player:
        print("It's a tie!")
        return None
    else:
        print("Computer Wins!")
        print("This is because: " + rules.explanation[(comp,player)])
        return "Computer"

def shoot(waitTime):
    print("Rock.", end=" ")
    sleep(waitTime)
    print("Paper.", end=" ")
    sleep(waitTime)
    print("Scissors.", end=" ")
    sleep(waitTime)
    print("Lizard.", end=" ")
    sleep(waitTime)
    print("Spock.", end=" ")
    sleep(waitTime)
    print("Shoot!", end="")
    sleep(waitTime)
    print()