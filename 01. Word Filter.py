words = input().split()
selected = [x for x in words if len(x) % 2 == 0]
for w in selected:
    print(w)