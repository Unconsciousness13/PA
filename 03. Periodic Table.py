n = int(input())

uniques = set()
for el in range(n):
    elements = input()
    splited = elements.split(" ")
    for ele in splited:
        uniques.add(ele)
for _ in uniques:
    print(_)