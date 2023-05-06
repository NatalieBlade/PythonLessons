def calculator(a, b, symb=''):
    if symb == "+":
        res = int(a + b)
    elif symb == "-":
        res = int(a - b)
    elif symb == "*":
        res = int(a * b)
    elif symb == "/":
        res = int(a / b)
    else:
        res = a + b
    return res

#print(calculator(40, 10, "/"))