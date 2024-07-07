import random

n1= int(input("Please define the lowest value: "))
n2= int(input("Please define the highest value: "))
R = range(n1,n2)
D = (random.randint(n1, n2))
attemp = 7

def guess():
    global attemp
    if attemp == 0:
        print('Sorry you lost your chances :(')
    else:
        G = int(input("Please guess the number: "))
        if D == G:
            print(f"Congratulations, you got it :) \n you got it in {7- attemp +1} chances.")
        elif D < G:
            print("You guess too high!, you can guess again: ")
            attemp -= 1
            return guess()
        else:
            print("You guess too little!, you can guess again: ")
            attemp -= 1
            return guess()
guess()
print(f"The number is {D} ")
