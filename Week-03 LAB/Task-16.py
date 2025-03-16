# List of daily expenses for a week (Monday to Sunday)
# Assume a missing expense is represented by None
expenses = [50, 30, None, 20, 40, 60, 10]

# Insert the missing expense (e.g., 25 for Wednesday)
missing_expense = 25
missing_index = 2  # Index for Wednesday (0-based index)

# Insert the missing expense in the correct position
expenses.insert(missing_index, missing_expense)

# Remove the placeholder None (if any)
if None in expenses:
    expenses.remove(None)

# Calculate the total expense for the week
total_expense = sum(expenses)

# Print the results
print("Updated Expenses:", expenses)
print("Total Expense for the Week:", total_expense)