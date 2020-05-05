import re

library = []


class file(object):
    def __init__(self, lines, nr, time):
        self.lines = lines
        self.nr = nr
        self.time = time


def file_reader():
    name = 'Test-01'
    try:
        with open(name, "r") as file_:
            files_0 = file_.readline()
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
        time_f = 'None'
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
    except FileNotFoundError:
        print('File not found')


file_reader()
