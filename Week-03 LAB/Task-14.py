# List of event attendees with duplicates
attendees = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob", "Eve"]

# Remove duplicates and sort alphabetically
sorted_unique_attendees = sorted(set(attendees))

# Print the result
print("Unique Attendees (Sorted):", sorted_unique_attendees)