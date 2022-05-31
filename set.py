"""
:Problem: Set!
:Authors: Stuart Harley, Hayden Klein, Brendan Ecker
"""

list = []

for i in range(4):
    line = input().split()
    for x in line:
        num = x[0]
        symbol = x[1]
        fill = x[2]
        color = x[3]
        list.append((num, symbol, fill, color))

openList = []
for i in range(len(list)):      # 3 nested for loops check every combination of 3 cards
    for x in range(len(list)):
        for j in range(len(list)):
            count = 0
            f = list[i]
            s = list[x]
            t = list[j]
            if i != x and x != j and i != j:        # Check to make sure none of the cards are the same card
                # The following if statements check if each component is the same or pairwise different for all 3 cards
                if (f[0] == s[0] and f[0] == t[0]) or (f[0] != s[0] and f[0] != t[0] and s[0] != t[0]):
                    if (f[1] == s[1] and f[1] == t[1]) or (f[1] != s[1] and f[1] != t[1] and s[1] != t[1]):
                        if (f[2] == s[2] and f[2] == t[2]) or (f[2] != s[2] and f[2] != t[2] and s[2] != t[2]):
                            if (f[3] == s[3] and f[3] == t[3]) or (f[3] != s[3] and f[3] != t[3] and s[3] != t[3]):
                                so = sorted((i + 1, x + 1, j + 1))  # sort by card number so duplicates aren't added
                                if so not in openList:
                                    openList.append(so)

if len(openList) == 0:
    print("no sets")
else :
    for x in openList:
        print(x[0], x[1], x[2])