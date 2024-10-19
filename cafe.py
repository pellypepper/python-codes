"""
this program calculates the total price of each item in the menu and 
the toal price of all the items in the menu .
its  stored the items in a list and uses a dictionary to store the 
stock value and price of each item in the menu

"""



# list of items in menu
menu = ["Americano", "Latte", "Espresso", "Cappuccino"]

#value of items stock
stock = {
    "Americano": 18,
    "Latte": 14,
    "Espresso": 21,
    "Cappuccino": 12
}

#price of  each item
price = {
    "Americano": 15,
    "Latte": 20,
    "Espresso": 34,
    "Cappuccino": 25
}


count = 0
total_item_value = 0

#iterate throught the menu list and calculate the total value of each item s
while  count < len(menu):
   item = menu[count]
   stock_value = int(stock[item])
   price_item = int(price[item])

   #calculate the total stock price of each item   and total stock value of all the item 
   item_value = stock_value * price_item
   total_item_value += item_value

   #output
   print(f"Total {item} stock value is {stock_value} and the total price is ${item_value:.2f}")
   count += 1

#output
print(f"The total value of all the item price is ${total_item_value:.2f}")

