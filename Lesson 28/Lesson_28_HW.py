import json

# favNum = input("Введите ваше любимое число: ")
#
# num = 'number.json'
# with open(num, 'w', encoding="utf-8") as f:
#     json.dump(favNum, f, ensure_ascii=False)
#     print("Я знаю ваше любимое число! Это " + favNum + "!")

def get_number():
    """Получает любимое число пользователя, если оно есть"""
    num = 'number.json'
    try:
        with open(num) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number

def give_number():
    favNum = get_number()
    if favNum:
        print("Я знаю ваше любимое число! Это " + favNum + "!")
    else:
        favNum = input("Введите ваше любимое число: ")
        num = 'number.json'
        with open(num, 'w', encoding="utf-8") as fl:
            json.dump(favNum, fl, ensure_ascii=False)
            print("Мы запомним ваше любимое число, как " + favNum + "!")

give_number()