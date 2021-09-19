import random

MIN = 1
MAX = 1000

r = random.randint(MIN,MAX)

guess = 0
tries = 0

while guess != r:
    tries += 1
    guess = int(input(f"Guess a number between {MIN} and {MAX}: "))
    if guess < r:
        print("Too low! Try again.")
    elif guess > r:
        print("Too high! Try again.")
    else:
        if tries == 1:
            print("Congratulations! You nailed it after 1 try.")
        else:
            print(f"Congratulations! You nailed it after {tries} tries.")