#Функции

#print(1232) #print - название функции, в скобках аргумент(ы)
#int() #приводит число с плавающей точкой в целое число
#input() #ввод данных от пользователя
#создание функции
def some():
    print("some")

#some() #вызываем созданную функцию

# def bitcoinToUsd(btc, course):
#     amount = btc * course
#     print(amount)
#
# bitcoinToUsd(4, 8520)

def bitcoinToUsd(btc, course):
    amount = btc * course
    print(amount)

bitcoinToUsd(round(4.6), 8520)

print(round(4.6))

