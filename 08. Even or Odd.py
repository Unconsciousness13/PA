def even_odd(*args):
    for arg in args:
        if arg == "even":
            result = [int(el) for el in args[:-1] if el % 2 == 0]
            return result
        if arg == "odd":
            result = [int(el) for el in args[:-1] if not el % 2 == 0]
            return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))