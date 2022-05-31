# Hailstone Sequence Solution
# Authors: Stuart Harley, Hayden Klein, Brendan Ecker

num = int(input())      # num is the current number in the sequence
length = 1              # length is the current length of the sequence
while num != 1:         # loops through until the number 1 is added to the sequence
    if num%2 == 0:      # If the current number is even, the next num is calculated to be num/2
        num = num/2
    else:               # If the current number is odd, the next num is calculated to be 3*num+1
        num = 3*num + 1
    length = length + 1
print(length)