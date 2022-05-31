"""
:Problem: Zebras and Ocelots
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""

n = int(input())
pile = ""
for i in reversed(range(n)):    # Add 0's and 1's to the pile in reverse order to make a bit string
    animal = input()
    if animal == 'Z':           # Zebra = 0, Ocelot = 1
        pile = pile + "0"
    else:
        pile = pile + '1'
                                # Flipping all zebras below the first ocelot is equivalent to bit subtraction of 1
print(int(pile, 2))             # Convert the bit string to an integer.
                                # The value of the bitstring is equal to the number of subtract 1's to reach 0