import re

library = []


class file(object):
    def __init__(self, lines, nr):
        self.lines = lines
        self.nr = nr

    def show_all(self, obj=''):
        counter = 1
        if obj in '':
            for element in self.lines:
                print(element)
        else:
            for element in self.lines:
                if len(element) >= 2:
                    print(str(counter) + ':' + element)
                    counter += 1

    def show_description(self, num=1):
        print(str(num) + ': ' + self.lines[2])

    def show_name(self):
        return self.lines[0]

    def info(self):
        return self.lines[5]

    def show_MTU(self):
        return self.lines[3]

    def show_reliability(self):
        nums = re.split(' | /', self.lines[4][17:])
        for element in range(len(nums)):
            nums[element] = nums[element].replace(',', '')
        rel_list = re.split('/', nums[0])
        rel_n = int(rel_list[0])
        rel_m = int(rel_list[1])
        rel_p = str(round(rel_n * 100 / rel_m, 2))
        txt_list = re.split('/', nums[2])
        txt_n = int(txt_list[0])
        txt_m = int(txt_list[1])
        txt_p = str(round(txt_n * 100 / txt_m, 2))
        rxl_list = re.split('/', nums[4])
        rxl_n = int(rxl_list[0])
        rxl_m = int(rxl_list[1])
        rxl_p = str(round(rxl_n * 100 / rxl_m, 2))
        return 'reliability ' + nums[0] + ' = ' + rel_p + ' %\n' + \
               '   txload      ' + nums[2] + ' = ' + txt_p + ' %\n' + \
               '   rxload      ' + nums[4] + ' = ' + rxl_p + ' %'

        # return self.lines[4][5:24] + ' = ' + str(
        # round(int(self.lines[4][17:20]) / int(self.lines[4][21:24]), 4) * 100) + ' % | ' +\
        # self.lines[4][26:38] + ' = ' + str(
        # round(int(self.lines[4][17:20]) / int(self.lines[4][21:]), 4) * 100)


def select_obj():
    input_25 = input('''To which object would you like to apply given command?
Enter   = all
Integer = given object
0       = return
: ''')
    return input_25


def program():
    go = True
    while go:
        commands = {
            '1': ['Show obj list'],
            '2': ['Show all info'],
            '3': ['Show description'],
            '4': ['Show MTU, BW and DLY'],
            '5': ['Show reliability, txload and rxload'],
            '7': ['End', ]
        }
        for key in commands:
            print(key + ': ' + commands[key][0])
        input_1 = str(input('What would you like to do?: '))
        if input_1 == '7':
            go = False
        elif input_1 == '1':
            counter_i1 = 0
            print('--------------------------------------')
            for element in library:
                print(str(counter_i1 + 1) + ': ' + element.show_name())
                counter_i1 += 1
            print('--------------------------------------')
        elif input_1 == '2':
            input_i2 = select_obj()
            if input_i2 == '':
                counter_i2 = 1
                for element in library:
                    print(str(counter_i2) + ': ----------------------------------')
                    element.show_all('')
                    counter_i2 += 1
            else:
                try:
                    print('--------------------------------------')
                    library[int(input_i2) - 1].show_all('1')
                except:
                    print('You have not managed the input correctly')
        elif input_1 == '3':
            input_i3 = select_obj()
            if input_i3 == '':
                print('--------------------------------------')
                counter__2 = 1
                for element in range(len(library)):
                    library[element].show_description(counter__2)
                    counter__2 += 1
                print('--------------------------------------')
            else:
                try:
                    print('--------------------------------------')
                    library[int(input_i3) - 1].show_description(int(input_i3))
                    print('--------------------------------------')
                except IndexError:
                    print('Object nr ' + str(input_i3) + ' does not exist')
                except:
                    print('You have not managed to enter input correctly')
        elif input_1 == '4':
            input_i4 = select_obj()
            if input_i4 == '':
                print('--------------------------------------')
                counter_4 = 1
                for element in range(len(library)):
                    print(str(counter_4) + ': ' + str(library[counter_4 - 1].show_MTU()))
                    counter_4 += 1
                print('--------------------------------------')
            else:
                try:
                    print('--------------------------------------')
                    print(str(int(input_i4)) + ': ' + library[int(input_i4)].show_MTU())
                    print('--------------------------------------')
                except:
                    print('You have not managed to enter the input correctly')
        elif input_1 == '5':
            input_i5 = select_obj()
            if input_i5 == '':
                print('--------------------------------------')
                counter_5 = 1
                for element in range(len(library)):
                    print(str(counter_5) + ': ' + str(library[counter_5 - 1].show_reliability()))
                    counter_5 += 1
                print('--------------------------------------')
            else:
                try:
                    print('--------------------------------------')
                    print(str(int(input_i5)) + ': ' + str(library[int(input_i5) - 1].show_reliability()))
                    print('--------------------------------------')
                except:
                    print('You have not managed to enter the input correctly')


def file_reader():
    file_name = 'Test'
    lines_count = 0
    line_min = 0
    line_max = 30
    file_lines = []
    try:
        with open(file_name, "r") as file_:
            file_lines_x = file_.readlines()
            for element in file_lines_x:
                element = element.rstrip('\n')
                lines_count += 1
                file_lines.append(element)
    except:
        print('File not found')
    while lines_count > 0:
        new_obj = []
        while line_min != line_max:
            try:
                new_obj.append(file_lines[line_min])
                line_min += 1
            except:
                line_min += 1
        new_file = file(new_obj, len(library) + 1)
        library.append(new_file)
        lines_count -= 30
        line_max += 30


# input_1 = str(input('Chose a file: '))
file_reader()
# for element in range(len(library)):
# print(library[element])
# print(library[element].show())
program()
