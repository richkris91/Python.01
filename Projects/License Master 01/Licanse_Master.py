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
            1: ['User', user_logs],
            2: ['Logs uses'],
            3: ['Computers ']
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
    # opening files
    users = {
        'Users': '\n'
    }
    log_fracts = []
    files = os.listdir('week_20')
    # extracting data
    for element in files:
        element1 = element.replace("'", '')
        with open('./week_20/' + element1, 'r+') as opened_file:
            content = opened_file.read().split('\n')
            for element in range(len(content)):
                if ' IN: ' in content[element] or ' OUT: ' in content[element]:
                    if ' ids_l ic@pl01-lic5' not in content[element]:
                        log_fract = content[element].split(' ')
                        log_fracts.append(log_fract)
    print('-' * 20)
    user_menu = {
        'enter': [': Show all info'],
        'x    ': [': Exit']
    }
    for key in user_menu:
        print(key + user_menu[key][0])
    print('-' * 20)
    input_user = input('What would you like to do?')
    if input_user == '':
        # Creating user objects
        for element in log_fracts:
            lic_count = ''
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
                if lic_count != '':
                    new_log = log(element[0], element[2], element[3], username, computer, lic_count)
                else:
                    new_log = log(element[0], element[2], element[3], username, computer)
                users[username].add_req(new_log)
                comps = users[username].show_comps()
                if str(computer) not in comps:
                    users[username].add_comp(computer)
        del users['Users']
        counter_name_list = 6
        users_list = []
        for key in users:
            if counter_name_list == 6:
                users_list.append([])
                counter_name_list = 0
            else:
                users_list[len(users_list) - 1].append(': ' + key + ' ' * (8 - len(key)))
                counter_name_list += 1
        for element in range(len(users_list)):
            if len(users_list[element]) != 0:
                print(str(users_list[element][:]))
        input_all = input('=' * 84 + '\nTo witch user would you like to apply this command?\n'
                                     'Press enter to apply to every one of the above:\n')
        if input_all == '':
            counter = 1
            for key in users:
                print(str(counter) + ': User : ' + users[key].show_user()[0])
                print(' ' * 5 + 'Number of Computers: ' + str(len(users[key].show_user()[1])))
                print(' ' * 5 + 'Number of logs: ' + str(len(users[key].show_user()[2])))
                print(' ' * 8 + 'Computers')
                comp_count = 0
                comps_logs = users[key].comps_logs()
                for key in comps_logs:
                    print(' ' * 10 + 'Computer: ' + key)
                    sorted_logs = log_sorter(comps_logs[key])
                    for key in sorted_logs:
                        for element in sorted_logs[key]:
                            print(' ' * 12 + element.show_log())
                        print('^' * 84)

                comp_count += 1
                counter += 1
        else:
            for key in users:
                if input_all == key:
                    user_ = input_all
                    print('User : ' + users[user_].show_user()[0])
                    print(' ' * 5 + 'Number of Computers: ' + str(len(users[user_].show_user()[1])))
                    print(' ' * 5 + 'Number of logs: ' + str(len(users[user_].show_user()[2])))
                    print(' ' * 8 + 'Computers')
                    comps_logs = users[user_].comps_logs()
                    for key in comps_logs:
                        print(' ' * 10 + key)
                        for element in comps_logs[key]:
                            print(' ' * 12 + element.show_log())
                else:
                    pass


def log_sorter(array):
    Sorted_logs = {}
    for element in array:
        if 'IN' in element.show_type():
            Sorted_logs[element.show_license() + ' : ' + str(element.show_lic_nr())] = []
            Sorted_logs[element.show_license() + ' : ' + str(element.show_lic_nr())].append(element)
    for element in array:
        if 'OUT' in element.show_type():
            for key in Sorted_logs:
                if element.show_license() + ' : ' + str(element.show_lic_nr()) == key:
                    Sorted_logs[element.show_license() + ' : ' + str(element.show_lic_nr())].append(element)
    return Sorted_logs


class log(object):
    def __init__(self, time, type_, license_, username, computer_, how_many_lic=1):
        self.time = time
        self.type_ = type_
        self.license_ = license_
        self.username = username
        self.computer = computer_
        self.how_many_licenses = how_many_lic

    def re_comp(self):
        return self.computer

    def show_log(self):
        return self.time + ' ' + self.type_ + ' ' + self.license_ + ' ' + str(self.how_many_licenses)

    def show_license(self):
        return self.license_

    def show_lic_nr(self):
        return self.how_many_licenses

    def show_type(self):
        return self.type_


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

    def comps_logs(self):
        comps_dic = {}
        logs = self.requests
        for element in self.computers:
            comps_dic[element] = []
        for key in comps_dic:
            deleted = 0
            for element in range(len(logs)):
                if logs[element - deleted].re_comp() == key:
                    comps_dic[key].append(logs[element - deleted])
                    del logs[element - deleted]
                    deleted += 1
        return comps_dic


user_logs()
