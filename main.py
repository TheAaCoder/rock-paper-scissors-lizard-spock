import rps


def main():
    keepPlaying = True
    rps.displayInstructions.called = False

    while keepPlaying:
        rps.displayInstructions()

        userMove = rps.getMove()
        compMove = rps.getCompMove()
        rps.getWinner(userMove, compMove)

        if not rps.playAgain("Do you want to play again y/n? "):
            keepPlaying = False

    print("Thanks for playing!")


if __name__ == "__main__":
  main()