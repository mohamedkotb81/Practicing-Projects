import random

print("Player 2 is Computer.")
values = []
s=input("Do you want to start the game? (Yes/No) \n")


def value_check(value):
    if value not in values:
       values.append(value)
    else:
        xo = int(input("The number you added already found, plz add another one: "))
        value_check(xo)

def value_check_two(val):
    if val not in values:
       values.append(val)
    else:
        xoo = random.randint(1,21)
        value_check_two(xoo)

def round_one():
    while len(values) < 22:
      if len(values) == 21:
        print("Congratulations, YOU WON !")
        exit()
      else:
        v = int(input("How many numbers do you wish to enter? "))
        if v + len(values) < 21:
            if 0 < v < 22:
                for c in range(v):
                    c = int(input("Enter your number: "))
                    if 0 < c < 22:
                        value_check(c)
                    else:
                        print("Add values less than 21.")
                print(f"you added {values}")   
                values.sort()
            else:
                print("Choose number less than 21.")
            w = random.randint(1,21)
            value_check_two(w)
            print(f"the computer added {w}")
            values.sort()
            print(f"We have now {values}")
        else:
            if len(values) < 21:
                d = 21 - (len(values)+1)
                print(f"you have {d} values only")
                round_one()
            else:
                exit()

        

def round_two():
    while len(values) < 22:
      if len(values) == 21:
        print("Congratulations, YOU WON !")
        exit()
      else:
        w = random.randint(1,21)
        value_check_two(w)
        print(f"the computer added {w}")
        values.sort()
        # print(f"We have now {values}")
        v = int(input("How many numbers do you wish to enter? "))
        if v + len(values) < 21:
            if 0 < v < 22:
                for c in range(v):
                    c = int(input("Enter your number: "))
                    if 0 < c < 22:
                        value_check(c)
                    else:
                        print("Add values less than 21.")
                print(f"you added {values}")   
                values.sort()
            else:
                print("Choose number less than 21.")
        else:
            if len(values) < 21:
                d = 21 - (len(values)+1)
                print(f"you have {d} values only")
                round_one()
            else:
                exit()

if s in ["Yes", "yes", "Y", "y"]:
    q = input("Enter 'F' to take the first chance.\nEnter 'S' to take the second chance. \n")
    if q in ["F", "f"]:
        round_one()
    elif q in ["S", "s"]:
        round_two()
    else:
        print("Wrong Choice !!")
else:
    print("OKAY; Have a nice time.")