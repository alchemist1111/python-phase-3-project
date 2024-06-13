from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Author, Book, Borrower, BorrowedBook

# Create the engine
engine = create_engine('sqlite:///library.db')

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# 1. Select all records from the 'authors' table
all_authors = session.query(Author).all()
print("All Authors:")
for author in all_authors:
    print(f"ID: {author.id}, Name: {author.name}")

# 2. Filter records with a condition
filtered_authors = session.query(Author).filter(Author.name == 'Author One').all()
print("\nFiltered Authors:")
for author in filtered_authors:
    print(f"ID: {author.id}, Name: {author.name}")

# 3. Join tables
books_with_authors = session.query(Book).join(Author).all()
print("\nBooks with Authors:")
for book in books_with_authors:
    print(f"Book Title: {book.title}, Author Name: {book.author.name}")

# 4. Update records
author_to_update = session.query(Author).filter(Author.name == 'Author One').first()
if author_to_update:
    author_to_update.name = 'Updated Author One'
    session.commit()
    print(f"\nUpdated Author ID: {author_to_update.id}, New Name: {author_to_update.name}")

# 5. Delete records
author_to_delete = session.query(Author).filter(Author.name == 'Updated Author One').first()
if author_to_delete:
    session.delete(author_to_delete)
    session.commit()
    print(f"\nDeleted Author ID: {author_to_delete.id}")

# Close the session
session.close()
