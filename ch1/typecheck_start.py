class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


b1 = Book("War and Peace")
b2 = Book("How not to give a F**k!")


n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")


print(type(b1))
print(type(n1))

print(isinstance(n1, Book))
print(isinstance(b2, Book))
print(isinstance(n2, object))
