from flask import Flask, jsonify, request
from library import Library

app = Flask(__name__)

library = Library()


@app.route('/')
def get_all_books():
    return jsonify(books=[b.serialize for b in library.get_all_books()])


@app.route('/<string:name>')
def get_book_by_name(name):
    book = library.get_book_by_name(name)
    if book is not None:
        return jsonify(book=book.serialize)
    else:
        return jsonify(error="There is no book with name: " + name)


@app.route('/addBook', methods=['POST'])
def add_book():
    name = request.get_json().get("name")
    author = request.get_json().get("author")
    return jsonify(book=library.add_book(name, author).serialize)


@app.route('/updateBook', methods=['PUT'])
def update_book():
    id = request.get_json().get("id")
    name = request.get_json().get("name")
    author = request.get_json().get("author")
    book = library.update_book(id, name, author)
    if book is not None:
        return jsonify(book=book.serialize)
    else:
        return jsonify(error="There is no book with id: " + str(id))


@app.route('/deleteBook/<int:id>', methods=['DELETE'])
def delete_book(id):
    is_deleted = library.delete_book_by_id(id)
    if is_deleted:
        return jsonify(message="Book with id = " + str(id) + " was successfully deleted")
    else:
        return jsonify(error="There is no book with id: " + str(id))


if __name__ == '__main__':
    app.run()
