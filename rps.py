from random import randint
from time import sleep
import rules
choices = ["rock", "paper", "scissors", "lizard", "spock"]

def displayInstructions():
    """
    Displays Instructions for the game rock, paper, scissors, lizard, spock.
    :return:
    """

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



def getUserChoice():
    """
    Gets user choice from input and validates it against answers, reprompting if necessary
    :returns: User Choice is Returned
    :rtype: str
    """
    choice = ""

    while choice not in choices:
        choice = input("Choose either Rock, Paper, Scissors, Lizard, or Spock: ").lower()
        if choice not in choices:
            print("Invalid Choice. Try again.")
    return choice

def getComputerChoice():
    """
    Gets randomly generated choice for the CPU
    :returns: Computer Choice
    :rtype: str
    """
    return choices[randint(0,4)]

def getWinner(comp, player):
    """
    Compares both player choices against the rules dictionary and determines the winner
    :param comp:
    :param player:
    :return: Winner
    :rtype: str
    """
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
    """
    Displays all five options in order 1 second at a time
    :param waitTime:
    :return:
    """
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