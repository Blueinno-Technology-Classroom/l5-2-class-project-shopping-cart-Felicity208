class Order:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
        self.cost = 0
    
    def get_cost(self):
        self.cost = self.price * self.quantity
        print(f'Total: {self.cost}')
        return self.cost


class ShoppingCart:
    def __init__(self):
        self.shoppinglist = []
        
    def add(self, order):
        self.shoppinglist.append(order)


    def get_total_cost(self):
        self.totalCost = 0
        for i in self.shoppinglist:
            self.totalCost += i.get_cost()
        return self.totalCost


cart = ShoppingCart()
apple = Order(5, 2.99)
banana = Order(2, 4.99)

cart.add(apple)
cart.add(banana)


total = cart.get_total_cost()

print(f'total: ${total}')
