"""
:Problem: Kitten on a Tree
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""
cat = int(input())

tree = [0] * 101            # Create an array to store the parent node numbers of each node
line = input().split()
while int(line[0]) != -1:
    for i in range(1, len(line)):
        tree[int(line[i])] = int(line[0])       # Store the parent of each node given in the array
    line = input().split()

path = [cat]

while tree[cat] != 0:       # Move from the location of the cat, to its parent node, repeating until reaching root
    cat = tree[cat]
    path.append(cat)        # Add each node visited to the path

print(*path)