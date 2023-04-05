import random


def play_game():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    user_choice = input("Choose rock, paper, or scissors: ")
    print("Computer chose", computer_choice)
    if computer_choice == user_choice:
        print("Tie!")
    elif (computer_choice == 'rock' and user_choice == 'scissors' or
          computer_choice == 'paper' and user_choice == 'rock' or
          computer_choice == 'scissors' and user_choice == 'paper'):
        print("You lose!")
    else:
        print("You win!")


while True:
    play_game()
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
        break
