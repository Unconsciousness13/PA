# result = [' '.join(list_as_string.split()) for list_as_string in input().split('|')[::-1]]
# print(*result)
result = input().split("|")[::-1]
final = [value.strip() for i in range(len(result)) for value in result[i].split()]
print(*final)