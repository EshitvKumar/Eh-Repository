import random

lim = 1000000
num = random.randrange(0, lim + 1)

start_1 = 0
start_2 = lim
i = 0
while True:
    i += 1
    guess = round((start_2 + start_1)/2)
    if guess > num:
        start_2 = guess
    elif guess < num:
        start_1 = guess
    elif guess == num:
        print("{} was correct".format(guess))
        break
print("took {} iterations".format(i))