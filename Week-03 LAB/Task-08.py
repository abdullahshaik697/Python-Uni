from collections import Counter
# List of words in a blog post
words = ["data", "analytics", "python", "data", "AI", "analytics", 
"python", "data", "data", "ML"]
# Count word occurrences
word_count = Counter(words)
# Print result
print("Word Frequency:", word_count)
