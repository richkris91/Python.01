import xlrd
from Modules_01.Biggest_array_element import biggest_string_in_a_array

workbook = xlrd.open_workbook('./db.xlsx')
worksheet = workbook.sheet_by_index(0)
f_obj_list = []
obj_list = []
books = []


def program():
    # Printing every product
    print('Available products')
    for row in worksheet.get_rows():
        obj_list_row = []
        libre_off_ls = []
        for element in row:
            libre_off_ls.append(element.value)
            obj_list_row.append(element.value)
        f_obj_list.append(obj_list_row)
        print(libre_off_ls)
    print(f_obj_list)
    # Creating objects
    for element in range(len(f_obj_list)):
        # Adding Book objects to obj list
        if f_obj_list[element][5] == 'Book' or 'EBook':
            print(f_obj_list[element][1])
            add_name = f_obj_list[element][1]
            add_id = f_obj_list[element][0]
            add_prize = f_obj_list[element][8]
            add_author = f_obj_list[element][6]
            add_pages = f_obj_list[element][7]
            add_quantity = f_obj_list[element][4]
            add_obj = Book(add_name, add_id, add_prize, add_author, add_pages, add_quantity)
            books.append(add_obj)
        obj_list.append(books)
    print(obj_list[0])


class Shopping_cart(object):
    def __init__(self, content=None):
        self.content = content

    def adding_book_to_cart(self, ID):
        self.content = []
        pass


class Product(object):
    def __init__(self, name, _id_, prize, quantity):
        self.quantity = quantity
        self.name = name
        self._id_ = _id_
        self.prize = prize


class Book(Product):
    def __init__(self, name, _id_, prize, author, pages, quantity):
        super().__init__(name, _id_, prize, quantity)
        self.pages = pages
        self.author = author


program()
