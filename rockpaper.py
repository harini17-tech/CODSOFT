import random
print("Welcome to ROCK PAPER SCISSORS game")
user_score=0
computer_score=0
while True:
    print("\n Choose any one option:")
    print("1.Rock")
    print("2.Paper")
    print("3..Scissors")
    user_choice = input("Enter 1,2 or 3:")
    if user_choice not in ['1','2','3']:
        print("Invalid ,Please enter 1,2 or 3.")
        continue
    user_choice = int(user_choice)
    computer_choice = random.randint(1,3)
    choices = {1:"Rock",2:"Paper",3:"Scissors"}
    print(f"\nYou Choose:{choices[user_choice]}")
    print(f"\nComputer Choose:{choices[computer_choice]}")
    if user_choice == computer_choice:
        print("Result: It's a draw!")
    elif(user_choice==1 and computer_choice==3)or \
        (user_choice==2 and computer_choice==1)or \
        (user_choice==3 and computer_choice==2):
        print("Result: You Win!")
        user_score+=1
    else:
        print("Result: Computer Wins!")
        computer_score+=1
    print(f"Score-> You:{user_score}|Computer:{computer_score}")
    play_again = input("\nDo you want to play again ?(yes/no):").lower()
    if play_again != 'yes':
        print("\n******GAME OVER******")
        print(f"Final Scores->You:{user_score}|Computer:{computer_score}")
        if user_score > computer_score:
            print("You won the game. Good Job!")
        elif user_score < computer_score:
            print("Computer won the game. Better luck next time!")
        else:
            print("It's a tie!")
        break