#1. Dice Rolling Simulator
#The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice. When the program runs, it will randomly choose a number between 1 and 6. (Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is. It should then ask you if you’d like to roll again. For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6. You’ll also want a function that randomly grabs a number within that range and prints it.

import random as rd
print("***...Welcome to dice game...***")
print("Enter the lowest value of your dice:")
a = int(input())
print("Enter the highest value of your dice:")
b = int(input())
print(r"Do you want to roll the dice? Enter (y\n)")
tryAgain = input()
while tryAgain != '':
    if tryAgain == 'n':
        break
    elif tryAgain == 'y':
        print("rolling.....")
        output = rd.randint(a, b)
        print(output)
        print(r"Do you want to roll again? Enter (y\n)")
        tryAgain = input()
    else:
        print("Please enter either 'y' or 'n'")
        tryAgain = input()
print("Thank you for playing")
