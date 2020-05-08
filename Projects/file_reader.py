import re
import xlrd
import xlwt

library = []


class file(object):
    def __init__(self, lines, nr, time, port, description, RE, TX, TX_b, TX_p, RX, RX_b, RX_p):
        self.lines = lines
        self.nr = nr
        self.time = time
        self.port = port
        self.Host_r = re.split(' ', self.port)[0]
        self.If_name = re.split(' ', self.port)[1]
        self.description = description
        self.RE = RE.strip(',')
        self.RE_min = re.split('/', self.RE)[0].strip(',')
        self.RE_max = re.split('/', self.RE)[1].strip(',')
        self.TX = TX.strip(',')
        self.TX_min = re.split('/', self.TX)[0].strip(',')
        self.TX_max = re.split('/', self.TX)[1].strip(',')
        self.TX_b = TX_b
        self.TX_p = TX_p
        self.RX = RX.strip(',')
        self.RX_min = re.split('/', self.RX)[0].strip(',')
        self.RX_max = re.split('/', self.RX)[1].strip(',')
        self.RX_b = RX_b
        self.RX_p = RX_p

    def show(self):
        return str(self.nr) + '\n' + str(len(self.lines)) + '\n' + str(self.time) + '\n' + str(self.por) + '\n' + str(
            self.description)

    def data_table(self):
        return_ls = []
        return_ls.append(str(self.nr))
        return_ls.append(str(self.Host_r))
        return_ls.append(str(self.time))
        return_ls.append(str(self.If_name))
        return_ls.append(str(self.description))
        return_ls.append(str(self.RE))
        return_ls.append(str(int(self.RE_min) * 100 / int(self.RE_max)))
        return_ls.append(str(self.TX))
        return_ls.append(str(self.TX_b))
        return_ls.append(str(int(self.TX_b) / 1000))
        return_ls.append(str(self.TX_p))
        return_ls.append(str(int(self.TX_min) * 100 / int(self.TX_max)))
        return_ls.append(str(self.RX))
        return_ls.append(str(self.RX_b))
        return_ls.append(str(int(self.RX_b) / 1000))
        return_ls.append(str(self.RX_p))
        return_ls.append(str(int(self.RX_min) * 100 / int(self.RX_max)))
        return return_ls


def show_data_table():
    try:
        workbook = xlrd.open_workbook('cisc.xlsx')
        worksheet = workbook.sheet_by_index(0)
    except FileNotFoundError:
        wb = xlwt.Workbook()
        newsheet = wb.add_sheet('cisc.xlsx')
        newsheet.write(1, 1, 'contents here')


def file_reader():
    try:
        with open('Test_01', "r+") as file__:
            files_0 = file__.readlines()
        obj_filter = {1: ' pl',
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
        description_f = ''
        for element in files_0:
            time_f = ''
            port_f = ''
            description_f = ''
            RE = ''
            TX = ''
            RX = ''
            TX_b = ''
            TX_p = ''
            RX_b = ''
            RX_p = ''
            if 'date and time' in element:
                time_f = element[16:]
                time_f = time_f.strip('\n')
            if 'Port pl' in element:
                port_f = element.strip('Port ')
                port_f = port_f.strip('\n')
                port_f = port_f.strip(':')
            if 'Description' in element:
                description_f = element.strip('Description: ')
            if 'reliability' and 'txload' and 'rxload' in element:
                RE_ls = re.split(' ', element)
                RE = RE_ls[1]
                TX = RE_ls[3]
                RX = RE_ls[5]
            if 'second output rate' in element:
                TX_l = re.split(' ', element)
                TX_b = TX_l[2]
                TX_p = TX_l[4]
            if 'second input rate' in element:
                RX_l = re.split(' ', element)
                RX_b = RX_l[2]
                RX_p = RX_l[4]
            if element == '\n':
                if len(lines_f) >= 7:
                    obj = file(lines_f, len(library) + 1, time_f, port_f, description_f, RE, TX, TX_b, TX_p, RX, RX_b,
                               RX_p)
                    library.append(obj)
                lines_f = []
            for key in obj_filter:
                if obj_filter[key] in element:
                    element = element.strip('\n')
                    lines_f.append(element)
    except FileNotFoundError:
        print('File not found')


file_reader()
for element in library:
    print(element.show())
