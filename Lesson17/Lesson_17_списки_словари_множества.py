#списки

lists = [123, "ghj", 12, 34, "some"]

#множества

#names = {"Ivan", "Irina", "Oleg", "Anna", "Sergey", "Irina", "Ivan"}
#множества не позволяют повтороений
# множества регистрозависимые
# print(len(names))

#словари (ключ:значение)

class_room = {"Ivan":"17", "Irina":"16", "Oleg":"16"}
# print(class_room)
# print(class_room["Oleg"])

for k, v in class_room.items():
    print(k, v)