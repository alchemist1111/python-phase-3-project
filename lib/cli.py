import argparse
from Database import session  # Import the session created in Database.py
from model import Book, Author, Borrower, BorrowedBook  # Import the models

# Function to get all books
def get_books():
    result = session.query(Book).all()
    for book in result:
        print(f"Title: {book.title}, Author: {book.author.name}")