#Запись в файл

# f = open('Assets/some.txt', 'a')
# f.write('Some text\n')
# f.write('1\n')
# f.close()


#str = input('Напечатай любой текст:  ')

#f = open('Assets/some1.txt', 'w')
#f.write(str)
#f.close()


#f = open('Assets/some1.txt', 'w')
#f.write('Start\n')
#f.write('1\n')
#f.close()

#Чтение файла

#fr = open('Assets/some.txt', 'r')
#text = fr.read()
#fr.close()

#print(text)

#Режимы можно комбинировать?

#fr = open('Assets/some.txt', 'rt')
#text = fr.read()
#fr.close()

#print(text)

#Можно ограничить количество считываемых символов

#fr = open('Assets/some.txt', 'r')
#text = fr.read(12)
#fr.close()

#print(text)

#Чтение текста построчно или работа с каждой строкой отдельно

fr = open('Assets/some.txt', 'r')

for line in fr:
    print(line)
fr.close()

