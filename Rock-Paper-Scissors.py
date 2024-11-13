import random

def get_name():
    name = input("\nEnter your name: ")
    return name

def computer():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer = "Rock"
    elif computer_choice == 2:
        computer = "Paper"
    else:
        computer = "Scissors"
    return computer

def main():
    name = get_name()
    print(f"Hello , {name}! Welcome to Rock-Paper-Scissors Game.")
    print('''You can choose one of the following: 
    1. Rock
    2. Paper
    3. Scissors''')
    computer_score = 0
    user_score = 0
    while True:
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            if choice == '1':
                choice_name = 'Rock'
            elif choice == '2':
                choice_name = 'Paper'
            else:
                choice_name = 'Scissors'
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
            continue
        computer_ch = computer()
        if choice_name == computer_ch:
            print(f"Both players selected {choice_name}. It's a tie!")
        elif choice_name == 'Rock':
            if computer_ch == 'Scissors':
                print(f"{name} wins! {choice_name} smashes {computer_ch}!")
                user_score += 1
                print(f"{name} score is {user_score}, Computer score is {computer_score}")
            else:
                print(f"Computer wins! {computer_ch} covers {choice_name}!")
                computer_score += 1
                print(f"{name} score is {user_score}, Computer score is {computer_score}")
        elif choice_name == 'Paper':
            if computer_ch == 'Rock':
                print(f"{name} wins! {choice_name} covers {computer_ch}!")
                user_score += 1
                print(f"{name} score is {user_score}, Computer score is {computer_score}")
            else:
                print(f"Computer wins! {computer_ch} cuts {choice_name}!")
                computer_score += 1
                print(f"{name} score is {user_score}, Computer score is {computer_score}")
        elif choice_name == 'Scissors':
            if computer_ch == 'Paper':
                print(f"{name} wins! {choice_name} cuts {computer_ch}!")
                user_score += 1
                print(f"{name} score is {user_score}, Computer score is {computer_score}")
            else:
                print(f"Computer wins! {computer_ch} smashes {choice_name}!")
                computer_score += 1
                print(f"{name} score is {user_score}, Computer score is {computer_score}")
        
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            print("Thanks for playing!")

            break
        
main()



