# Popularity Contest Solution
# Authors: Stuart Harley, Hayden Klein, Brendan Ecker

first_line = input().split()
friends = int(first_line[0])
friendships = int(first_line[1])

count_list = [0] * friends

for x in range(friendships):
    current = input().split()
    count_list[int(current[0])-1] = count_list[int(current[0])-1] + 1
    count_list[int(current[1])-1] = count_list[int(current[1])-1] + 1

ret = ""
for x in range(friends):
    ret = ret + str(count_list[x] - (x+1)) + " "
print(ret)