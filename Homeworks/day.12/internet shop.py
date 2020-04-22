from flask import Flask, render_template, request, url_for
import xlrd

workbook = xlrd.open_workbook('../day.10/db.xlsx')
worksheet = workbook.sheet_by_index(0)
f_obj_list = []
obj_list = []
books = []


def info():
    return True


def all_info():
    for row in worksheet.get_rows():
        libre_off_ls = []
        for element in row:
            libre_off_ls.append(element.value)
        return libre_off_ls


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
        info_1 = 'ID: ' + str(self._id_) + ' ' + str(self.name) + ' :' + str(self.prize) + ' $'
        return info_1

    def show_money(self):
        return float(self.prize)


class Book(Product):
    def __init__(self, name, _id_, prize, author, pages, quantity):
        super().__init__(name, _id_, prize, quantity)
        self.pages = pages
        self.author = author


start_program()
app = Flask(__name__)
app.debug = True


@app.route('/')
def main():
    return render_template('totalyrealshop.html')


@app.route('/products/', methods=["post"])
def products():
    return render_template('totalyrealshop.html', list_0=f_obj_list)


app.run()
