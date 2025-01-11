# 404B Lesson 5 Class Project - Shopping Cart

## Instructions

### Split VS Code Window

You can drag `main.py` tab to the right side of the window to split the window into two panes. This will allow you to see the instructions and the code at the same time.

### Answering

You can answer the questions by writing your answers in the `main.py` file.

You can run the code by clicking the `Run` button on the top right corner of the editor.

The output will be shown in the `Terminal` tab at the bottom of the editor.

## Your Task

Write two classes:

`ShoppingCart` class that represents a list of items to buy from the market.should have the following methods:

- `__init__()`: Create a new empty list.

- `add(order)`: Adds the given item order to this list.

- `get_total_cost()`: Returns the total sum cost of all grocery item orders in this list.

---

`Order` class that represents a request to purchase a particular item in a given quantity (e.g., four boxes of cookies).

- `__init__(quantity, price)`: Initialize properties: **quantity** & **price per unit**

- `get_cost()`: Returns the total cost of this item in its given quantity.\
  For example, four boxes of cookies that cost 2.30 per unit have a total cost of 9.20.

### Sample Input

```python
class Order:
    ...


class ShoppingCart:
    ...


cart = ShoppingCart()
apple = Order(5, 2.99)
banana = Order(2, 4.99)

cart.add(apple)
cart.add(banana)
total = cart.get_total_cost()
print(f'total: ${total}')
```

### Sample Output

`total: $24.93`

## Submitting Your Work

1. Make sure the assignment repository is opened in VS Code.

2. Make sure you have completed all the tasks.

3. (First time only)
Use Command + J to open the Terminal tab and config your git username and email:

    ```bash
    git config user.name "Your Name"
    git config user.email "Your GitHub Email"
    ```

4. Click on the "Source Control" icon on the left. Source Control

    ![1](https://github.com/BlueinnoClassroom/404B-L2.1-Template/assets/155412668/2c31026e-c14d-484f-bb9e-dc87189a0216)

5. Enter a commit message and click on the "Commit" button.

6. Click on the "Sync Changes" button.
