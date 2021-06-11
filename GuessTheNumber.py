import random


def guessing(x):
    randomNumber = random.randint(1, x)
    guessing = 0
    while guessing != randomNumber:
        guessing = int(input(f'Guess a number between 1 and {x}: '))
        if guessing < randomNumber:
            print(f'Your guess ({guessing}) is low! Try again!')
        elif guessing > randomNumber:
            print(f'Your guess ({guessing}) is high! Try again!')

    print(f'Your guess is correct! Congrats! {randomNumber} !')


def compGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (h), too low (l) or correct (c)?').lower()
        if feedback == 'h':
            high = guess + 1
        elif feedback == 'l':
            low = guess + 1
    print(f'I have guessed your number correctly! HA! Guess: {guess}')

compGuess(2750)
