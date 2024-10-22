# FIXME Handle KeyError for when player enters a string and not an int

import random

# creates random num variable between 1 and 10
random_num = random.randint(1, 11)

# created an int input variable user_guess
user_guess = int(input('Enter a number between 1 and 10: '))

# while user guess is not the random number loop
while user_guess != random_num:
    # if user guess is less than 1 or greater than 10 remind user to stay between those numbers and ask for guess again
    if user_guess < 1 or user_guess > 10:
        print('Please keep the number between 1 and 10')
        user_guess = int(input('Enter a number between 1 and 10: '))
    # Else if user guess is the random number, break the loop
    elif user_guess == random_num:
        break
    # Else if user guess is higher than the random number, tell player guess is too high and ask for guess again
    elif user_guess > random_num:
        print('Too high, try again.')
        user_guess = int(input('Enter a number between 1 and 10: '))
    # Else user guess to less than the random number, tell player guess is too low and ask for guess again
    else:
        print('Too low, try again.')
        user_guess = int(input('Enter a number between 1 and 10: '))

# Prints the random number was successfully guessed
print(f'The number was {random_num}, you guessed right!')