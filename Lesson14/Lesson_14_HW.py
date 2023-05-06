def calc(first, second, symbol):
    if symbol == "+":
        return first+second
    elif symbol == "-":
        return first-second
    elif symbol == "*":
        return first*second
    elif symbol == "/":
        if second > first:
            print("Warning!")
        else:
            return first/second
print(calc(30, 5, "/"))