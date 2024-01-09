import random

while True:
    user = input("Enter your choice (rock/paper/scissor): ")

    elements = ['rock', 'paper', 'scissor']

    computer = random.choice(elements)
    
    if user == computer:
        print(user, "vs", computer)
        print("Tie!")
    elif user == 'rock':
        if computer == 'paper':
            print(user, "vs", computer)
            print("You lose!", computer, "covers", user)
        else:
            print(user, "vs", computer)
            print("You win!", user, "smashes", computer)
    elif user == 'paper':
        if computer == 'scissor':
            print(user, "vs", computer)
            print("You lose!", computer, "cut", user)
        else:
            print(user, "vs", computer)
            print("You win!", user, "covers", computer)
    elif user == 'scissor':
        if computer == 'rock':
            print(user, "vs", computer)
            print("You lose!", computer, "smashes", user)
        else:
            print(user, "vs", computer)
            print("You win!", user, "cut", computer)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
