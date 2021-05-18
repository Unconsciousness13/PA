def concatenate(*args):
    result = ''
    for arg in args:
        result += arg
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
