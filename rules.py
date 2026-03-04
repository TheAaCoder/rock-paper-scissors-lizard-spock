wins_against = {
    "rock":     ["scissors", "lizard"],
    "paper":    ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard":   ["spock", "paper"],
    "spock":    ["rock", "scissors"]
}

explanation = {
    ("rock", "scissors"): "Rock crushes Scissors",
    ("rock", "lizard"): "Rock crushes Lizard",
    ("paper", "rock"): "Paper covers Rock",
    ("paper", "spock"): "Paper disproves Spock",
    ("scissors", "paper"): "Scissors cuts Paper",
    ("scissors", "lizard"): "Scissors decapitates Lizard",
    ("lizard", "spock"): "Lizard poisons Spock",
    ("lizard", "paper"): "Lizard eats Paper",
    ("spock", "rock"): "Spock vaporizes Rock",
    ("spock", "scissors"): "Spock smashes Scissors"
}