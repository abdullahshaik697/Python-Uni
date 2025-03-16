# List of daily sales (in USD)
sales = [210, 340, 290, 450, 320, 400, 500, 620, 300, 280, 490, 515, 400, 
390, 275, 
 325, 410, 475, 525, 300, 350, 420, 275, 620, 580, 495, 515, 610, 
700, 450]
# Compute total, average, max, and min sales
total_sales = sum(sales)
average_sales = total_sales / len(sales)
max_sales = max(sales)
min_sales = min(sales)
# Print results
print("Total Sales:", total_sales, "USD")
print("Average Daily Sales:", round(average_sales, 2), "USD")
print("Highest Sales:", max_sales, "USD")
print("Lowest Sales:", min_sales, "USD")
