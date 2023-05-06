#from Car import Car, ElectricCar #импортируем нужные классы из модуля
from Car import * #импортируем всё
from Electric_car import ElectricCar

a4 = Car("audi", "a4", 2016)
print(a4.description_name())

tesla = ElectricCar("Tesla", "s", 2017)
tesla.battery.description_battery()