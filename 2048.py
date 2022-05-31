"""
:Problem: 2048
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""

# An Inplace function to rotate N x N matrix by 90 degrees in counter-clockwise direction
def rotateMatrixCCW(mat):
    # reversing the matrix
    for i in range(len(mat)):
        mat[i].reverse()
    # make transpose of the matrix
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            # swapping mat[i][j] and mat[j][i]
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


# An Inplace function to rotate N x N matrix by 90 degrees in clockwise direction
def rotateMatrixCW(mat):
    # make transpose of the matrix
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            # swapping mat[i][j] and mat[j][i]
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # reversing the matrix
    for i in range(len(mat)):
        mat[i].reverse()


board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

for i in range(4):          # Use input to fill in board values
    line = input().split()
    for j in range(4):
        board[i][j] = int(line[j])

move = int(input())         # 0 means left, 1 means up, 2 means right, 3 means down

for rotate in range(move):  # Rotate the board so we always move the pieces left
    rotateMatrixCCW(board)

for i in range(4):          # For each row of the board, perform combinations and then shifts to the left
    if board[i][0] == board[i][1]:          # Check if first 2 squares can be combined
        board[i][0] = board[i][0] * 2
        board[i][1] = 0
        if board[i][2] == board[i][3]:      # Check if 3rd and 4th square can be combined
            board[i][2] = board[i][2] * 2
            board[i][3] = 0
    elif board[i][0] == board[i][2] and board[i][1] == 0:        # Check if 1st and 3rd squares can be combined
        board[i][0] = board[i][0] * 2
        board[i][2] = 0
    elif board[i][0] == board[i][3] and board[i][1] == 0 and board[i][2] == 0:        # Check if 1st and 4th squares can be combined
        board[i][0] = board[i][0] * 2
        board[i][3] = 0
    elif board[i][1] == board[i][2]:        # If not check if 2nd and 3rd square can be combined
        board[i][1] = board[i][1] * 2
        board[i][2] = 0
    elif board[i][1] == board[i][3] and board[i][2] == 0:        # Check if 2nd and 4th squares can be combined
        board[i][1] = board[i][1] * 2
        board[i][3] = 0
    elif board[i][2] == board[i][3]:        # If not check if 3rd and 4th square can be combined
        board[i][2] = board[i][2] * 2
        board[i][3] = 0
    for x in range(3):
        if board[i][0] == 0:                    # Shift 2nd square to 1st if 1st is zero
            board[i][0] = board[i][1]
            board[i][1] = 0
        if board[i][1] == 0:                    # Shift 3rd square to 2nd if 2nd is zero
            board[i][1] = board[i][2]
            board[i][2] = 0
        if board[i][2] == 0:                    # Shift 4th square to 3rd if 3rd is zero
            board[i][2] = board[i][3]
            board[i][3] = 0

for rotate in range(move):  # Rotate the board back to its original orientation
    rotateMatrixCW(board)

for i in range(4):
    print(board[i][0], board[i][1], board[i][2], board[i][3])
