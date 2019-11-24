from book import Book


class Library:
    books = [Book(1, "book1", "author1"), Book(2, "book2", "author2"), Book(3, "book3", "author3")]

    def __init__(self) -> None:
        super().__init__()

    def get_all_books(self):
        books = self.books
        return self.books

    def get_book_by_name(self, name):
        for book in self.books:
            if book.name == name:
                return book

    def get_book_by_id(self, id):
        for book in self.books:
            if book.id == id:
                return book

    def add_book(self, book):
        self.books.append(book)

    def add_book(self, name, author):
        max_id = 0
        for book in self.books:
            if book.id > max_id:
                max_id = book.id
        max_id += 1
        new_book = Book(max_id, name, author)
        self.books.append(new_book)
        return self.get_book_by_id(max_id)

    def update_book(self, id, name, author):
        for book in self.books:
            if book.id == id:
                book.name = name
                book.author = author
        return self.get_book_by_id(id)

    def delete_book_by_id(self, id):
        print(id)
        book = self.get_book_by_id(id)
        print(book)
        if book is not None:
            self.books.remove(book)
            return True
        else:
            return False

    def __repr__(self):
        return str(self.__dict__)
