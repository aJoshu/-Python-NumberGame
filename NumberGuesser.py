import random;
from termcolor import colored, cprint

number = random.randint(1, 25)
maxattempts = 6
number_of_guesses = 0
cprint('Guess the number between 1 and 25.','green')

while number_of_guesses < maxattempts:
        number_of_guesses += 1
        guess = int(input())
        if guess < number:
            cprint('Your guess is too low you have '+str(maxattempts-number_of_guesses)+' tries left.','red')
        if guess > number:
            cprint('Your guess is too high','red')

        if guess == number:
         break

    
if guess == number:
    if int(number_of_guesses) < 1:
        cprint('You guessed the number first time!','green')
    else:
        cprint('You guessed the number in ' + str(number_of_guesses) + ' tries!\nIt was '+str(number),'yellow')
else:
    cprint('You did not guess the number, The number was ' + str(number),'red')
    
