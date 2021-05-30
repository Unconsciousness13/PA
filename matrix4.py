n = int(input())
matrix = [[list(n) for n in input().split(", ")] for _ in range(n)]
result = None
searched_symbol = input()
s_i = None
for el in range(len(matrix)):

    for index in matrix[el]:
        if searched_symbol in index:
            s_i = index.index(searched_symbol)
            result = (f"({el}, {s_i})")
            print(result)
            if result:
                break
            else:
                continue
        if result:
            break
    if result:
        break
if not result:
    print(f"{searched_symbol} does not occur in the matrix")
