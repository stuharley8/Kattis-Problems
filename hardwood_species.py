"""
:Problem: Hardwood Species
:Author: Stuart Harley
"""
from sys import stdin

total = 0.0
treeMap = {}

for tree in stdin:
    if treeMap.get(tree) is not None:       # Check if tree is already in dictionary
        treeMap[tree] = treeMap[tree] + 1   # Increment count of that tree if it exists
    else:
        treeMap[tree] = 1                   # Add the new tree to the dict and set the count to 1
    total = total + 1

for key in sorted(treeMap.keys()):          # Loops through the keys sorted alphabetically
    print(key, round(treeMap[key]/total * 100, 6))  # Print out the Trees and their percentages of occurrences
