def var(*args):
    result = 1
    for arg in args:
        result *= arg
        num = len(args)
    return result, num

print(var(8, 9, 10))