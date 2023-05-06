from Rest import Restaurant
from Kal import Kalyan_corner

my_corner = Kalyan_corner('"У Марио"', "Японские блюда", "свежевыжатый сок", "08:00", "22:00", 15, "Konoplya")
my_corner.order()

my_rest = Restaurant('"У Марио"', "Японские блюда", "свежевыжатый сок", "08:00", "22:00", 15)
my_rest.desc_rest()
my_rest.num_of_seats(6)
my_rest.working_hours("23:00")
my_rest.num_of_workers()