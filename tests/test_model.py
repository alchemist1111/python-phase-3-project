# tests/test_model.py
import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Book, Author, Borrower, BorrowedBook

class TestModels(unittest.TestCase):

    def setUp(self):
        """Set up an in-memory SQLite database for testing."""
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        """Tear down the database after each test."""
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_author_creation(self):
        """Test creating an author."""
        author = Author(name="J.K. Rowling")
        self.session.add(author)
        self.session.commit()
        
        # Fetch the author from the database
        saved_author = self.session.query(Author).filter_by(name="J.K. Rowling").first()
        self.assertIsNotNone(saved_author)
        self.assertEqual(saved_author.name, "J.K. Rowling")

    def test_book_creation(self):
        """Test creating a book with an author."""
        author = Author(name="J.K. Rowling")
        self.session.add(author)
        self.session.commit()

        book = Book(title="Harry Potter and the Philosopher's Stone", author=author)
        self.session.add(book)
        self.session.commit()

        # Fetch the book from the database
        saved_book = self.session.query(Book).filter_by(title="Harry Potter and the Philosopher's Stone").first()
        self.assertIsNotNone(saved_book)
        self.assertEqual(saved_book.title, "Harry Potter and the Philosopher's Stone")
        self.assertEqual(saved_book.author.name, "J.K. Rowling")

    def test_borrower_creation(self):
        """Test creating a borrower."""
        borrower = Borrower(name="John Doe")
        self.session.add(borrower)
        self.session.commit()
        
        # Fetch the borrower from the database
        saved_borrower = self.session.query(Borrower).filter_by(name="John Doe").first()
        self.assertIsNotNone(saved_borrower)
        self.assertEqual(saved_borrower.name, "John Doe")

    def test_borrowing_books(self):
        """Test borrowing a book."""
        author = Author(name="J.K. Rowling")
        self.session.add(author)
        self.session.commit()

        book = Book(title="Harry Potter and the Chamber of Secrets", author=author)
        self.session.add(book)
        self.session.commit()

        borrower = Borrower(name="Jane Doe")
        self.session.add(borrower)
        self.session.commit()

        borrowed_book = BorrowedBook(book=book, borrower=borrower)
        self.session.add(borrowed_book)
        self.session.commit()

        # Fetch the borrowed book relationship from the database
        saved_borrowed_book = self.session.query(BorrowedBook).filter_by(book_id=book.id, borrower_id=borrower.id).first()
        self.assertIsNotNone(saved_borrowed_book)
        self.assertEqual(saved_borrowed_book.book.title, "Harry Potter and the Chamber of Secrets")
        self.assertEqual(saved_borrowed_book.borrower.name, "Jane Doe")

if __name__ == '__main__':
    unittest.main()
