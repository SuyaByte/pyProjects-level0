# 2. Guess the Number

# The Goal: Similar to the first project, this project also uses the random module in Python. The program will first randomly generate a number unknown to the user.
# The user needs to guess what that number is. (In other words, the user needs to be able to input information).
# If the user’s guess is wrong, the program should return some sort of indication as to how wrong (e.g. The number is too high or too low).
# If the user guesses correctly, a positive indication should appear.
# You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number and the randomly generated numbers, and to then compare the numbers.

import random as rd
print("***...Welcome to the number guessing game...***")
print("!!!...You can choose a range here...!!!")
print("Enter the lowest number:")
a = int(input())
print("Enter the highest number:")
b = int(input())
print(r"Do you want to start the game? Enter (y/n)")
answer = input()
while answer != '':
    if answer == 'n':
        break
    elif answer == 'y':
        print("Guess the number:")
        actual = rd.randint(a, b)
        guess = input()
        while True:
            if guess.isnumeric():
                if int(guess) == actual:
                    print("Viola! you guessed it correctly")
                    break
                elif int(guess) <= a or int(guess) >= b:
                    guess = input("Your number is out of range. Try again\n")
                elif int(guess) <= actual:
                    guess = input("Your guess is too low. Try again\n")
                else:
                    guess = input("Your guess is too high. Try again\n")
            else:
                print("!!!---Enter only numbers---!!!\n Try again:")
                guess = input()
        print(r"Do you want to play again? Enter (y/n)")
        answer = input()
    else:
        print("Enter either 'y' or 'n'")
        answer = input()
print("Thank you for playing")
