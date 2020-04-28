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
            '6': ['Show commands', ],
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
                print('--------------------------------------')
                library[int(input_i2) - 1].show_all('1')
            #except:
                    #print('You have not managed the input correctly')
        elif input_1 == '3':
            input_i3 = select_obj()
            if input_i3 == '':
                print('--------------------------------------')
                counter__2 = 1
                for element in range(len(library)):
                    library[element].show_description(counter__2)
                    counter__2 += 1
                print('--------------------------------------')
            elif input_i3 == 0:
                pass
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
            pass


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
                lines_count += 1
                file_lines.append(element)
    except:
        print('File not found')
    print(str(lines_count) + ' lines')
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
