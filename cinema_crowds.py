# Cinema Crowds Solution
# Authors: Stuart Harley, Hayden Klein, Brendan Ecker

first_line = input().split()
seats = int(first_line[0])
groups = int(first_line[1])

second_line = input().split()
count = 0
let_in = 0
for i in range(groups):
    count = count + int(second_line[i])
    if count > seats:
        count = count - int(second_line[i])
    else:
        let_in = let_in + 1
print(groups - let_in)