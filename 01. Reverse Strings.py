text = input()
elements = []
for char in text:
    elements.append(char)
reverseda = ''
while len(elements) > 0:
    letter = elements.pop()
    reverseda += letter
print(reverseda)