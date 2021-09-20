import random
from cs50 import get_int
import sys

# Explain the rules
print("Welcome to the Cows and Bulls Game!")
print("Computer generates a 4-digit number and your task is to guess it.")
print("You get feedback after each guees. You get a cow for every digit guessed correctly in the correct place. You get a bull for every digit guessed correctly in the wrong place.")
print("The game ends when you manage to guees the entire number correctly.")

r = random.randint(1000,9999)
sr = str(r)

guess = 0
tries = 0

while guess != r:
    cows = 0
    bulls = 0
    tries += 1
    guess = get_int("Enter a 4-digit number: ")
    sguess = str(guess)
    if guess < 1000 or r > 9999:
        print('Error. You must provide 4-digit number')
        sys.exit

    for i in range(0,4):
        if sr[i] == sguess[i]:
            cows += 1
        else:
            if sguess[i] in list(sr):
                bulls += 1
    print(f'{cows}, {bulls}')

    if (cows == 1) and (bulls == 0):
        print('1 cow, 1 bull')
    elif cows == 1:
        print(f'1 cow, {bulls} bulls')
    elif bulls == 1:
        print(f'{cows} cows, 1 bull')
    else:
        print(f'{cows} cows, {bulls} bulls')

if tries == 1:
    print(f'Congrats! You got it after 1 try!')
else:
    print(f'Congrats! You got it after {tries} tries.')