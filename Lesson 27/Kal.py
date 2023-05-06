from Rest import  Restaurant

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