from db.run_sql import run_sql

from models.book import Book
from models.author import Author

import repositories.author_repository as author_repository

def save(book):
    sql = "INSERT INTO books (title, genre, publisher,author_id) VALUES (%s,%s,%s,%s) RETURNING *"
    values = [book.title, book.genre, book.publisher,book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book



def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        book = Book(row['title'], row['genre'], row['publisher'], row['author_id'])
        books.append(book)
    return books
    
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql,values)