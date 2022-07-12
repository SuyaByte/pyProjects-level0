# 3. Mad Libs Generator

# The Goal: Inspired by Summer Son’s Mad Libs project with Javascript. The program will first prompt the user for a series of inputs a la Mad Libs. For example, a singular noun, an adjective, etc.
# Then, once all the information has been inputted, the program will take that data and place them into a premade story template.
# You’ll need prompts for user input, and to then print out the full story at the end with the input included.

print("Welcome to the Mad Libs Generator Game")
print("Do you want to play? Enter(y/n)")
answer = input()
while answer != '':
    if answer == 'n':
        break
    elif answer == 'y':
        first = input("Enter an Animal:\n")
        second = input("Enter a Feeling:\n")
        third = input("Enter Things (plural):\n")
        fourth = input("Enter a Profession (like “Baker”):\n")
        fifth = input("Enter a Piece of Clothing:\n")
        sixth = input("Enter Things (plural):\n")
        seventh = input("Enter the name of a Person:\n")
        eighth = input("Enter a Place:\n")
        ninth = input("Enter a Verb (ending in “ing”):\n")
        tenth = input("Enter your favorite Food:\n")
        print("Say '"+tenth+"', the photographer said as the camera flashed! "+seventh+" and I had gone to "+eighth+" to get our photos taken today. The first photo we really wanted was a picture of us dressed as a "+first+" pretending to be a "+fourth+". When we saw the proofs of it, I was a bit "+second+" because it looked different than in my head. (I hadn't imagined so many "+third+" behind us.) However, the second photo was exactly what I wanted. We both looked like "+sixth+" wearing "+fifth+" and "+ninth+"--exactly what I had in mind!")
        print("Do you want to play again? Enter (y/n):")
        answer = input()
    else:
        print("Enter either y or n:")
        answer = input()
print("Thank you for playing")
