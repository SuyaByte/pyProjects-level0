import random
wordsList = ['aries', 'taurus']
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
