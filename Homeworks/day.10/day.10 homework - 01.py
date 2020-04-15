import xlrd
from Modules_01.validator_01 import validator
from Modules_01.Biggest_array_element import biggest_string_in_a_array

workbook = xlrd.open_workbook('./db.xlsx')
worksheet = workbook.sheet_by_index(0)
f_obj_list = []
obj_list = []
books = []


def adding_to_cart():
    info()
    add_cart = input('Enter objects ID without .0: ')
    if validator(add_cart) and int(add_cart) <= len(obj_list) - 1:
        cart.adding_to_cart(int(add_cart))
        return True
    else:
        return True


def go_away():
    print('Bye')
    return False


def info():
    for element in obj_list:
        print(element.show())
    return True


def all_info():
    for row in worksheet.get_rows():
        libre_off_ls = []
        for element in row:
            libre_off_ls.append(element.value)
        print(libre_off_ls)
    return True


def start_program():
    # Printing every product
    for row in worksheet.get_rows():
        obj_list_row = []
        for element in row:
            obj_list_row.append(element.value)
        f_obj_list.append(obj_list_row)
    # Creating objects
    for element in range(len(f_obj_list)):
        # Adding Book objects to obj list
        if f_obj_list[element][5] == 'Book' or 'EBook':
            add_name = f_obj_list[element][1]
            add_id = f_obj_list[element][0]
            add_prize = f_obj_list[element][8]
            add_author = f_obj_list[element][6]
            add_pages = f_obj_list[element][7]
            add_quantity = f_obj_list[element][4]
            add_class = Book
            add_obj = add_class(add_name, add_id, add_prize, add_author, add_pages, add_quantity)
            obj_list.append(add_obj)


def program():
    start_program()
    End = True
    print('Welcome to definitely not fake shop')
    options = {
        1: ['. View available objects', info],
        2: ['. Full object info', all_info],
        3: ['. Add to cart', adding_to_cart],
        4: ['. Show cart', show_cart],
        5: ['. Exit', go_away]
    }
    while End:
        for key in options:
            print(str(key) + options[key][0])
        print('------------------------------------')
        x = input('Whats your choice? :')
        if validator(x) and int(x) <= 5:
            End = options[int(x)][1]()
            print('------------------------------------')
        else:
            print('------------------------------------')
            pass


def show_cart():
    cart.show_cart()
    return True


class Shopping_cart(object):
    def __init__(self, content=None):
        if content is None:
            content = []
        self.content = content

    def adding_to_cart(self, ID):
        self.content.append(obj_list[ID])

    def show_cart(self):
        money = 0
        if len(self.content) == 0:
            print('Your cart is empty!')
        else:
            for element in self.content:
                money += element.show_money()
                print(element.show())
            print('That will cost you: ' + str(money) + ' $')


class Product(object):
    def __init__(self, name, _id_, prize, quantity):
        self.quantity = quantity
        self.name = name
        self._id_ = _id_
        self.prize = prize

    def show(self):
        return 'ID: ' + str(self._id_) + ' ' + str(self.name) + ' :' + str(self.prize) + ' $'

    def show_money(self):
        return float(self.prize)


class Book(Product):
    def __init__(self, name, _id_, prize, author, pages, quantity):
        super().__init__(name, _id_, prize, quantity)
        self.pages = pages
        self.author = author


cart = Shopping_cart()
program()
