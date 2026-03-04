import rps
from rps import *


def main():
    keepPlaying = True
    rps.displayInstructions.called = False
    displayInstructions()
    userChoice = getUserChoice()
    computerChoice = getComputerChoice()
    print("User Choice:",userChoice)
    print("Computer Choice:", computerChoice)
    getWinner(computerChoice,userChoice)
    print("Thanks for playing!")

if __name__ == "__main__":
  main()