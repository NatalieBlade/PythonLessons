class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + ", " + self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан открыт")

restaurant = Restaurant("Tropicano", "Вьетнамская кухня")
restaurant_2 = Restaurant("У Марио", "Итальянская кухня")
restaurant_3 = Restaurant("Матрешка", "Русская кухня")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(restaurant.restaurant_name, restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()