import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("J.D.", "Salinger")
author_repository.save(author1)

author2 = Author("Dossie", "Easton")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Catcher in the Rye", "Fiction", "Little, Brown and Company", author1)
book_repository.save(book1)

book2 = Book("The Ethical Slut", "Self-help", "Greenery Press", author2)
book_repository.save(book2)

book_repository.select_all()

