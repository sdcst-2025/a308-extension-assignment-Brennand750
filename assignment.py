#! python3

# SD Computing Studies Assignment
'''Task 1'''

import random
rnum = random.randint(1,100)
attempts = 0
print("Please guess a random number.")
while True:
    guess = input("Please guess the random number generated")
    guess = int(guess)
    attempts += 1
    if guess < rnum:
        print("You are too low")
    elif guess > rnum:
        print("You are too high")
    else:
        print("You are correct")
        print("It took you this many trys", attempts)


