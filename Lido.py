import random

def roll():
    max_v = 6
    min_v = 1
    roll = random.randint(min_v, max_v)
    return roll

while True:
    players = input("plz select number between (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Seclect number between (2 - 4). ")
    else:
        print("invalid value, try again! ")

max_score = 50

player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_indx in range(players):
        print("\n Player number", player_indx +1 , "turn has just started!\n Your total score is:" , player_score[player_indx], "\n")
        current_score = 0
        while True:
            should_roll = input("Would you like to roll? (y or n): ")
            if should_roll.lower() != "y":
                break
            value = roll()

            if value == 1:
                print("You rolled a 1, your turn is gone !!! ")
                current_score = 0
                break
            else:
                print("You rolled a:", value)
                current_score += value
            print("Your cuurent score is:", current_score)
        player_score[player_indx] += current_score
        print("Your total score is:", player_score[player_indx])
print("The winner is player number:" , player_score.index(max(player_score))+1)
print(player_score)
