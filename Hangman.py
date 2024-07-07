# import random 
# from collections import Counter 
  
# # someWords = '''ahmed mohamed alibaba mostafa  
# # maged sayed osama mahmoud fouad ayman hany 
# # amgad sameh hesham galal naser hassan'''

# someWords = '''ahmed ahmed ahmed ahmed  
# ahmed ahmed ahmed ahmed ahmed ahmed ahmed 
# ahmed ahmed ahmed ahmed ahmed ahmed'''
  
# someWords = someWords.split(' ') 
# word = random.choice(someWords) 
# print('Guess the word! HINT: word is a name of a boy') 

# for i in word: 
#         # For printing the empty spaces for letters of the word 
#     print('_', end=' ') 
# print() 
# chances = 7

# z= list(word)
# y = len(z)
# l=" _ "
# letterGuessed = ''
# # print(z)
# w = []
# correct = 0
# flag = 0


# for _ in range(y+2):
#     x = input("Guess a letter from the name: ").lower()
#     if not x.isalpha(): 
#         print('Enter only a LETTER') 
#         continue
#     elif len(x) > 1: 
#         print('Enter only a SINGLE letter') 
#         continue
#     elif x in z:
#         j = z.index(x)
#         print((l*(y-(y-j))) + x +(l*(y-(j+(y-(y-1))))))
#         w.append(x)
#         continue
#     else:
#         print("Wrong choice!")
#         pass
#     if x in z: 
#     # k stores the number of times the guessed letter occurs in the word 
#         k = word.count(x) 
#     for _ in range(k): 
#         letterGuessed += x  # The guess letter is added as many times as it occurs 

# # Print the word 
# for char in word: 
#     if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
#         print(char, end=' ') 
#         correct += 1
#     # If user has guessed all the letters 
#     # Once the correct word is guessed fully, 
#     elif (Counter(letterGuessed) == Counter(word)): 
#                                                     # the game ends, even if chances remain 
#         print("The word is: ", end=' ') 
#         print(word) 
#         flag = 1
#         print('Congratulations, You won!') 
#         break  # To break out of the for loop 
#         break  # To break out of the while loop 
#     else: 
#         pass

# print("".join(w))


import random 
from collections import Counter 
  
someWords = '''apple banana mango strawberry  orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
  
someWords = someWords.split(' ') 
word = random.choice(someWords) 

if __name__ == '__main__': 
    print('Guess the word! HINT: word is a name of a fruit') 
  
    for i in word: 
        print('_', end=' ') 
    print() 
    # list for storing the letters guessed by the player 
    letterGuessed = '' 
    chances = len(word) + 2
    correct = 0
    flag = 0
    while (chances != 0) and flag == 0:  # flag is updated when the word is correctly guessed 
            chances -= 1
            guess = str(input('\nEnter a letter to guess: ')) 
  
            # Validation of the guess 
            if not guess.isalpha(): 
                print('Enter only a LETTER') 
                continue
            elif len(guess) > 1: 
                print('Enter only a SINGLE letter') 
                continue
            elif guess in letterGuessed: 
                print('You have already guessed that letter') 
                continue
  
            # If letter is guessed correctly 
            if guess in word: 
                k = word.count(guess) # k stores the number of times the guessed letter occurs in the word 
                for _ in range(k): 
                    letterGuessed += guess  # The guess letter is added as many times as it occurs 
  
            # Print the word 
            for char in word: 
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)): 
                    print(char, end=' ') 
                    correct += 1
                # If user has guessed all the letters 
                # Once the correct word is guessed fully, 
                elif (Counter(letterGuessed) == Counter(word)): 
                                                                # the game ends, even if chances remain 
                    print("The word is: ", end=' ') 
                    print(word) 
                    flag = 1
                    print('Congratulations, You won!') 
                    break  # To break out of the for loop 
                    break  # To break out of the while loop 
                else: 
                    print('_', end=' ') 
  
        # If user has used all of his chances 
    if chances <= 0 and (Counter(letterGuessed) != Counter(word)): 
            print() 
            print('You lost! Try again..') 
            print('The word was {}'.format(word)) 
  


    





















