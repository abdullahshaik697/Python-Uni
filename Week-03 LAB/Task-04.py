# List of stock prices over 10 days
stock_prices = [102.5, 101.8, 105.3, 107.2, 98.6, 103.4, 106.9, 99.3, 
100.5, 108.1]
# Compute highest, lowest, and average prices
max_price = max(stock_prices)
min_price = min(stock_prices)
avg_price = sum(stock_prices) / len(stock_prices)
# Print results
print("Highest Stock Price:", max_price, "USD")
print("Lowest Stock Price:", min_price, "USD")
print("Average Stock Price:", round(avg_price, 2), "USD")
