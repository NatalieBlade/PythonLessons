
#h = input('Привет! Как дела?:  ')

#if h == "Хорошо!":
    #print("Отлично!")
#else:
    #print("Тоже хорошо!")

#f = open('dialogue/dialog.txt', 'w')
#f.write(h)
#f.close()

f1 = input('Введите вопрос:  ')
print(f1)
f2 = input('Введите ответ:  ')
print(f2)
f3 = input('Введите вопрос:  ')
print(f3)
f4 = input('Введите ответ:  ')
print(f4)

f = open('dialogue/dialog.txt', 'w')
f.write(f1+"\n"+f2+"\n"+f3+"\n"+f4+"\n")
f.close()
