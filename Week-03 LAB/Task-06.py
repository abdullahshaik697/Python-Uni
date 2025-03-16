# List of product prices
product_prices = [45, 78, 120, 55, 95, 34, 85, 150, 60, 99]
# Filter products in the given price range
filtered_prices = [price for price in product_prices if 50 <= price <= 100]
# Print result
print("Products in price range $50 - $100:", filtered_prices)
