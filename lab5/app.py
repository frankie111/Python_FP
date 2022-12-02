from lab5.models.CookedDish import CookedDish
from lab5.models.Customer import Customer
from lab5.models.Drink import Drink
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.Repository import Repository

m1 = CookedDish("ciorba de legume", 460, 24, 30)
m2 = CookedDish("Pizza Quattro Formaggi", 640, 50, 45)
d1 = Drink("Bere Ursus", 500, 8, 5)

repo = CustomerRepository()
c1 = Customer(0, "Mircea", "Rozdesti")
c2 = Customer(0, "Cox", "Nasaud")
c3 = Customer(0, "Baiatu", "Tocmai din India")
c4 = Customer(0, "Mircea", "Nasaud")
c5 = Customer(0, "Andrei", "Constanta")

# repo.add_customer(c1)
# repo.add_customer(c2)
# repo.add_customer(c3)
# repo.add_customer(c4)
# repo.remove_customer(c2)
for customer in repo.get_all():
    print(customer)