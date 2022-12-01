from lab5.models.CookedDish import CookedDish
from lab5.models.Drink import Drink
from lab5.repository.CookedDishFormatter import CookedDishFormatter
from lab5.repository.DrinkFormatter import DrinkFormatter

m1 = CookedDish("ciorba de legume", 460, 24, 30)
m2 = CookedDish("Pizza Quattro Formaggi", 640, 50, 45)
d1 = Drink("Bere Ursus", 500, 8, 5)

cd_formatter = CookedDishFormatter("repository/test.txt")
cd_formatter.save([m1])
cd_list = cd_formatter.load()

d_formatter = DrinkFormatter("repository/test.txt")
d_formatter.save([d1])
d_list = d_formatter.load()

for d in d_list:
    print(d.id)
    print(type(d))
