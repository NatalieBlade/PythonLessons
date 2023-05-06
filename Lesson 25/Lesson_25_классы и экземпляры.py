#классы и экземпляры

class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reader = 0

    def description_name(self):
        """Возвращаем описание автомобиля"""
        desc = str(self.year) + " " + self.make + " " + self.model
        return desc.title()

    def read_odometer(self):
        """Выводим пробег авто"""
        print("Пробег этого авто " + str(self.odometer_reader) + " км")

    #лучше изменять значение пробега с помощью метода
    def upd_odometer(self, km):
        """Устанавливаем значение на одометре"""
        if km >= self.odometer_reader:
            self.odometer_reader = km
        else:
            print("Не стоит с этим баловаться")

    def increment_odometer(self, km):
        """Увеличиваем показания одометра на заданную величину"""
        if km > 0:
            self.odometer_reader += km
        else:
            print("Отнимать пробег не стоит")

my_car = Car("audi", "a4", 2017)
#my_car.odometer_reader = 30 #можно измнить пробег, обратившить к атрибуту экземпляра напрямую
#print(my_car.description_name())
my_car.upd_odometer(33)
#my_car.upd_odometer(23)
my_car.increment_odometer(10)
my_car.increment_odometer(20)
my_car.read_odometer()