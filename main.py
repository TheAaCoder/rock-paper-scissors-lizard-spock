import rps
from rps import displayInstructions


def main():
    keepPlaying = True
    rps.displayInstructions.called = False
    displayInstructions()
    print("Thanks for playing!")


if __name__ == "__main__":
  main()