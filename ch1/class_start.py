class Book:
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    __booklist = None

    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def settitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype) -> None:
        self.title = title

        if (booktype not in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype


print("Book types: ", Book.getbooktypes())


b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "PAPERBACK")


thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)

print(thebooks)
