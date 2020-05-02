import math

start = 0
step = 1
stop = 5
top_wall = [(min(n+step-1, stop), start) for n in range(start, stop+1, step)]


start = 0
step = 1
stop = 5
left_wall = [(start, min(n+step-1, stop)) for n in range(start, stop+1, step)]

start = 0
step = 1
stop = 5
right_wall = [(stop, min(n+step-1, stop)) for n in range(start, stop+1, step)]

start = 0
step = 1
stop = 5
bottom_wall = [(min(n+step-1, stop), stop) for n in range(start, stop+1, step)]

head = (0,4)
print(head in top_wall)
print(head in bottom_wall)
print(head in right_wall)
print(head in left_wall)
# print((5,4) in left_wall or right_wall or bottom_wall or top_wall)
print(top_wall)
print(bottom_wall)
print(right_wall)
print(left_wall)


