### This is a Python-based guessing game, using random variables, booleans, else/if statements, and while loops. This was started at 21:00 on Tuesday, Jan 7 2025. ###
import random
### An issue I ran into while coding this was making sure that a player would not be able to guess a number outside the range without an error, so I created a function which defined the range of numbers in the range I wanted. ###
def inRange(guess):
    return guess > 0 and guess < 101

### I used randint in order to generate the number. ###
number = random.randint(1,100)

###I then print the title of the game and a short description of the game to create an easily understood and simple user interface. ###
print("HIGHER OR LOWER NUMBER GAME")
print("Guess what number the computer has generated. Enter a number between 1 and 100!")
guesses = 0
guessing = True

###For the gameplay, I used a simple while loop, and made sure to account for errors (EG: The player typing "1000" or "pie"). ###
while guessing:
    guess = int(input("What is your guess? "))
    guesses += 1
    if guess < number and inRange(guess):
        print("The number you chose is too low!")
    elif guess > number and inRange(guess):
        print("The number you chose is too high!")
    elif guess == number and inRange(guess):
        guessing = False
        print("Correct! You've won the game! Your prize? A succulent pie 🥧")
        print("It took you " + str(guesses) + " tries.")
    else:
        print("ERROR! Input a number between 1 and 100")

###When finished, I began debugging and testing the program, I faced issues with syntax (formatted the else statement incorrectly) and incorrectly capitalised the randint function. I played through the game multiple times, both correctly and incorrectly, in order to make sure that the game worked as intended. I had extra time so I added a simple tally feature using guesses += 1###
