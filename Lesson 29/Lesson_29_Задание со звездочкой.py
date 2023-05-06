from collections import Counter

text = input('Напечатай любой текст:  ')

words = open('some.txt', 'w')
words.write(text)

word_list = []

for word in text.split(): #в word записываем каждое отдельное слово из text
    clear_word = "" #переменная, в которую будем записывать только буквы
    for letter in word:
        if letter: #если символ является алфавитом
            clear_word += letter.lower() #то мы записываем его в clear_word
    word_list.append(clear_word) #затем добавляем слово в список при помощи append из clear_word
    clear_symbol = ""
    for symbol in text.split():
        if symbol == ".":
            clear_symbol += symbol
    word_list.append(clear_symbol)

print(Counter(word_list))

words.close()