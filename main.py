class Order:
    # TODO:
    pass


class ShoppingCart:
    # TODO:
    pass


cart = ShoppingCart()
apple = Order(5, 2.99)
banana = Order(2, 4.99)

cart.add(apple)
cart.add(banana)

total = cart.get_total_cost()

print(f'total: ${total}')
