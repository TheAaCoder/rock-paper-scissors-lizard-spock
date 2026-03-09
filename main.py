import rps
from rps import *


def main():
    computerScore = 0
    playerScore = 0
    keepPlaying = True
    rps.displayInstructions.called = False
    displayInstructions()
    while keepPlaying:
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()
        print("The computer chose: " + computerChoice +".")
        winner = getWinner(computerChoice,userChoice)
        if winner == "Player":
            playerScore += 1
        elif winner == "Computer":
            computerScore += 1
        else:
            computerScore += 1
            playerScore += 1
        print(f"Computer: {computerScore}\nPlayer: {playerScore}")
        playAgain = input("Would you like to keep playing?[y/n] ")

        while playAgain[0].lower() not in ('y', 'n'):
            playAgain = input("Not a valid option. Please enter y or n: ")

        if playAgain[0].lower() == 'n':
            keepPlaying = False

    print("\nFinal Score")
    print(f"Computer: {computerScore}\nPlayer: {playerScore}")
    print()
    print("Thanks for playing!")

if __name__ == "__main__":
  main()