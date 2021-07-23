class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.autho = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secrect attribute"

    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price*self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount


b1 = Book("Nice New World", "Hooman", 101, 10.99)
b2 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

print(b1.getprice())

print(b2.getprice())
b2.setdiscount(.25)
print(b2.getprice())

print(b2._Book__secret)  # Name Mangling
