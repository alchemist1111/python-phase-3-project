# tests/test_database.py
import unittest
from database import session
from model import Author, Book

class TestDatabase(unittest.TestCase):

    def test_author_creation(self):
        author = Author(name='J.K. Rowling')
        session.add(author)
        session.commit()
        self.assertIsNotNone(author.id)

if __name__ == '__main__':
    unittest.main()
