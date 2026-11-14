import os
import random
import time

wordSet = {"APPLE", "CHILD", "HOUSE", "MOUSE", "WATER", "PLANT", "BRAVE", "CANDY", "DREAM", "EARTH"}
word = random.choice(list(wordSet))
guessed = False

print("HELLO!")
while (not guessed):
    print("guess the five letter word")

    answer = input("GUESS:" )
    answer = answer.upper()

    correctLetters = 0
   
    for letter in answer:
        if letter in word:
            correctLetters += 1

    if answer == word:
        print("YAHOOO!")
        guessed = True
    elif correctLetters >= 1:
        print("YOU HAVE " + str(correctLetters) + " CORRECT LETTERS")
    else:
        print("TRY AGAIN!")

