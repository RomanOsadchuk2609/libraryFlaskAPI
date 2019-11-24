class Book:
    id: int
    name: str
    author: str

    def __init__(self, id, name, author):
        self.id = id
        self.name = name
        self.author = author

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author
        }

    def __repr__(self):
        return str(self.__dict__)
