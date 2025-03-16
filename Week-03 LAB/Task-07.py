# List of player jersey numbers
jersey_numbers = [12, 7, 18, 9, 25, 6, 14, 21, 4, 11]
# Separate even and odd numbers
even_numbers = [num for num in jersey_numbers if num % 2 == 0]
odd_numbers = [num for num in jersey_numbers if num % 2 != 0]
# Print result
print("Team A (Even Jerseys):", even_numbers)
print("Team B (Odd Jerseys):", odd_numbers)
