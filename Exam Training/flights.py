def flights(*args):
    result = {}
    flight = None
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

