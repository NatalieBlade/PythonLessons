# def calorie_calculator(name, get_calorie, spend_calorie):
#     if get_calorie > spend_calorie:
#         msg = name + " is getting fat"
#     else:
#         msg = name + " is losing weight"
#     return msg
#
# person = ["Inna", 1800, 1200]
#
# print(calorie_calculator(*person))
# print(calorie_calculator("Natalia", 1900, 1950))

def some (*args): #любое количество аргументов
    result = 0
    for f in args:
        result += f
        num = len(args)
    print(result, num)

some (3, 12)
some (3, 12, 15)
some (3, 12, 15, 30)