"""
:Problem: Guessing Game
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""

lside = 1       # set bounds for valid answers
rside = 10
honest = True
while True:
    guess = int(input())
    if guess == 0:
        break
    response = input()
    if response == "too high":
        if guess <= lside:      # guess is outside the left bound which means its a lie
            honest = False
        if guess <= rside:      # adjusts the right side bound if appropriate
            rside = guess - 1
    elif response == "too low":
        if guess >= rside:      # guess is outside the right bound which means its a lie
            honest = False
        if guess >= lside:      # adjusts the left side bound if appropriate
            lside = guess + 1
    else:       # right on
        if guess < lside or guess > rside:  # checks if the guess is outside either bound which means its a lie
            honest = False
        if honest:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        honest = True       # reset the bounds for the next series of guesses
        lside = 1
        rside = 10