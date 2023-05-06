#модули

import some
import os #модуль из библиотеки python
import random

x = random.randrange(1, 100) #генерирует случайное число
print(x)

info = os.getcwd() #текущее положение файлов,с которыми мы работаем
print(info)

some.func()