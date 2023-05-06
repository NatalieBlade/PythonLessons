#ТЕСТИРОВАНИЕ В PYTHON

def full_name(first, last, middle=''): #middle='' необязательный параметр
    """Отдает полное имя и фамилию пользователя"""
    if middle:
        full = first + ' ' + last + ' ' + middle
    else:
        full = first + ' ' + last
    return full.title()

# print(full_name("Наталья", "Ким"))