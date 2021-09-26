import random

def numberGuess():
  randNum = random.randrange(1,101) # this line generates a random number
  guess = int(input("Try to guess the number, between 1 and 100: ")) # ask user for a number

  while True:
    if (guess == randNum):
        print ("\nYou got it!")
        break
    if (guess > randNum):
        print ("Wrong! You guessed too high")
        guess = int(input("\nTry to guess the number:"))  # ask user for a number
    if (guess < randNum):
        print ("Wrong! You guessed too low")
        guess = int(input("\nTry to guess the number:"))  # ask user for a number

numberGuess()