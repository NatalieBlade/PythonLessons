from calc import calculator

def count_input():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    symb = input("Что делаем? +, -, *, /. \nЕсли ничего - то введите символ 'Q':\n")
    if symb:
        res = calculator(a, b)
    else:
        res = calculator(a, b, symb)
    print(res)

count_input()