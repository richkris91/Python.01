# #!/usr/bin/python3

import os


# files = os.listdir('week_20')

def license_master():
    menu()


def menu():
    go = 1
    while go == 1:
        commands = {
            0: ['Exit'],
            1: ['User logs', user_logs],
            2: ['Logs uses']
        }
        print('-' * 40)
        for key in commands:
            print(str(key) + ': ' + commands[key][0])
        command = input('Enter what would you like to do? :')
        print('-' * 40)
        try:
            r_com = int(command)
            if r_com > len(commands):
                print('You have not managed to enter the input correctly')
            else:
                if r_com == 0:
                    go -= 1
                else:
                    commands[r_com][1]()
        except:
            print('You have not managed to enter the input correctly')


def is_in_dic(dic, obj):
    for key in dic:
        if str(obj) in key:
            return True
    return False


def user_logs():
    users = {
        'start': 'start'
    }
    log_fracts = []
    files = os.listdir('week_20')
    for element in files:
        element1 = element.replace("'", '')
        with open('./week_20/' + element1, 'r+') as opened_file:
            content = opened_file.read().split('\n')
            for element in range(len(content)):
                if ' IN: ' in content[element] or ' OUT: ' in content[element]:
                    if ' ids_l ic@pl01-lic5' not in content[element]:
                        log_fract = content[element].split(' ')
                        log_fracts.append(log_fract)
    for element in log_fracts:
        lic_count = 'None'
        if len(element) >= 7 and '(' in str(element[:][6:7]):
            lic_count = element[:][6:7][0]
            lic_count = lic_count.replace('(', '')
            lic_count = int(lic_count)
        username = element[4].split('@')[0]
        computer = element[4].split('@')[1]
        if not is_in_dic(users, username):
            new_user = user(username, [], [])
            users[username] = new_user
        if is_in_dic(users, username):
            new_log = log(element[0], element[2], element[3], username, computer, lic_count)
            users[username].add_req(new_log)
            comps = users[username].show_comps()
            if str(computer) not in comps:
                users[username].add_comp(computer)
    counter = 1
    del users['start']
    for key in users:
        print(str(counter) + '_User : ' + users[key].show_user()[0])
        print(' ' * 5 + 'Number of Computers used by User_' + str(len(users[key].show_user()[1])))
        print(' ' * 5 + 'Number of logs_' + str(len(users[key].show_user()[2])))
        print(' ' * 8 + 'Computers')
        for element in users[key].show_user()[1]:
            print(' ' * 10 + element)
        counter += 1


class log(object):
    def __init__(self, time, type_, license_, username, computer, how_many_lic=1):
        self.time = time
        self.type_ = type_
        self.license_ = license_
        self.username = username
        self.computer = computer
        self.how_many_licenses = how_many_lic


class user(object):
    def __init__(self, username, computers, requests):
        self.requests = requests
        self.username = username
        self.computers = computers

    def add_req(self, add_list):
        self.requests.append(add_list)

    def add_comp(self, add_comp):
        self.computers.append(add_comp)

    def show_comps(self):
        return self.computers

    def show_user(self):
        return [self.username, self.computers, self.requests]


user_logs()
