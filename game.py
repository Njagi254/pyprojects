import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Kigongi a deductive logic game
I am thinking of a {}-- digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When i say :        That means:
Pico                One digit is correct but in the wrong position
Fermi               One digit is correct and in the right position
Kigongi             No digit is correct

For ecample if the secret number was 248 and your guess is 843, the 
clues would be Fermi Pico.'''.format(NUM_DIGITS))
while True:
    secretNum = getSecretNum()
    print('I have thought up a number.')
    print('You have {} guesses to get it.'.format(MAX_GUESSES))
    