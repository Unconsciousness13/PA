from collections import deque

males = deque([int(m) for m in input().split()])
females = deque([int(f) for f in input().split()])

matches = 0
while True:
    if not males:
        break
    if not females:
        break
    for idx in range(len(females)):
        if males[-1] <= 0:
            males.pop()
            break
        if females[idx] <= 0:
            females.popleft()
            break
        if males[-1] % 25 == 0:
            males.pop()
            males.pop()
            break

        elif females[idx] % 25 == 0:
            females.popleft()
            females.popleft()
            break
        if females[idx] == males[-1]:
            matches += 1
            males.pop()
            females.popleft()
            break
        else:
            females.popleft()
            males[-1] -= 2
            break

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    top = males.reverse()
    print(f"Males left: {', '.join([str(el) for el in males])}")
if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(list(map(str, females)))}")
