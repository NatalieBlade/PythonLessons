class User():
    def __init__(self, first_name, last_name, age, hobby, favourite_music):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.favourite_music = favourite_music

    def describe_user(self):
        print(self.first_name + ", " + self.last_name + ", " + self.age + ", " + self.hobby + ", " + self.favourite_music)

    def greet_user(self):
        print("Добрый день, " + self.last_name + "!")

user = User("Иванов", "Сергей", "16 лет", "Плавание", "Реп")
user_2 = User("Игнатова", "Анна", "19 лет", "Вокал", "Поп-музыка")
user_3 = User("Сидоров", "Андрей", "18 лет", "Баскетбол", "Рок")
user_4 = User("Гвоздиков", "Олег", "19 лет", "Футбол", "Реп")
user_5 = User("Антонова", "Елена", "15 лет", "Компьютерные игры", "Поп-музыка")

user.describe_user()
user.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

user_4.describe_user()
user_4.greet_user()

user_5.describe_user()
user_5.greet_user()