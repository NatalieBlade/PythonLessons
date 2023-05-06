class Restaurant():
    def __init__(self, name, meals, drinks, open_hours, close_hours, workers):
        self.name = name
        self.meals = meals
        self.drinks = drinks
        self.open_hours = open_hours
        self.close_hours = close_hours
        self.workers = workers
        self.seats = 0

    def desc_rest(self):
        descRest = "Сегодня в меню в " + self.name + ": " + self.meals + " и " + self.drinks + ". Часы работы: с " + self.open_hours + " до " + self.close_hours + ", всего сотрудников: " + str(self.workers)
        print(descRest)

    def num_of_seats(self, num_tables):
        if num_tables >= 1:
            self.seats = num_tables * 4
            print(self.seats)
        else:
            print("Сколько у вас столов?")

    def working_hours(self, time):
        if time >= "08:00" and time <= "22:00":
            print("Ресторан открыт!")
        else:
            print("Закрыто! Ждем вас завтра!")

    def num_of_workers(self):
        x = input("Сколько сейчас времени? ")
        if x >= "08:00" and x <= "16:00":
            print("Сейчас в ресторане " + str(self.workers) + " сотрудников.")
        elif x > "16:00" and x <= "22:00":
            print("Сейчас в ресторане " + str(self.workers * 2) + " сотрудников.")
        else:
            print("Ресторан закрыт!")

class Kalyan_corner(Restaurant):
    def __init__(self, name, meals, drinks, open_hours, close_hours, workers, sort):
        """Инициализация атрибутов класса родителя"""
        super().__init__(name, meals, drinks, open_hours, close_hours, workers)
        self.sort = sort

    def order(self):
        print("Я хочу заказать кальян")
        f = input("А сколько вам лет? ")
        if f >= "18":
            print("Хорошо, заказ принят")
        else:
            print("Простите, только для совершеннолетних")

my_corner = Kalyan_corner('"У Марио"', "Японские блюда", "свежевыжатый сок", "08:00", "22:00", 15, "Konoplya")
my_corner.order()

# my_rest = Restaurant('"У Марио"', "Японские блюда", "свежевыжатый сок", "08:00", "22:00", 15)
# my_rest.desc_rest()
# my_rest.num_of_seats(6)
# my_rest.working_hours("23:00")
# my_rest.num_of_workers()
