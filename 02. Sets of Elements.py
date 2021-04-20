numbers = input().split()
n = int(numbers[0])
m = int(numbers[1])


first = set()
second = set()
uniques = set()
for num1 in range(n):
    numb = int(input())
    first.add(numb)
for num2 in range(m):
    numb = int(input())
    second.add(numb)
for el in first:
    if el in second:
        uniques.add(el)
for _ in uniques:
    print(_)