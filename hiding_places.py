"""
:Problem: Hiding Places
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""

arr = [[6, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 6],           # array is a full array of all possible solutions
       [5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 5],
       [4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4],
       [5, 4, 3, 4, 3, 2 ,3, 2, 3, 2, 3, 4, 3, 4, 5],
       [4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4],
       [5, 4, 3, 2, 3, 4, 1, 2, 1, 4, 3, 2, 3, 4, 5],
       [4, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4],
       [5, 4, 3, 2, 3, 2, 3, 0, 3, 2, 3, 2, 3, 4, 5],
       [4, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4],
       [5, 4, 3, 2, 3, 4, 1, 2, 1, 4, 3, 2, 3, 4, 5],
       [4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4],
       [5, 4, 3, 4, 3, 2 ,3, 2, 3, 2, 3, 4, 3, 4, 5],
       [4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4],
       [5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 5],
       [6, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 6]]

sc = {'a':7, 'b':6, 'c':5, 'd':4, 'e':3, 'f':2, 'g':1, 'h':0}       # dict to convert starting column to col index

times = int(input())
for i in range(times):
    spot = input()
    row = int(spot[1])
    col = spot[0]
    start_row = row - 1             # calculates starting row in full array
    end_row = start_row + 7         # calculates ending row in full array
    start_col = sc.get(col)         # gets starting column for sc dictionary
    end_col = start_col + 7         # calculates ending column in full array
    max = 0
    for r in range(start_row, end_row+1):       # loops through every space in the row/column subarray for the max value
        for c in range(start_col, end_col+1):
            if arr[r][c] > max:
                max = arr[r][c]
    spots = []
    rcount = 9
    for r in range(start_row, end_row+1):       # loops through every space in the row/column subarray that equals max value
        rcount = rcount - 1
        ccount = 0
        for c in range(start_col, end_col+1):
            ccount = ccount + 1
            if arr[r][c] == max:
                spots.append(chr(ccount+96) + str(rcount))      # adds valid spots to the spots array
    prt = str(max)
    for spot in spots:                          # prints out the max value and valid spots
        prt = prt + " " + spot
    print(prt)
