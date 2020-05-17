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


def user_logs():
    users = {}
    files = os.listdir('week_20')
    for element in files:
        element1 = element.replace("'", '')
        with open('./week_20/' + element1, 'r+') as opened_file:
            content = opened_file.read().split('\n')
            for element in range(len(content)):
                if ' IN: ' in content[element] or ' OUT: ' in content[element]:
                    if ' ids_l ic@pl01-lic5' not in content[element]:
                        log_fract = content[element].split(' ')
    for element in log_fract:
        if element[4] not in users:
            users[str(element[4])] = []
        if element[4] in users:
            log = [element[0], element[2], element[3]]
            if len(element) == 8:
                log.append(element[6])
            else:
                log.append('None')




class user(object):
    def __init__(self, requests, username, computer):
        self.requests = requests
        self.username = username
        self.computer = computer


user_logs()
