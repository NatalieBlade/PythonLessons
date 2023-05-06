import json

def get_username():
    """Получает имя пользователя, если оно есть"""
    filename = 'user.json'
    try:
        with open(filename, encoding="utf-8", errors='ignore') as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user

def greet_user():
    """Приветствие пользователя"""
    username = get_username()
    x = input("Это ваше имя: " + username + "?")
    if x == "Да":
        print("Добро пожаловать, " + username + "!")
    elif x == "Нет":
        get_new_username()
    #else:
        #username = input("Введите ваше имя: ")
        #filename = 'user.json'
        #with open(filename, 'w', encoding="utf-8") as fl:
            #json.dump(username, fl, ensure_ascii=False)
            #print("Мы запомним ваше имя, как " + username + "!")

def get_new_username():
    """Получение правильного имени пользователя"""
    new_name = input("Введите ваше настоящее имя: ")
    filename = 'user.json'
    with open(filename, 'w', encoding="utf-8", errors='ignore') as fx:
        json.dump(new_name, fx, ensure_ascii=False)
        print("Мы запомним ваше имя, как " + new_name + "!")

greet_user()