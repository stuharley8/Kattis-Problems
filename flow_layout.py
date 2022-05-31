# Flow Layout Solution
# Authors: Stuart Harley, Hayden Klein, Brendan Ecker

while True:
    max_width = int(input())
    if max_width == 0:
        break
    final_width = 0
    final_height = 0
    row_width = 0
    row_height = 0
    while True:
        next_line = input().split()
        block_width = int(next_line[0])
        block_height = int(next_line[1])
        if block_height and block_width == -1:
            break
        if max_width < block_width + row_width:  # Checks if adding a new block would exceed the limit
            if final_width < row_width:          # If true it adds to the totals accordingly and resets the row metrics
                final_width = row_width
            final_height = final_height + row_height
            row_height = 0
            row_width = 0
        row_width = row_width + block_width      # Adds the block to the current row by updating the row's metrics
        if block_height > row_height:
            row_height = block_height
    if final_width < row_width:                  # Adds the last row's metrics to the totals
        final_width = row_width
    final_height = final_height + row_height
    print(str(final_width) + " x " + str(final_height))
