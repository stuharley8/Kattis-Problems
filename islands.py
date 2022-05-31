"""
:Problem: Islands3
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""


def change_clouds(arr, col, row):
    """
    Changes the clouds to land if the cloud touches a land.
    """
    # Checks if the position is valid and if it is a cloud
    if col >= cols or row >= rows or col < 0 or row < 0 or arr[row][col] != 'C':
        return 0

    arr[row][col] = 'L'

    return 1 + change_clouds(arr, col + 1, row) + change_clouds(arr, col - 1, row) \
           + change_clouds(arr, col, row + 1) + change_clouds(arr, col, row - 1)


def count_islands(arr, col, row):
    """
    Counts the islands that are present in the area.
    """
    # Checks to see if the position is valid and if it is a land
    if col >= cols or row >= rows or col < 0 or row < 0 or arr[row][col] != 'L':
        return 0

    arr[row][col] = 'V'

    return 1 + count_islands(arr, col + 1, row) + count_islands(arr, col - 1, row) \
           + count_islands(arr, col, row + 1) + count_islands(arr, col, row - 1)


if __name__ == '__main__':
    # Input
    line = input().split()
    rows = int(line[0])
    cols = int(line[1])
    arr = [['' for c in range(cols)] for r in range(rows)]
    for r in range(rows):
        line = input()
        for c in range(cols):
            arr[r][c] = line[c]
    # Change the Clouds to Land if they are touching land
    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == 'L':
                arr[r][c] = 'C'
                change_clouds(arr, c, r)

    counts = []
    # Counts the area of the islands that are present in the array
    for i in range(rows):
        for x in range(cols):
            if arr[i][x] == 'L':
                counts.append(count_islands(arr, x, i))
    count2 = 0
    # Gets the amount of islands that are bigger than 1.
    for x in counts:
        if x > 0:
            count2 += 1
    # Print the amount of islands
    print(count2)
