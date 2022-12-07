from lab5.models.CookedDish import CookedDish
from lab5.models.Customer import Customer
from lab5.models.Order import Order
from lab5.repository.CookedDishRepository import CookedDishRepository
from lab5.repository.CustomerRepository import CustomerRepository
from lab5.repository.OrderRepository import OrderRepository


def order_bill_test():
    customer_repo = CustomerRepository("customers.txt")
    dish_repo = CookedDishRepository("cooked_dishes.txt")
    dish_repo.clear()
    customer_repo.clear()

    customer_repo.add(Customer(0, "Marian", "Str. Ciocan"))
    dish_repo.add_list([CookedDish(0, "Sarmale", 400, 35, 60), CookedDish(0, "Ciorba de burta", 350, 24, 45)])

    customer = customer_repo.get_all()[0]
    dishes = dish_repo.get_all()

    order = Order(0, customer.id, [dishes[0].id, dishes[1].id])
    order.create_time_stamp()
    bill = order.generate_bill(dishes)
    print(bill)

    assert "Sarmale" in bill and "Ciorba de burta" in bill and "Gesamtkosten .................. 59" in bill


def save_load_order_test():
    order_repo = OrderRepository("orders.txt")
    customer_repo = CustomerRepository("customers.txt")
    dish_repo = CookedDishRepository("cooked_dishes.txt")
    dish_repo.clear()
    customer_repo.clear()
    order_repo.clear()

    customer_repo.add(Customer(0, "Marian", "Str. Ciocan"))
    dish_repo.add_list([CookedDish(0, "Sarmale", 400, 35, 60), CookedDish(0, "Ciorba de burta", 350, 24, 45)])

    customer = customer_repo.get_all()[0]
    dishes = dish_repo.get_all()

    order = Order(0, customer.id, [dishes[0].id, dishes[1].id])
    order.compute_total_price(dishes)
    order.create_time_stamp()

    order_repo.add(order)

    read_order = order_repo.get_all()[0]

    assert read_order == order


order_bill_test()
save_load_order_test()
