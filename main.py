import rps
from rps import displayInstructions, getUserChoice


def main():
    keepPlaying = True
    rps.displayInstructions.called = False
    displayInstructions()
    userChoice = getUserChoice()
    print(userChoice)
    print("Thanks for playing!")

if __name__ == "__main__":
  main()