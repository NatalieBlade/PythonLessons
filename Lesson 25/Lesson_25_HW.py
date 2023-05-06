# Производство столов

class Table():
    """Класс по созданию письменного стола"""
    def __init__(self, name, color, height, width, material, purpose):
        """Инициализация атрибутов стола"""
        self.name = name
        self.color = color
        self.height = height
        self.width = width
        self.material = material
        self.purpose = purpose
        self.number_of_tables = 0

    def description_table(self):
        """Возвращаем описание стола"""
        desc = self.color + " " + self.purpose + " " + self.name + " стол" + ", высота " + str(self.height) + " см, ширина " + str(self.width) + " см, материал: " + self.material
        return desc.title()

    def tables_number(self):
        """Выводим количество изготовленных столов"""
        print("На данный момент изготовлено " + str(self.number_of_tables) + " столов")

    def num_tables(self, units):
        """Устанавливаем количество столов"""
        if units >= self.number_of_tables:
            self.number_of_tables = units
        else:
            print("Кажется не хватает столов")

    def increment_tables(self, units):
        """Увеличиваем количество столов на заданную величину"""
        if units > 0:
            self.number_of_tables += units
        else:
            print("Так быстро раскупают!")

    def sale_tables(self, units):
        """Продаем столы"""
        if units > 0:
            self.number_of_tables -= units
        else:
            print("Нельзя продать отрицательное количество столов")

newtable = Table("Неополитанский", "Коричневый", 80, 120, "деревянный", "письменный")

print(newtable.description_table())

newtable.number_of_tables = 12
newtable.num_tables(14)
newtable.increment_tables(12)
print(newtable.number_of_tables)

newtable.sale_tables(7)
print(newtable.number_of_tables)
newtable.tables_number()