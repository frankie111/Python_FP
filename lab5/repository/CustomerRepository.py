from lab5.repository.Repository import Repository
from lab5.repository.formatters.CustomerFormatter import CustomerFormatter


class CustomerRepository(Repository):

    def __init__(self):
        super().__init__()
        self.__customers = self.__db_root + "/customers/customers.txt"

    def add(self, customer):
        """
        Adds a new customer to the database
        :param customer:
        """
        c_formatter = CustomerFormatter(self.__customers)
        customer_list = c_formatter.load()

        if customer_list == -1:
            customer_list = [customer]
            c_formatter.save(customer_list)
            print(f"Added '{customer.name}' with address '{customer.address}'")
            return

        if customer not in customer_list:
            next_id = customer_list[-1].id + 1
            customer.id = next_id
            customer_list.append(customer)
            c_formatter.save(customer_list)
            print(f"Added '{customer.name}' with address '{customer.address}'")
        else:
            print(f"Customer '{customer.name}' with address '{customer.address}' already exists!")

    def remove(self, customer):
        """
        Removes a customer from the database
        :param customer:
        """
        c_formatter = CustomerFormatter(self.__customers)
        customer_list = c_formatter.load()

        if customer_list == -1:
            print("Customer database is empty!")
            return

        new_list = list(filter(lambda c: c != customer, customer_list))

        if len(new_list) != len(customer_list):
            c_formatter.save(new_list)
            print(f"Removed customer '{customer.name}' with address '{customer.address}'")
        else:
            print(f"Customer '{customer.name}' with address '{customer.address}' doesn't exist!")

    def find(self, name=None, address=None):
        """
         Filters a list of customers that match the name or address provided
         :param name:
         :param address:
         :returns: a list of customers | -1 if no information was provided
         :rtype: list|int
         """
        c_formatter = CustomerFormatter(self.__customers)
        customer_list = c_formatter.load()

        if name is not None:
            results = list(filter(lambda c: name.lower() in c.name.lower(), customer_list))
            return results

        if address is not None:
            results = list(filter(lambda c: address.lower() in c.address.lower(), customer_list))
            return results

        return -1

    def update(self, customer, updated_customer):
        """
        Updates a customer if found in database
        :param updated_customer:
        :param customer:
        """
        c_formatter = CustomerFormatter(self.__customers)
        customer_list = c_formatter.load()
        