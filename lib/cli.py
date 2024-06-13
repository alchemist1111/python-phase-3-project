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

# Function to return a book
def return_book(book_id):
    book = session.query(Book).get(book_id)
    if book:
        borrowed_books = session.query(BorrowedBook).filter_by(book_id=book.id).all()
        for borrowed_book in borrowed_books:
            session.delete(borrowed_book)
        session.commit()
        print(f"Book {book.title} returned")
    else:
        print("Invalid book")  

# Main function to parse command-line arguments and execute actions
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--action', choices=['get_books', 'get_authors', 'get_borrowers', 'borrow_book', 'return_book'])
    parser.add_argument('--book_id', type=int)
    parser.add_argument('--borrower_id', type=int)
    args = parser.parse_args()

    if args.action == 'get_books':
        get_books()
    elif args.action == 'get_authors':
        get_authors()
    elif args.action == 'get_borrowers':
        get_borrowers()
    elif args.action == 'borrow_book':
        borrow_book(args.book_id, args.borrower_id)
    elif args.action == 'return_book':
        return_book(args.book_id)                                  