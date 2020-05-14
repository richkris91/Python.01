import re
import xlwt

library = []


class file(object):
    def __init__(self, lines, nr, date, time, port, des_host, des_interface, BW, RE, TX, TX_b, TX_p, RX, RX_b, RX_p):
        self.lines = lines
        self.nr = nr
        self.date = date
        self.time = time
        self.port = re.split(' ', port)
        self.Host_r = self.port[1]
        self.If_name = self.port[2]
        self.des_host = des_host
        self.des_interface = des_interface
        self.BW = BW
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
        return str(self.nr) + '\n' + str(len(self.lines)) + '\n' + str(self.time) + '\n' + str(self.port)

    def data_table(self):
        return_ls = [str(self.nr),
                     str(self.date), str(self.time),
                     str(self.Host_r),
                     str(self.If_name), str(self.des_host), str(self.des_interface),
                     str(self.BW),
                     str(self.RE), str(round(int(self.RE_min) * 100 / int(self.RE_max), 2)) + '%',
                     str(self.TX), str(round(int(self.TX_min) * 100 / int(self.TX_max), 2)) + '%', str(self.TX_b),
                     str(int(self.TX_b) / 1000), str(self.TX_p),
                     str(self.RX), str(round(int(self.RX_min) * 100 / int(self.RX_max), 2)) + '%', str(self.RX_b),
                     str(int(self.RX_b) / 1000), str(self.RX_p)]
        return return_ls


def table_data(root='cisc.xlsx'):
    wb = xlwt.Workbook()
    new_sheet = wb.add_sheet(root)
    data = [
        'Object_Number',
        'Date', 'Time',
        'Host_attribute', 'If_name', 'Des_Host', 'Des_Interface',
        'BW', 'RE', 'RE_%',
        'TX', 'TX_%', 'TX_b/s', 'TX_Mb/s', 'TX_packets',
        'RX', 'RX_%', 'RX_b/s', 'RX_MB/s', 'RX_packets'
    ]
    counter = 0
    for element in data:
        new_sheet.write(0, counter, element)
        counter += 1
    counter2 = 1
    for element in range(len(library)):
        counter3 = 0
        while counter3 < len(data):
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
        des_host_f = ''
        des_interface_f = ''
        date_f = ''
        time_f = ''
        port_f = ''
        RE = ''
        BW = ''
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
                time_1 = element[16:]
                time_1 = time_1.strip('\n')
                time_2 = time_1.split(' ')
                date_f = time_2[0]
                time_f = time_2[1]
            if 'Port pl' in element:
                port_f = element.strip('\n')
                port_f = port_f.strip('Port')
                port_f = port_f.replace(' :', '')
            if 'Description:' in element:
                des_1 = element.replace('Description: ', '')
                des_2 = des_1.replace('\n', '')
                des_3 = des_2.split(' ')
                counter_des = 0
                max_des = len(des_3)
                while max_des != 0:
                    if des_3[counter_des] == '':
                        del des_3[counter_des]
                        counter_des -= 1
                    if des_3[counter_des] == 'connection':
                        del des_3[counter_des]
                        counter_des -= 1
                    if des_3[counter_des] == 'to':
                        del des_3[counter_des]
                        counter_des -= 1
                    counter_des += 1
                    max_des -= 1
                if ':' not in des_3[0]:
                    des_host_f = 'None'
                    des_interface_f = 'None'
                else:
                    des_4 = str(des_3[0]).split(':')
                    des_host_f = des_4[0]
                    des_interface_f = des_4[1]
            if 'MTU ' and 'BW ' and 'DLY ' in element:
                BW_1 = element.strip('\n')
                BW_2 = BW_1.split(' ')
                count_BW = 0
                while count_BW < len(BW_2):
                    if BW_2[count_BW] == '':
                        del BW_2[count_BW]
                    count_BW += 1
                MTU = BW_2[1:4]
                BW = str(BW_2[5] + ' ' + BW_2[6].strip(','))
                DLY = BW_2[7:10]
            if 'reliability' and 'txload' and 'rxload' in element:
                RE_ls = re.split(' ', element.strip())
                RE = RE_ls[1]
                TX = RE_ls[3]
                RX = RE_ls[5]
            if 'output rate' in element:
                TX_1 = element
                TX_2 = TX_1.split('rate', 2)
                del TX_2[0]
                TX_3 = str(TX_2[0])
                TX_4 = TX_3.split(',', 2)
                TX_b = int(str(TX_4[0]).split('bits', 2)[0])
                TX_p = int(str(TX_4[1]).split('packets', 2)[0])
            if 'input rate' in element:
                RX_1 = element
                RX_2 = RX_1.split('rate', 2)
                del RX_2[0]
                RX_3 = str(RX_2[0])
                RX_4 = RX_3.split(',', 2)
                RX_b = int(str(RX_4[0]).split('bits', 2)[0])
                RX_p = int(str(RX_4[1]).split('packets', 2)[0])
            if element == '\n':
                if len(lines_f) >= 7:
                    obj = file(lines_f, len(library) + 1,
                               date_f, time_f,
                               port_f, des_host_f, des_interface_f,
                               BW, RE,
                               TX, TX_b, TX_p, RX, RX_b, RX_p)
                    library.append(obj)
                lines_f = []

            counter_act = 0
            while counter_act == 0:
                for key in obj_filter:
                    if obj_filter[key] in element:
                        element = element.strip('\n')
                        lines_f.append(element)
                    counter_act += 1
    except FileNotFoundError:
        print('File not found')


file_reader()
table_data()
x = input('Enter file: ')
if x == '':
    table_data()
else:
    table_data(x)
