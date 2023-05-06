# Классы (метод в классе - это обычная функция)

class Dog(): #создали класс с именем Dog
    """Простая модель собаки"""

    def __init__(self, name, age): #пераметр self обязателен при создании любого метода
        """инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        #print("Собака создана")

    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + " сел")

    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " прыгнул")

    def bark(self):
        """Собака будет лаять по команде"""
        print("гав-гав")

#создаем объект по инструкции (экземпляр класса)
my_dog = Dog("Топик", 4) #метод init автоматически вызывается при записи этой стороки
my_dog_2 = Dog("Nick", 7)
mike = Dog('Mike', 7)
print(my_dog.age)
print(my_dog.name)

my_dog.jump()
my_dog_2.sit()
mike.bark()