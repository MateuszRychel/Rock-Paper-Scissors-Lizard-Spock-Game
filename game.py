import random

def game():
    moves = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    rules = ["Scissors cuts Paper",
             "Paper covers Rock",
             "Rock crushes Lizard",
             "Lizard poisons Spock",
             "Spock smashes Scissors",
             "Scissors decapitates Lizard",
             "Lizard eats Paper",
             "Paper disproves Spock",
             "Spock vaporizes Rock",
             "Rock crushes Scissors"]

    print("Rules of the game:")
    number_of_rule = 1
    for i in range (len(rules)):
        print(number_of_rule, rules[i])
        number_of_rule += 1
    print()

    print("What you choose?")
    number_of_move = 1
    for i in range(len(moves)):
        print(number_of_move, moves[i])
        number_of_move += 1
    print()
    user_choice = int(input()) -1#-1
    computer_choice = random.randint(0, len(moves) -1)

    print("You chose: ", moves[user_choice])
    print("Computer chose: ", moves[computer_choice])

    if user_choice == computer_choice:
        print("Draw")

    # User Rock
    elif user_choice == 0:
        if computer_choice == 1:
            print("You lose")
        if computer_choice == 2:
            print("You win")
        if computer_choice == 3:
            print("You win")
        if computer_choice == 4:
            print("You lose")

    # User Paper
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win")
        if computer_choice == 2:
            print("You lose")
        if computer_choice == 3:
             print("You win")
        if computer_choice == 4:
            print("You lose")

    # User Scissors
    elif user_choice == 2:
        if computer_choice == 0:
            print("You lose")
        if computer_choice == 1:
            print("You win")
        if computer_choice == 3:
            print("You win")
        if computer_choice == 4:
            print("You lose")

    # User Lizard
    elif user_choice == 3:
        if computer_choice == 0:
            print("You lose")
        if computer_choice == 1:
            print("You lose")
        if computer_choice == 2:
            print("You lose")
        if computer_choice == 4:
            print("You win")

    # User Spock
    elif user_choice == 4:
        if computer_choice == 0:
            print("You win")
        if computer_choice == 1:
            print("You lose")
        if computer_choice == 2:
            print("You win")
        if computer_choice == 3:
            print("You lose")

print(game())