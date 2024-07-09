import random

is_choice = True
while is_choice:
    user_choice = int(input("Enter your choice:\n'0' for Rock.\n'1' for Scissor.\n'2' for Paper:\n"))
    computer_choice=random.randint(0,2)
    print("Computer choice",computer_choice)
    if user_choice==0 and computer_choice==0:
        print("Draw!")
    elif user_choice == 0 and computer_choice == 1:
        print("You wins!")
    elif user_choice == 0 and computer_choice == 2:
        print("Computer Wins!")
    elif user_choice == 1 and computer_choice == 0:
        print("Computer Wins!")
    elif user_choice == 1 and computer_choice == 1:
        print("Draw!")
    elif user_choice == 1 and computer_choice == 2:
        print("You Wins!")
    elif user_choice == 2 and computer_choice == 0:
        print("Computer Wins!")
    elif user_choice == 2 and computer_choice == 1:
        print("You Wins!")
    elif user_choice == 2 and computer_choice == 2:
        print("Draw")
    play_again = input("Do you want to play again(y/n):").lower()
    if play_again=="n":
        print("Exit from the game.")
        print("Thankyou for playing!")
        is_choice = False


