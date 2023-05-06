# Исключения try, except

a = 100
b = 0

try:
    c = a/b
except ZeroDivisionError:
    c = 0
    print('Ошибка в делении')
    print('Переменная a =', a)
    print('Переменная b =', b)

print(c)

# a = 100
# b = '12'
# c = a/b
#
# print(c)

