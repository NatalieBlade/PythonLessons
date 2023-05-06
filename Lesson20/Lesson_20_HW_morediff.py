f = open('dialogue/fileWithText.txt', 'w')
f.write('Who wants\n')
f.write('to live forever?')
f.close()

fr = open('dialogue/fileWithText.txt', 'r')
text = fr.read()
fr.close()

print(text)

fr = open('dialogue/fileWithText.txt', 'r')
count = 0
for line in fr:
    count = count+1

print(count)

# fr = open('dialogue/fileWithText.txt', 'r')
# countElem = 0
# for element in fr:
#     count = count+1
#
# print(countElem)

fr = open('dialogue/fileWithText.txt', 'r')
text = fr.read()
syms = len(text) - text.count(" ")
print(syms)
from collections import Counter
#count2 = sum(c != " " for c in fr)
#print(count2)
# def count_letters(fr):
#     BAD_LETTERS = " "
#     return len([letter for letter in fr if letter not in BAD_LETTERS])
# fr = open('dialogue/fileWithText.txt', 'r')
# count_letters(fr)
    #counter = Counter()
#element = 0
#for letter in fr:
    #element = element+1
    #return int(count)
#elements = open('dialogue/fileWithText.txt', 'r')
#count_letters(letters)

#print(element)

# with open('dialogue/fileWithText.txt', 'r') as x:
#     for line in x:
#         print(line)

# fr = open('dialogue/fileWithText.txt', 'rt')
#
# num_lines = len(fr.splitlines())
# num_words = 0
# num_chars = 0
# for line in num_lines:
#     num_words +=len(line.split())
#     #for word in line:
#         #fr+=int(len(line))
# print(fr)
