# class Animal(object):
#    def __init__(self, name, sex):
#        self.name = name
#        self.sex = sex
# dog = Animal('Rex', 'male')
# print(dog)
#
#
# class Animal(object):
#    pass
#
#
# class Human(Animal):
#    pass
#
#
# class Student(Human):
#   pass


class Book(object):
    def __init__(self, title, author, vat=0.07, sites=100, price=19.99):
        self.title = title
        self.sites = sites
        self.author = author
        self.price = price
        self.vat = 0.07


class Ebook(Book):
    def __init__(self, title, author, vat=0.15, sites=210, price=9.99):
        super().__init__(title, author, vat, sites, price)
        self.sites = sites
        self.price = 9.99
        self.vat = 0.15


class Cart(object):
    def __init__(self, books=0, ebooks=0):
        self.books = books
        self.ebooks = ebooks

    def add_book(self, ebooks0, books0):
        self.books += books0
        self.ebooks += ebooks0
        print('Books added')
        print('You have: ' + str(self.books) + ' books')
        print('You have: ' + str(self.ebooks) + ' ebooks')

        def gross_price(self, books, ebooks):
            gross = books * Book.price() + ebooks * Ebook.price()
            return gross



cart1 = Cart
cart1.add_book(Cart, 12, 12)
