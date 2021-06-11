def stock_availability(*args):
    products = args[0]
    command = args[1]
    if command == "delivery":
        for flavour in args[1:]:
            for n in range(args.index('delivery') + 1, len(args)):
                products.append(args[n])
            return products

    elif command == "sell":
        if len(args) == 2:
            products.pop(0)

        if isinstance(args[-1], int):
            number = int(args[-1])
            return products[number:]
        if isinstance(args[-1], str):
            cupcakes = args[int(args.index("sell") + 1):]
            for sweet in cupcakes:
                products = [i for i in products if not i == sweet]
            return products

    return products


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
