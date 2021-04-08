numbers = input().split(' ')

output = []
while numbers:
    next_number = numbers.pop()
    output.append(next_number)
print(' '.join(output))
