def list_manipulator(*args):
    nums = args[0]
    if args[1] == "add":
        if args[2] == "beginning":
            count = 0
            for num in range(3, len(args)):
                nums.insert(count, args[num])
                count += 1
        elif args[2] == "end":
            for num in range(3, len(args)):
                nums.append(args[num])
    elif args[1] == "remove":
        if len(args) > 3:
            s = args[3]
            s = int(s)
            if args[2] == "beginning":
                for i in range(s):
                    nums.pop(0)
            elif args[2] == "end":
                for i in range(s):
                    nums.pop()

        else:
            if args[2] == "beginning":
                nums = nums[1:]
            elif args[2] == "end":
                nums = nums[:-1]

    return nums


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
