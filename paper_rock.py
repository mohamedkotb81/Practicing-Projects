import random

options = ["paper", "rock", "scissors"]

user_wins = 0
computer_wins = 0


while True:
    user_input = input('please write "paper, rock, scissors" to play or "q" to quite. ')
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    else:
        computer_choice = random.randint(0,2)
        comp_pick = options[computer_choice]
        if user_input == comp_pick:
            print("withdraw..")
        elif user_input == "paper" and comp_pick == "rock":
            print("You Win !")
            user_wins +=1
        elif user_input == "scissors" and comp_pick == "paper":
            print("You Win !")
            user_wins +=1
        elif user_input == "rock" and comp_pick == "scissors":
            print("You Win !")
            user_wins +=1
        else:
            print("Computer wins !!!")
            computer_wins +=1

print('You won: ', user_wins)
print('Computer won: ', computer_wins)
print("Good Bye!")