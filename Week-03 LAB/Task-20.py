# List of property prices
property_prices = [250000, 300000, 150000, 500000, 200000, 400000, 350000]

# Define the price range
min_price = 200000
max_price = 400000

# Filter properties within the price range using list comprehension
filtered_prices = [price for price in property_prices if min_price <= price <= max_price]

# Sort the filtered prices in ascending order
filtered_prices.sort()

# Print the results
print("Filtered and Sorted Prices:", filtered_prices)