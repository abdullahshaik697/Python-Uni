# Initial list of product quantities
product_quantities = [10, 5, 8, 3, 0, 7]

# New shipment quantities
new_shipment = [4, 6, 0, 9]

# Append new shipment quantities to the list
product_quantities.extend(new_shipment)

# Remove items that are out of stock (quantity = 0)
product_quantities = [quantity for quantity in product_quantities if quantity != 0]

# Print the updated list
print("Updated Product Quantities:", product_quantities)