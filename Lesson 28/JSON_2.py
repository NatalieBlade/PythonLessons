import json

def get_username():
    """Получает имя пользователя, если оно есть"""
    filename = 'user.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user

def greet_user():
    """Приветствие пользователя"""
    username = get_username()
    if username:
        print("Добро пожаловать, " + username + "!")
    else:
        username = input("Введите ваше имя: ")
        filename = 'user.json'
        with open(filename, 'w', encoding="utf-8") as fl:
            json.dump(username, fl, ensure_ascii=False)
            print("Мы запомним ваше имя, как " + username + "!")


greet_user()

# username = input("Введите ваше имя: ")
#
# filename = 'user.json'
# with open(filename, 'w', encoding="utf-8") as fl:
#     json.dump(username, fl, ensure_ascii=False)
#     print("Мы запомним ваше имя, как " + username + "!")

#Для восприятия кириллицы: encoding="utf-8" и ensure_ascii=False

# with open(filename) as f:
#     user = json.load(f)
#     print("Добро пожаловать, " + user + "!")