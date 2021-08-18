def fill_the_box(*args):
    size_of_the_box = args[0] * args[1] * args[2]
    sum = 0
    for el in range(len(args)):
        if args[el] == "Finish":
            break
        if el > 2:
            sum += int(args[el])
    if size_of_the_box - sum > 0:
        return f"There is free space in the box. You could put {size_of_the_box - sum} more cubes."
    return f"No more free space! You have {abs(size_of_the_box - sum)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
