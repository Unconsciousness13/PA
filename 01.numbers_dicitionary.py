numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
        line = input()
        if line == "Search":
            number = input()
            try:
                if number in numbers_dictionary:
                    print(numbers_dictionary[number])
            except:
                print("Number does not exist in dictionary")
                break
    except ValueError:
        print("The variable number must be an integer")
        print(numbers_dictionary)
        exit()

while line != "Remove":
    if line == "End":
        break
    searched = line
    num = input()
    if num == "Remove":
        line = input()
        try:
            del numbers_dictionary[line]
        except:
            print("Number does not exist in dictionary")
            break

    line = input()
while line != "End":
    line = input()

print(numbers_dictionary)
