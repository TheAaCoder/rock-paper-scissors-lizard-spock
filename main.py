import rps
from rps import *


def main():
    keepPlaying = True
    rps.displayInstructions.called = False
    displayInstructions()
    while keepPlaying:
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()
        print("The computer chose: " + computerChoice +".")
        getWinner(computerChoice,userChoice)
        playAgain = input("Would you like to keep playing?[y/n] ")

        while playAgain[0].lower() not in ('y', 'n'):
            playAgain = input("Not a valid option. Please enter y or n: ")

        if playAgain[0].lower() == 'n':
            keepPlaying = False
    print("Thanks for playing!")

if __name__ == "__main__":
  main()