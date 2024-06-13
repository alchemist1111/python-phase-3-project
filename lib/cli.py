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

# Function to borrow a book
def borrow_book(book_id, borrower_id):
    book = session.query(Book).get(book_id)
    borrower = session.query(Borrower).get(borrower_id)
    if book and borrower:
        borrowed_book = BorrowedBook(book=book, borrower=borrower)
        session.add(borrowed_book)
        session.commit()
        print(f"Book {book.title} borrowed by {borrower.name}")
    else:
        print("Invalid book or borrower")                     