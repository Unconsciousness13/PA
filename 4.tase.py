frase = input()
result = {}
for el in frase:
    result[el] = frase.count(el)
sorted_items = sorted(result.items(), key=lambda x: x[0])
for key,value in sorted_items:
    print(f"{key}: {value} time/s")