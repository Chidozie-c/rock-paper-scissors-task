import random

print("Hi there!\n======Welcome to Rock-Paper-Scissors Python Game======!")

while True:
    # Getting user input
    user = input(
        "Pick an option ('R' for rock, 'P' for paper, 'S' for scissors)\nPlayer: ",
    )
    # List of possible options
    options = ["R", "P", "S"]

    computer = random.choice(options)

    # Computer option
    print("CPU:", computer)

    # Logic conditions (Win, lose or Draw/Tie)
    if user == computer:
        print("Both Player and CPU have selected the same option\nIt's a tie!")

    elif user == "R":
        if computer == "P":
            print("Player (Rock) : CPU (Paper)\nComputer wins!")
        else:
            print("Player wins!")

    elif user == "R":
        if computer == "S":
            print("Player (Rock) : CPU (Scissors)\nPlayer wins!")
        else:
            print("Computer wins!")

    elif user == "S":
        if computer == "R":
            print("Player (Scissors) : CPU (Rock)\nComputer wins!")
        else:
            print("Player wins!")

    elif user == "S":
        if computer == "P":
            print("Player (Scissors) : CPU (Paper)\nPlayer wins!")
        else:
            print("Computer wins!")

    elif user == "P":
        if computer == "S":
            print("Player (Paper) : CPU (Scissors)\nComputer wins!")
        else:
            print("Player wins!")

    elif user == "P":
        if computer == "R":
            print("Player (Paper) : CPU (Rock)\nPlayer wins!")
        else:
            print("Computer wins!")

    # Error message
    else:
        print("Error! Invalid input, enter the correct option ...")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again [yes, no]? : ")
    if play_again == "yes":
        continue
    else:
        print("Oops! Wrong command!")
    if play_again == "no":
        break
print("=====GAME ENDS!====\nI hope you had a nice time. Good bye!")
