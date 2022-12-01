from lab5.repository.formatters.CustomerFormatter import CustomerFormatter


class Repository:
    def __init__(self, db_root="repository/database"):
        self.__db_root = db_root
        self.__menu = db_root + "/menu"
        self.__cooked_dishes = self.__menu + "/cooked_dishes.txt"
        self.__drinks = self.__menu + "/drinks.txt"
        self.__customers = db_root + "/customers/customers.txt"
        self.__orders = db_root + "/orders/orders.txt"

    def add_customer(self, customer):
        """
        Adds a new customer to the database
        :param customer:
        """
        c_formatter = CustomerFormatter(self.__customers)
        customer_list = c_formatter.load()

        if customer_list == -1:
            customer_list = [customer]
            c_formatter.save(customer_list)
            print(f"Added '{customer.name}'")
            return

        if customer not in customer_list:
            next_id = customer_list[-1].id + 1
            customer.id = next_id
            customer_list.append(customer)
            c_formatter.save(customer_list)
            print(f"Added '{customer.name}'")
        else:
            print(f"Customer '{customer.name}' with address '{customer.address}' already exists!")

    def remove_customer(self, customer):
        """
        Removes a customer from the database
        :param customer:
        :return:
        """
        c_formatter = CustomerFormatter(self.__customers)
        customer_list = c_formatter.load()

        if customer_list == -1:
            print("Customer database is empty!")
            return

        if customer in customer_list:
            customer_list.remove(customer)
            c_formatter.save(customer_list)
            print(f"Removed customer '{customer.name}' with address '{customer.address}'")
        else:
            print(f"Customer '{customer.name}' with address '{customer.address}' doesn't exist!")