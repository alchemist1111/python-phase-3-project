from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, declarative_base


# Define the base class for the ORM models
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', backref='books')


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String) 

class Borrower(Base):
    __tablename__ = 'borrowers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    borrowed_books = relationship('BorrowedBook', back_populates='borrower') 

class BorrowedBook(Base):
    __tablename__ = 'borrowed_books'
    book_id = Column(Integer, ForeignKey('books.id'), primary_key=True)
    borrower_id = Column(Integer, ForeignKey('borrowers.id'), primary_key=True)
    book = relationship('Book', backref='borrowed_books')
    borrower = relationship('Borrower', back_populates='borrowed_books')  

# Create the engine
engine = create_engine('sqlite:///library.db')

# Create the tables in the database
Base.metadata.create_all(engine)
           