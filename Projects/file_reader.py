import re
import xlwt

library = []


class file(object):
    def __init__(self, lines, nr, time, port, description, RE, TX, TX_b, TX_p, RX, RX_b, RX_p):
        self.lines = lines
        self.nr = nr
        self.time = time
        self.port = re.split(' ', port)
        self.Host_r = self.port[1]
        self.If_name = self.port[2]
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
        return str(self.nr) + '\n' + str(len(self.lines)) + '\n' + str(self.time) + '\n' + str(self.port) + '\n' + str(
            self.description)

    def data_table(self):
        return_ls = [str(self.nr), str(self.Host_r), str(self.time), str(self.If_name), str(self.description),
                     str(self.RE), str(round(int(self.RE_min) * 100 / int(self.RE_max), 2)),
                     str(self.TX), str(round(int(self.TX_min) * 100 / int(self.TX_max), 2)), str(self.TX_b),
                     str(int(self.TX_b) / 1000), str(self.TX_p),
                     str(self.RX), str(round(int(self.RX_min) * 100 / int(self.RX_max), 2)), str(self.RX_b),
                     str(int(self.RX_b) / 1000), str(self.RX_p)]
        return return_ls


def table_data():
    wb = xlwt.Workbook()
    new_sheet = wb.add_sheet('cisc.xlsx')
    data = [
        'Object Nr', 'Host attribute', 'Date', 'If_name', 'Description',
        'RE', 'RE_%',
        'TX', 'TX_%', 'TX_b/s', 'TX_Mb/s', 'TX_packets',
        'RX', 'RX_%', 'RX_b/s', 'RX_MB/s', 'TX_packets'
    ]
    counter = 0
    for element in data:
        new_sheet.write(0, counter, element)
        counter += 1
    counter2 = 1
    for element in range(len(library)):
        counter3 = 0
        while counter3 <= 16:
            new_sheet.write(counter2, counter3, library[element].data_table()[counter3])
            counter3 += 1
        counter2 += 1
    wb.save('cisc.xlsx')


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
        time_f = ''
        port_f = ''
        RE = ''
        TX = ''
        RX = ''
        TX_l = ''
        TX_b = ''
        TX_p = ''
        RX_l = ''
        RX_b = ''
        RX_p = ''
        for element in files_0:
            if 'date and time' in element:
                time_f = element[16:]
                time_f = time_f.strip('\n')
            if 'Port pl' in element:
                port_f = element.strip('\n')
                port_f = port_f.strip('Port')
                port_f = port_f.replace(' :', '')
            if 'Description' in element:
                description_f = element.replace('Description: ', '')
                description_f = description_f.replace('\n', '')
                description_f[0].replace(' ', '')
            if 'reliability' and 'txload' and 'rxload' in element:
                RE_ls = re.split(' ', element.strip())
                RE = RE_ls[1]
                TX = RE_ls[3]
                RX = RE_ls[5]
            if 'second output rate' in element:
                TX_l = re.split(' ', element)
                TX_b = TX_l[2]
                TX_p = TX_l[4]
            if 'second input rate' in element:
                RX_f = element.replace('30 second input rate', '')
                RX_f1 = RX_f.replace('bits/sec,', '')
                RX_f2 = RX_f1.replace(' packets/sec\n', '')
                for element in range(len(RX_f2)):
                    if RX_f2 == '':
                        del.RX_f2
                RX_l = re.split(' ', RX_f2)
                print(RX_l)
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
table_data()
