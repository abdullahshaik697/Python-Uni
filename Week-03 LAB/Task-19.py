# List of book titles with duplicates
book_titles = ["The Great Gatsby", "1984", "To Kill a Mockingbird", "1984", "The Catcher in the Rye", "The Great Gatsby"]

# Remove duplicates by converting to a set and back to a list
unique_books = list(set(book_titles))

# New arrivals to add at the beginning
new_arrivals = ["Brave New World", "Pride and Prejudice"]

# Add new arrivals at the beginning of the list
unique_books = new_arrivals + unique_books

# Print the updated list
print("Updated Book List:", unique_books)