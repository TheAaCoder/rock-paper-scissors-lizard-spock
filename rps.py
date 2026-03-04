def displayInstructions():
    if not displayInstructions.called:
        print("This is the game rock, paper, scissors, lizard, spock.")
        print("""
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
        """)
        print("You are playing against the computer.")
        displayInstructions.called = True
