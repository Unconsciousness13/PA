from collections import deque
numbers = [int(x) for x in input().split()]
queue = deque()
for n in range(len(numbers)):
    queue.append(numbers.pop())
print(*queue)
