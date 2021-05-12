numbers = [int(num) for num in input().split(", ")]
negative = [n for n in numbers if n < 0]
positive = [n for n in numbers if n >= 0]
even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if not n % 2 == 0]
p = (", ".join([str(n) for n in positive]))
n = (", ".join([str(n) for n in negative]))
e = (", ".join([str(n) for n in even]))
o = (", ".join([str(n) for n in odd]))
print(f'Positive: {p}')
print(f'Negative: {n}')
print(f'Even: {e}')
print(f'Odd: {o}')