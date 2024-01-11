# Library.py

from Book import Book
from User import User

# Create a book and a user
book = Book("Python Programming", "John Doe", "978-0-13-444432-1")
user = User("python_user", "python@example.com")

# Display book and user details
book.display()
user.display()
