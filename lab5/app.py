from lab5.models.CookedDish import CookedDish
from lab5.models.Customer import Customer
from lab5.models.Drink import Drink
from lab5.repository.CustomerRepository import CustomerRepository

m1 = CookedDish("ciorba de legume", 460, 24, 30)
m2 = CookedDish("Pizza Quattro Formaggi", 640, 50, 45)
d1 = Drink("Bere Ursus", 500, 8, 5)

repo = CustomerRepository("repository/database/customers/customers.txt")
c1 = Customer(0, "Mircea", "Rozdesti")
c2 = Customer(0, "Bobi", "Bobalna")
c3 = Customer(0, "Baiatu", "Tocmai din India")
c4 = Customer(0, "Mircea", "Nasaud")
c5 = Customer(0, "Andrei", "Constanta")

res = repo.add_list([c1, c2, c3, c4, c5])