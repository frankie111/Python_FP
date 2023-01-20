
class Shop:
    def __init__(self, products):
        self.products = products

    def buy(self, price):
        result = []
        for product in self.products:
            if len(product) * 2 <= price:
                result.append(f"{product} - {price}")
            else:
                raise BadName("Product name is too long")
        return result

class BadName(Exception):
    pass

class BetterShop(Shop):
    def __init__(self, products):
        super().__init__(products)
        self.total = 0

    def buy(self, price):
        try:
            result = super().buy(price)
            self.total += price
            return result
        except BadName:
            self.total = -1

    def __sub__(self, other):
        return [product for product in self.products if product in other.products]