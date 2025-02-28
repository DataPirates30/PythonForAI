# List Comprehensions provide a concise, readable, and efficient way to create list
# They are widely used in data science and machine learning, web scraping, and text processing
# Use them to filter, transform, and process data faster!

# Key Advantages of List Comprehension
# ✔ More concise: Reduces multiple lines of code to one.
# ✔ More readable: Easy to understand for simple operations.
# ✔ Faster execution: Python optimizes list comprehensions better than loops.

def listComprehend():
    dataSets = [1,2,3,4]
    # Using list comprehension
    # Syntax: [expression for item in iterable if condition]
    # The expression is applied to each item in the iterable.
    # The condition filters the items that satisfy the condition.
    features = [i*j for i in range(5) for j in range(5)]
    print(features)

listComprehend()

