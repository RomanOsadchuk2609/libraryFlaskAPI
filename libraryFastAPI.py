from fastapi import FastAPI
from pydantic import BaseModel

from library import Library


class Book(BaseModel):
    id: int
    name: str
    author: str


app = FastAPI()

library = Library()


@app.get('/')
def get_all_books():
    return library.get_all_books()


@app.get('/{name}"')
def get_book_by_name(name: str):
    book = library.get_book_by_name(name)
    if book is not None:
        return book
    else:
        return "There is no book with name: " + name


@app.post('/addBook')
def add_book(book: Book):
    name = book.name
    author = book.author
    return library.add_book(name, author)


@app.put('/updateBook')
def update_book(book: Book):
    updated_book = library.update_book(book.id, book.name, book.author)
    if updated_book is not None:
        return updated_book
    else:
        return "There is no book with id: " + str(book.id)


@app.delete('/deleteBook/{id}')
def delete_book(id: int):
    is_deleted = library.delete_book_by_id(id)
    if is_deleted:
        return "Book with id = " + str(id) + " was successfully deleted"
    else:
        return "There is no book with id: " + str(id)
