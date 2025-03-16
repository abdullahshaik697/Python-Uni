from collections import Counter
# List of customer orders
orders = ["Burger", "Pizza", "Pasta", "Pizza", "Burger", "Burger", "Salad", 
"Pizza", "Pasta", "Burger"]
# Count occurrences of each item
order_counts = Counter(orders)
# Find the most ordered item
most_ordered = order_counts.most_common(1)[0]
# Print result
print("Most Ordered Item:", most_ordered[0], "(", most_ordered[1], "times)")
