import random
import time

operators = ["+", "-", "*"]

min_value = 5
max_value = 12
total = 10
wrong = 0

def problem():
    left = random.randint(min_value, max_value)
    right = random.randint(min_value, max_value)
    operator = random.choice(operators)
    exp = str(left) + " " + operator + " " + str(right)
    answer = eval(exp)
    return exp, answer


start_time = time.time()
input("Press any key to start ")
print("-----------------------")

for i in range(total):
    exp, answer = problem()
    while True:
        guess = input("Problem # " + str(i+1) +  ": " + exp + " = ")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()

act_time = round(end_time - start_time, 2)
print("-----------------------")


print("Nice, you finished in", act_time, "seconds and got", wrong, "wrong problems.")

