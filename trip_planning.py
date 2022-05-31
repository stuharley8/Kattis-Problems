"""
:Problem: Trip Planning
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""

def main():
    line = input().split()
    cities = int(line[0])
    trains = int(line[1])

    lines = {}
    for i in range(1, trains+1):
        line = input().split()
        if int(line[0]) < int(line[1]):             # Add each train line to the dict always in asc order
            lines[line[0] + ' ' + line[1]] = i
        else:
            lines[line[1] + ' ' + line[0]] = i      # Swap the two cities of a train line if they are in desc order

    seq = []
    for i in range(1, cities):
        if lines.get(str(i) + ' ' + str(i+1)) is not None:      # Checks if there is a line between each adjacent city
            seq.append(lines.get(str(i) + ' ' + str(i+1)))      # Adds the line number to the sequence if it exists
        else:
            print('impossible')                                 # If line doesn't exist prints impossible
            return
    if lines.get('1 ' + str(cities)) is not None:               # Checks if there is a line from 1 to the last number city
        seq.append(lines.get('1 ' + str(cities)))               # Adds the line number to the sequence if it exists
    else:
        print('impossible')                                     # Prints impossible if it doesn't exist
        return
    for i in seq:
        print(i)


main()
