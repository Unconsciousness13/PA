text = input()

symbols = {}

for char in text:
    symbols[char] = text.count(char)
sorted_char = sorted(symbols.items(), key=lambda x: x[0])
for _ in sorted_char:
    print(f'{_[0]}: {_[1]} time/s')