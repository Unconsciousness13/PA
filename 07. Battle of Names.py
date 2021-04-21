n = int(input())

even_numbers_set = set()
odd_numbers_set = set()

for current_iteration_count in range(1, n + 1):
    name = input()
    current_sum = sum([ord(el) for el in name]) // current_iteration_count

    if current_sum % 2 == 0:
        even_numbers_set.add(current_sum)
    else:
        odd_numbers_set.add(current_sum)

sum_evens = sum(even_numbers_set)
sum_odd = sum(odd_numbers_set)

if sum_evens == sum_odd:
    modified_set = [str(el) for el in even_numbers_set.union(odd_numbers_set)]
    print(f"{', '.join(modified_set)}")
elif sum_evens < sum_odd:
    modified_set = [str(el) for el in odd_numbers_set.difference(even_numbers_set)]
    print(f"{', '.join(modified_set)}")
elif sum_evens > sum_odd:
    modified_set = [str(el) for el in even_numbers_set.symmetric_difference(odd_numbers_set)]
    print(f"{', '.join(modified_set)}")
