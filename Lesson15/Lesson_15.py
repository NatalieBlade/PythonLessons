# def gender(sex="Unknown"): #в скобках значение по-умолчанию
#     if sex =="m":
#         sex = "Male"
#     elif sex == "f":
#         sex = "Female"
#     # else:
#     #     sex = "Unknown"
#     return sex
#
# print(gender())
# print(gender("f"))

some = 111 #some - глобальная переменная (можем использовать ее как внутри, так и снаружи функции)

def var1():
    some = 121 #локальная переменная (можем использовать только внутри функции)
    print(some)

def var2():
    print(some)

var1()
var2()

print (some)