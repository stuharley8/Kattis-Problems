"""
:Problem: DNA
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
This solution is the 2nd fastest solution for Python3 as of 4/20/2022
"""
N = int(input())
word = input()

searchFor = 'B'         # Current letter to search for. This will switch if we mutate an entire prefix
lastLetter = -1         # index of the last letter we're searching for in the word
inRow = 0               # How many of the current letters are in a row where we're searching
count = 0               # Number of mutations it will take

for i in range(N-1, -1, -1):    # Starting at the end of the word, search for the first B
    if word[i] == searchFor:
        lastLetter = i
        inRow = 1
        break

while inRow != 0:
    for i in range(lastLetter - 1, -1, -1):     # Determine how many of the letters we're searching for are in a row
        if word[i] == searchFor:
            inRow = inRow + 1
        else:
            break
    lastLetter = lastLetter - inRow     # Calculate the last letter index we will start searching next
    count = count + 1
    if inRow > 1:                       # If we mutated an entire prefix, we swap the letter we're searching for
        if searchFor == 'B':
            searchFor = 'A'
        else:
            searchFor = 'B'
    inRow = 0

    for i in range(lastLetter, -1, -1):     # Search for the next letter we're looking for
        if word[i] == searchFor:
            lastLetter = i
            inRow = 1
            break

print(count)
