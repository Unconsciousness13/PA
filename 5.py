from collections import deque
names = deque(input().split())
rotations = int(input())
while len(names) > 1:
    names.rotate(-rotations)
    print(f"Removed {names.pop()}")
print(f"Last is {names.popleft()}")

