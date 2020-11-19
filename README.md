# Python number guess game

Super simple python command line game for learning python.
## Dependencies
`pip install termcolor`

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Expected result

```js
Guess the number between 1 and 25.
> 10
Your guess is too high
> 2
Your guess is too low you have 2 tries left.
> 4
You guessed the number in 3 tries!
It was 4
```

## Source Code
```py
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
    
```

Please make sure to install dependencies
