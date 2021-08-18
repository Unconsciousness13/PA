from collections import deque

working_bees = [int(b) for b in input().split()]
nectar = [int(n) for n in input().split()]
working_bees = deque(working_bees)
nectar = deque(nectar)

symbols = input()
reformat_symbols = deque()
result = 0

for el in symbols:
    if not el == chr(32):
        reformat_symbols.append(el)

while working_bees and nectar:
    sum = 0
    if nectar[-1] >= working_bees[0]:
        operator = reformat_symbols.popleft()
        if operator == "/" and working_bees == 0:
            continue
        sum += abs(eval(f"{working_bees[0]} {operator} {nectar[-1]}"))
        result += abs(sum)
        working_bees.popleft()
        nectar.pop()
    else:
        nectar.pop()

print(f"Total honey made: {result}")
if working_bees:
    print(f"Bees left: {', '.join([str(el) for el in working_bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(el) for el in nectar])}")