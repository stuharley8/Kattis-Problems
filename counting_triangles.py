"""
:Problem: Counting Triangles
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""


# Checks to see if two line segments are intersecting. Using dot and cross product.
def intersects(s0, s1):
    # Gets the 4 determinants of the "matrix"
    dx0 = s0[1][0] - s0[0][0]
    dx1 = s1[1][0] - s1[0][0]
    dy0 = s0[1][1] - s0[0][1]
    dy1 = s1[1][1] - s1[0][1]
    # Dot products of the determinants and the difference of the line segments.
    p0 = dy1 * (s1[1][0] - s0[0][0]) - dx1 * (s1[1][1] - s0[0][1])
    p1 = dy1 * (s1[1][0] - s0[1][0]) - dx1 * (s1[1][1] - s0[1][1])
    p2 = dy0 * (s0[1][0] - s1[0][0]) - dx0 * (s0[1][1] - s1[0][1])
    p3 = dy0 * (s0[1][0] - s1[1][0]) - dx0 * (s0[1][1] - s1[1][1])
    # Checks if the lines are crossing
    return (p0 * p1 <= 0) & (p2 * p3 <= 0)


num = int(input())
# Get the number of lines coming up. Stop if zero lines coming
while num != 0:

    # The lines that we are given
    lines = []

    # The triangles that have been found
    tri = []

    # All the intersecting lines for each line.
    # IE 3 lines line 1 and 2 intersect and line 2 and 3 intersect [ [2], [1,3], [2] ]
    intr = []
    # set up intr with empty lists
    for i in range(num):
        intr.append([])
    count = 0
    # Go through all the lines given and check if they intersect we any other lines
    for i in range(num):
        line = input().split()
        lines.append((float(line[0]), float(line[1]), float(line[2]), float(line[3])))
        # Checks if there is any line to check if they intersect
        if len(lines) > 1:
            # Go through all the previous lines to see if the current line intersects with them
            for x in range(len(lines) - 1):
                temp = lines[x]
                """If the two lines intersect add the index of the lines to the intersecting array to store these two 
                lines intersect """
                if intersects([(float(line[0]), float(line[1])), (float(line[2]), float(line[3]))],
                              [(temp[0], temp[1]), (temp[2], temp[3])]):
                    intr[x].append(i)
                    intr[i].append(x)
    # For each line see if the intersecting lines can make a triangle
    for i in range(len(lines)):
        # Go through all the line pairs that intersect line i
        for x in range(len(intr[i]) - 1):
            line1 = intr[i][x]
            for y in range(x, len(intr[i])):
                line2 = intr[i][y]
                """ Checks to see if line 2 intersects with line 1 if so the 
                current line, line 1, and line 2 for a triangle. """
                if line2 in intr[line1]:
                    # Make the triangle with ascending indices to keep track of
                    triangle = (i, line2, line1)
                    triangle = sorted(triangle)
                    # Checks to see if the triangle is already counted
                    if triangle not in tri:
                        tri.append(triangle)
                        count += 1
    print(count)
    num = int(input())
