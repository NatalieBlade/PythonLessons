import json

nums = [4, 76, 58, 5, 95, 21, 31, 8]

filename = 'nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f) #записывает список в файл nums.json

file = 'nums.json' #обращаемся к файлу
with open(file) as fl: #открываем файл
    nums_new = json.load(fl)

print(nums_new)