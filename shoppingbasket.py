class Item:
    def __init__(self, name, description, price, stock_level=0):
        self.name = name
        self.description = description
        self.price = price
        self.stock_level = stock_level

    def __str__(self):
        return f"Name :{self.name}\nDescription: {self.description}\nPrice: {self.price}\nStock level: {self.stock_level}\n"

class ShoppingBasket:
    def __init__ (self ):
        self.items = {}
    
    # Add an item to the basket
    def addItem(self,item, quantity):
        if quantity == 0:
            return "Quantity must be greater than zero"
        if item.name in self.items:
            # Increase the quantity if the item already exists in the basket
            self.items[item.name]['quantity'] += quantity
 
        else:
            # Add new item to the basket
            self.items[item.name] = {'item': item, 'quantity': quantity}
        # Decrease the stock level by the quantity
        item.stock_level -= quantity

    # Remove an item from the basket
    def remove(self, item, quantity):
        if item.name in self.items:
            # Decrease the quantity if the item exists in the basket
            self.items[item.name]['quantity'] -= quantity
            if self.items[item.name]['quantity'] <= 0:
                # Remove item if quantity is zero or negative
                del self.items[item.name]
        else:
            return "Item not found in basket"
        # Increase the stock level by the quantity
        item.stock_level += quantity
 
    # Get the total cost of the items in the basket
    def getTotalCost(self):
        total_cost = 0
        # Calculate the total cost of all items in the basket
        for item_name, details in self.items.items():
           total_cost += details['item'].price * details['quantity']
        return total_cost
        
    # Update the quantity of an item in the basket
    def update(self, item, quantity):
        if quantity <= 0:
            return "Quantity must be greater than zero"
        # Check if the item exists in the basket
        if item.name in self.items:
            # Get the current quantity in the basket
            current_quantity = self.items[item.name]['quantity']

            # Check if there's enough stock to increase the quantity
            if quantity > current_quantity:
                difference = quantity - current_quantity
                if item.stock_level >= difference:
                    # Decrease the stock by the difference
                    item.stock_level -= difference
                else:
                    return f"Not enough stock to update {item.name} to {quantity}. Only {item.stock_level} items left."
            elif quantity < current_quantity:
                # Increase the stock level if reducing quantity in the basket
                difference = current_quantity - quantity
                item.stock_level += difference

            # Update the quantity in the basket
            self.items[item.name]['quantity'] = quantity
        else:
            return "Item not found in basket"
       
    
    # Reset the basket
    def reset(self):
        self.items = {}


    def __str__(self):
        basket_contents = ""
        for item_name, details in self.items.items():
            basket_contents += f"{details['item']} \nQuantity: {details['quantity']}\n\n"
        return f"Shopping Basket:\n{basket_contents}"

       
    def __repr__(self):
        return f"Items in the basket: {self.items}"
     
item1 = Item("Bread", "Whole wheat bread", 2.50, 40)
item2 = Item("Milk", "Whole milk", 3.50, 30)
print(item1)


shop1 = ShoppingBasket()
shop1.addItem(item1, 2)
shop1.addItem(item2, 10)
total = shop1.getTotalCost()
print(shop1)
print(f"Total cost: ${total:.2f}")

shop1.remove(item2, 5)
print(shop1)

shop1.update(item1, 5)
print(shop1)

