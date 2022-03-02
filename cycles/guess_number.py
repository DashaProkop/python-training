import random

tries = 0
number = random.randint(1, 50)
print('What number did i conceiv?')
while tries < 6:
    guess = int(input('Enter a number between 1 to 50: '))
    tries += 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    elif guess == number:
        print(f'Congratulations! You guessed my number in {tries} guesses')
        break
    elif guess != number and tries > 6:
        print('Sorry')
        break
