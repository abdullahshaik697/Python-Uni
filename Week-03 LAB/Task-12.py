from collections import Counter

# Customer's order history
order_history = ["apple", "banana", "apple", "orange", "banana", "grape", "apple", "orange", "canceled", "banana", "canceled"]

# Remove canceled orders
while "canceled" in order_history:
    order_history.remove("canceled")

# Count the frequency of each product
product_counts = Counter(order_history)

# Print the updated order history and product counts
print("Updated Order History:", order_history)
print("Product Counts:", product_counts)