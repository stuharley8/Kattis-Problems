"""
:Problem: Hermit
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numStreet = input()
    streets = input().split(' ')
    # Change all of the inputs into integers
    for x in range(len(streets)):
        streets[x] = int(streets[x])

    # The array of the populations of each street
    population = streets.copy()

    # Go through each intersection and add population to the intersecting streets
    for x in range(int(input())):
        line = input().split(' ')
        # First Index in the input
        first = int(line[0])-1
        # Second Index in the input
        second = int(line[1])-1
        # Add the population of the connected(second) street to the first street
        population[first] = population[first] + streets[second]
        # Add the population of the connected(First) street to the second street
        population[second] = population[second] + streets[first]
    # The lowest population of the streets
    lowest = population[0]
    index = 0
    # Go through all the populations and find the lowest one and its index.
    for x in range(len(population)):
        temp = population[x]
        if temp < lowest:
            lowest = temp
            index = x

    print(index + 1)
