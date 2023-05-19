#5. Hangman

#The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main goal here is to create a sort of “guess the word” game. 
#The user needs to be able to input letter guesses. A limit should also be set on how many guesses they can use. 
#This means you’ll need a way to grab a word to use for guessing. (This can be grabbed from a pre-made list. No need to get too fancy.) 
#You will also need functions to check if the user has actually inputted a single letter, 
#to check if the inputted letter is in the hidden word (and if it is, how many times it appears), to print letters, and a counter variable to limit guesses.

import random
wordsList = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra', 'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']
index = random.randint(0, len(wordsList)-1)
word = wordsList[index]
wordlen = len(word)
print(word)
print("Your word is:")
guess = ""
for i in word:
    guess += "_"
print(guess)
count = 0
count2 = 0
guess2 = ""
while word != guess and count < len(guess):
    count += 1
    print("Do you want to guess a letter or word?\nEnter 1 to guess a letter!\nEnter 2 to guess the word!!")
    ch = input()
    match ch:
        case "1":
            print("Guess a letter:")
            letter = input()
            if len(letter) != 1:
                print("Enter only one letter please.")
                count -= 1
            else:
                for i in range(0, len(word)):
                    if word[i] == letter:
                        guess2 += letter
                        count2 += 1
                    else:
                        guess2 += guess[i]
                guess = guess2
                guess2 = ""
                print(guess)
                if count2 > 0:
                    count2 = 0
                else:
                    print("Oops. Wrong letter.")
        case "2":
            print("Guess the word:")
            ans = input()
            if ans == word:
                print("Yayyyy!! You guessed it right. The word is "+ans+"!!!")
                guess = ans
            else:
                print("Oops. you just lost a chance.")
if count > len(guess):
    print("You have used up all chances. Try again :P")
elif count == len(guess):
    print("You barely managed it.")
else:
    print("You guessed the letters perfectly!")
