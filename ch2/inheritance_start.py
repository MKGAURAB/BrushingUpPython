class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price


class Magazine:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period


class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("The New York Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, n1.price, m1.price)
