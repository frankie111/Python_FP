class BadName(Exception):
    def __init__(self):
        self.message = "Bad Name"


class Shop:
    def __init__(self, products: list[str]):
        self.products = products

    def buy(self, price: int):
        if len(self.products) * 2 > price:
            raise BadName

        return list(map(lambda product: f"{product} - {price}", self.products))


class BetterShop(Shop):
    def __init__(self, products: list[str]):
        super().__init__(products)
        self.total = 0

    def buy(self, price):
        try:
            res = super().buy(price)
            self.total += price
            return res
        except BadName as e:
            print(e.message)
            self.total = -1

    def __sub__(self, other: Shop):
        return BetterShop(list(filter(lambda product: product in other.products, self.products)))

# bs = BetterShop(["mere", "pere"])
# bs.buy(1)
