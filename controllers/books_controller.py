from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.book import Book
from repositories import book_repository, author_repository

books_blueprint = Blueprint("books", __name__)


# NEW

# GET '/books/new'
@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', all_books = books )
# CREATE
# POST '/books'

# SHOW
# GET '/books/<id>'

# EDIT
# GET '/books/<id>/edit'

# UPDATE
# PUT '/books/<id>'

# DELETE
# DELETE '/books/<id>'
@books_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete(id):
    book_repository.delete(id)
    return redirect ("/books")