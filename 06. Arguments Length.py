def args_length(*args):
    total_length = 0
    for arg in args:
        total_length += 1
    return total_length


print(args_length("john", "peter"))
