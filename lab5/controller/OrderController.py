from lab5.repository.OrderRepository import OrderRepository


class OrderController:
    def __init__(self, customer_repo, order_repo, cooked_dish_repo, drink_repo):
        self.__customer_repo = customer_repo
        self.__order_repo = order_repo
        self.__cooked_dish_repo = cooked_dish_repo
        self.__drink_repo = drink_repo
