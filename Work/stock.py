class Stock:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.price*self.shares

    def sell(self, amount):
        self.shares -= amount

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
