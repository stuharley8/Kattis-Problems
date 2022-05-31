"""
:Problem: Supercomputer
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""


class SegmentTreeArray:
    """
    Class implements a segment tree with an underlying array data structure
    """
    def __init__(self, num_bits):
        """
        Constructor. Makes an array of size num_bits * 2 to represent the segment tree
        :param num_bits: the number of leaf nodes in the segment tree
        """
        self.tree = [0] * (num_bits * 2)
        self.num_bits = num_bits

    def update(self, index):
        """
        Flips the bit at the specified index. Updates the counts of the appropriate parent indexes
        :param index: the bit to be flipped (1 to 0, or 0 to 1)
        """
        temp_index = index + self.num_bits
        if self.tree[temp_index] == 0:
            self.tree[temp_index] = 1
        else:
            self.tree[temp_index] = 0
        while temp_index > 1:
            if temp_index % 2 == 0:
                self.tree[int(temp_index/2)] = self.tree[temp_index] + self.tree[temp_index + 1]
            else:
                self.tree[int(temp_index/2)] = self.tree[temp_index] + self.tree[temp_index - 1]
            temp_index = int(temp_index / 2)

    def query(self, l, r):
        """
        Calculates and prints the count of all 1 bits between some left and right bounds
        :param l: the left index bound
        :param r: the right index bound
        """
        sum = 0
        temp_left = l + self.num_bits
        temp_right = r + self.num_bits + 1

        while temp_left < temp_right:
            if temp_left % 2 == 1:
                sum = sum + self.tree[temp_left]
                temp_left = temp_left + 1
            if temp_right % 2 == 1:
                temp_right = temp_right - 1
                sum = sum + self.tree[temp_right]
            temp_left = int(temp_left / 2)
            temp_right = int(temp_right / 2)
        print(sum)


line = input().split()
bits = int(line[0])
queries = int(line[1])

tree = SegmentTreeArray(bits)       # Create the segment tree array with the specified number of bits
for i in range(queries):
    query = input().split()
    if query[0] == 'F':                 # Flip a specified bit
        tree.update(int(query[1])-1)
    else:                               # Get a count of the 1 bits between the left and right bounds
        tree.query(int(query[1])-1, int(query[2])-1)
