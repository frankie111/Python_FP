from lab5.models.CookedDish import CookedDish
from lab5.models.Customer import Customer
from lab5.models.Drink import Drink
from lab5.repository.CustomerRepository import CustomerRepository

m1 = CookedDish("ciorba de legume", 460, 24, 30)
m2 = CookedDish("Pizza Quattro Formaggi", 640, 50, 45)
d1 = Drink("Bere Ursus", 500, 8, 5)

repo = CustomerRepository("repository/database/customers/customers.txt")