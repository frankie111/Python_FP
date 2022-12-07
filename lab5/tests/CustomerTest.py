from lab5.models.Customer import Customer
from lab5.repository.CustomerRepository import CustomerRepository

customer_repo = CustomerRepository("customers.txt")
customer_repo.clear()
cus1 = Customer(0, "Mircea", "Str. Rozdesti")
cus2 = Customer(0, "Andrei", "Str. Ardei")
cus3 = Customer(0, "Marian", "Str. Ciocan")
customer_repo.add_list([cus1, cus2, cus3])


def search_customer_by_name_test(repo):
    customer1 = repo.search(Customer(name="mir"))[0]
    customer2 = repo.search(Customer(name="drei"))[0]
    customer3 = repo.search(Customer(name="ian"))[0]

    assert customer1 == cus1 and customer2 == cus2 and customer3 == cus3


def search_customer_by_address_test(repo):
    customer1 = repo.search(Customer(address="roz"))[0]
    customer2 = repo.search(Customer(address="dei"))[0]
    customer3 = repo.search(Customer(address="cioc"))[0]

    assert customer1 == cus1 and customer2 == cus2 and customer3 == cus3


def update_customer_test(repo: CustomerRepository, cus):
    cus_id = repo.search(Customer(name="Mircea"))[0].id
    repo.update(cus, Customer(name="Bogdan"))
    customer = repo.find_by_id(cus_id)

    assert customer.id == cus_id


search_customer_by_name_test(customer_repo)
search_customer_by_address_test(customer_repo)
update_customer_test(customer_repo, cus1)
