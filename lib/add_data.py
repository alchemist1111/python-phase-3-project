from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Author, Book, Borrower, BorrowedBook

# Create the engine
engine = create_engine('sqlite:///library.db')

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add authors
author1 = Author(name='Author One')
author2 = Author(name='Author Two')
session.add(author1)
session.add(author2)
session.commit()

# Add books
book1 = Book(title='Book One', author=author1)
book2 = Book(title='Book Two', author=author2)
session.add(book1)
session.add(book2)
session.commit()

# Add borrowers
borrower1 = Borrower(name='Borrower One')
borrower2 = Borrower(name='Borrower Two')
session.add(borrower1)
session.add(borrower2)
session.commit()

# Add borrowed books
borrowed_book1 = BorrowedBook(book=book1, borrower=borrower1)
borrowed_book2 = BorrowedBook(book=book2, borrower=borrower2)
session.add(borrowed_book1)
session.add(borrowed_book2)
session.commit()

# Close the session
session.close()
