import re

library = []


class file(object):
    def __init__(self, lines, nr, time):
        self.lines = lines
        self.nr = nr
        self.time = time

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

    def show__reliability(self):
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
        return "| " + nums[0] + ' ' * (7 - len(str(nums[0]))) + " = " + rel_p + ' %' + ' ' * (5 - len(str(rel_p))) + \
               "| " + nums[2] + ' ' * (7 - len(str(nums[2]))) + " = " + txt_p + ' %' + ' ' * (5 - len(str(txt_p))) + \
               "| " + nums[4] + ' ' * (7 - len(str(nums[2]))) + " = " + rxl_p + ' %' + ' ' * (5 - len(str(rxl_p))) + \
               "| "


def show_reliability(All=0):
    if len(library) < All:
        print('You have not managed to enter the input correctly')
    else:
        num = len(str(len(library))) + 2
        print('-------------------------------------------------------------')
        print(' ' * num + '|   Reliability    |      Txload      |       Rxload     |')
        print('-------------------------------------------------------------')
        if All == 0:
            counter_rel = 1
            for element in range(len(library)):
                print(str(counter_rel) + ': ' + library[element].show__reliability())
                counter_rel += 1
            print('-------------------------------------------------------------')
        else:
            print(str(All) + ': ' + library[All - 1].show__reliability())
            print('-------------------------------------------------------------')


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
                show_reliability()
            else:
                show_reliability(int(input_i5))


def file_reader():
    try:
        with open('Test_01', "r") as file_:
            files_0 = file_.readlines()
        obj_filter = {1: 'Port pl01-c4500x-1 :',
                      2: 'Description:',
                      3: 'MTU',
                      4: 'reliability',
                      5: 'Input queue:',
                      6: '30 second output rate',
                      7: 'input errors,',
                      8: 'output errors,',
                      9: 'unknown protocol drops'
                      }
        lines_f = []
        time_f = ''
        for element in files_0:
            if 'date and time' in element:
                time_f = element[16:]
            if element == '\n':
                if len(lines_f) >= 8:
                    obj = file(lines_f, len(library) + 1, time_f, )
                    library.append(obj)
                lines_f = []
            for key in obj_filter:
                if obj_filter[key] in element:
                    lines_f.append(element)
    except FileNotFoundError or FileExistsError:
        print('File not found')


file_reader()
print(library)
