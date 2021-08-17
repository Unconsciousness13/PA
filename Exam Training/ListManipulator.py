from collections import deque


def list_manipulator(*args):
    numbers = []
    for index in range(len(args)):
        if index > 2:
            numbers.append(args[index])
    lista = deque(args[0])
    first = args[1]
    second = args[2]
    if first == "add":
        if second == "beginning":
            lista.appendleft(numbers)
        if second == "end":
            lista.append(numbers)

    elif first == "remove":
        if second == "beginning":
            if len(args) > 3:
                for index in range(2, len(args)):
                    lista.popleft()
            else:
                lista.popleft()
        if second == "end":
            if len(args) > 3:
                for index in range(args[3]):
                    lista.pop()
            else:
                lista.pop()
    final_result = []
    for el in lista:
        if isinstance(el,list):
            for el1 in el:
                final_result.append(el1)
        else:
            final_result.append(el)
    return final_result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
