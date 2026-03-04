import random
choiceWords = ["rock", "paper", "scissors"]
def displayInstructions():
    if not displayInstructions.called:
        print("This is the game rock, paper, scissors.")
        print("You are playing against the computer.")
        displayInstructions.called = True

def getWinner(player, comp):
    if player == comp:
        print("It was a tie.")
    elif (player - comp) % 3 == 1:
        print("You won!")
    else:
        print("The computer won.")

def getCompMove():
    compMove = random.randint(0, 2)
    print(f"The computer picked {choiceWords[compMove]}.")
    return compMove

def getMove():
    userInput = input("Please enter (R)ock, (P)aper, or (S)cissors: ")

    while not userInput or userInput[0].lower() not in ['r','p','s']:
        userInput = input("Invalid choice. Must be R, P, or S. Please try again:")

    playerMove = userInput[0].lower()

    for i in range(len(choiceWords)):
        if choiceWords[i][0].lower() == playerMove:
            return i


def playAgain(msg):
  answer = input(msg).lower()
  while answer not in ['y', 'n']:
    answer = input("Invalid response, must be y or n: ").lower()
  return answer == 'y'