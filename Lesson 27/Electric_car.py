from Car import Car

class Battery():
    """Простая модель аккумулятора для электромобиля"""
    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        """Выводит информацию о мощности батареи"""
        print("Этот автомобиль имеет батарею мощьностью " + str(self.battery) + " киловат")

    def razryad(self):
        self.odometer_reader

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