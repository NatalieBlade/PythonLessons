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

class Battery():
    """Простая модель аккумулятора для электромобиля"""
    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print("Этот автомобиль имеет батарею мощьностью " + str(self.battery) + " киловат")

    def razryad(self, odometer):
        self.odometer_reader = odometer
        if self.battery < 100:
            self.odometer_reader * self.battery

    def charge(self):
        input("Уровень заряда батареи: ")
        if self.battery <= 20:
            print("Пора зарядить батарею")
        elif self.battery > 20 and self.battery <= 99:
            print("Заряда батареи достоточно")
        elif self.battery == 100:
            print("Батарея заряжена полностью")
        else:
            print("Уровень заряда батареи: ")


class ElectricCar(Car):
    """Аспекты для электромобиля"""
    def __init__(self, make, model, year):
        """Инициализация атрибутов класса родителя"""
        super().__init__(make, model, year) #super помогает связать потомка и родителя
        self.battery = Battery()

    def description_name(self):
        """Переопределяем метод родителя""" #python игнорирует метод родителя и спользует метод ребенка
        desc = str(self.year) + " " + self.model
        return desc.title()

#В атрибуте любого класса мы можем использовать экземпляр другого класса

tesla = ElectricCar("Tesla", "s", 2017)
tesla.battery.description_battery()

tesla.battery.charge()

#tesla = ElectricCar("Tesla", "s", 2017)
#print(tesla.description_name())
#tesla.description_battery()
