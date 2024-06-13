import argparse
from Database import session  # Import the session created in Database.py
from model import Book, Author, Borrower, BorrowedBook  # Import the models

# Function to get all books
def get_books():
    result = session.query(Book).all()
    for book in result:
        print(f"Title: {book.title}, Author: {book.author.name}")

# Function to get all authors
def get_authors():
    result = session.query(Author).all()
    for author in result:
        print(f"Name: {author.name}")  

# Function to get all borrowers
def get_borrowers():
    result = session.query(Borrower).all()
    for borrower in result:
        print(f"Name: {borrower.name}")              