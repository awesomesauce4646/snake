import os
import random
import time

word = "CHILD"
guessed = False

print("HELLO!")
while (not guessed):
    print("guess the five letter word")

    answer = input("GUESS:" )
    answer = answer.upper()

    if answer == word:
        print("YAHOOO!")
        guessed = True
    else:
        print("TRY AGAIN!")

