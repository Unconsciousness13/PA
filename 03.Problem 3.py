def flights(*args):
    result = {}
    for arg in range(len(args)):
        if args[arg] == "Finish":
            break
        if arg % 2 == 0:
            if args[arg] not in result:
                result[args[arg]] = 0
            flight = args[arg]
        else:
            pas = args[arg]
            result[flight] += pas
    return result


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
