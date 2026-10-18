# This program calculates the total value of the stock of my cafe

# List of items on the menu
menu = ['espresso',
        'cappuccino',
        'croissant',
        'sandwich',
        'muffin']

# Dictionary with the item and its quantity on stock

stock = {'espresso': 400,
         'cappuccino': 200,
         'croissant': 100,
         'sandwich': 100,
         'muffin': 100,
         }

# Dictionary with the item and its unit price
price = {'espresso': 1.00,
         'cappuccino': 1.50,
         'croissant': 2.00,
         'sandwich': 2.00,
         'muffin': 1.50,
        }

# Setting total_stock = 0
total_stock = 0

# Iterate over my stock dictionary
for item, value in stock.item():
    
    