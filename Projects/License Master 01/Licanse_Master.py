# #!/usr/bin/python3

import os


def user_creator(users, log_fracts):
    files_name = 'None'
    users = users
    for element in log_fracts:
        if '__FILE' in element:
            files_name = str(element).split(':')[1]
        else:
            lic_count = ''
            if 'licenses)' in str(element):
                lic_count = str(element).split('(',)[-1]
                lic_count = lic_count.[0].replace
                lic_count = lic_count.replace(')', '')
                lic_count = int(lic_count)
            username = element[4].split('@')[0]
            computer = element[4].split('@')[1]
            if not is_in_dic(users, username):
                new_user = user(username, [], [])
                users[username] = new_user
            if is_in_dic(users, username):
                if lic_count != '':
                    new_log = log(element[0], element[2], element[3], username, computer, files_name, lic_count)
                else:
                    new_log = log(element[0], element[2], element[3], username, computer, files_name)
                users[username].add_req(new_log)
                comps = users[username].show_comps()
                if str(computer) not in comps:
                    users[username].add_comp(computer)
    return users


def is_in_dic(dic, obj):
    for key in dic:
        if str(obj) in key:
            return True
    return False


def log_master():
    go = 1
    users_count = 1
    # opening files
    users = {
        'Users': '\n'
    }
    log_fracts = []
    files = os.listdir('week_20')
    # extracting data
    for element in files:
        element1 = element.replace("'", '')
        log_fracts.append('____FILE:' + str(element.split('_', 2)[1] + '_' + str(element.split('_', 2)[2])))
        with open('./week_20/' + element1, 'r+') as opened_file:
            content = opened_file.read().split('\n')
            for element in range(len(content)):
                if ' IN: ' in content[element] or ' OUT: ' in content[element]:
                    if ' ids_l ic@pl01-lic5' not in content[element]:
                        log_fract = content[element].split(' ')
                        log_fracts.append(log_fract)
    while go == 1:
        print('-' * 20)
        user_menu = {
            'enter': ': Show all info',
            'c    ': ': create text file',
            'x    ': ': Exit'
        }
        for key in user_menu:
            print(key + user_menu[key])
        print('-' * 20)
        input_user = input('What would you like to do?')
        # Don't mind this
        while users_count != 0:
            del users['Users']
            users_count -= 1
        #
        if input_user == 'x':
            go -= 1
        elif input_user == '':
            # Creating user objects
            users = user_creator(users, log_fracts)
            #
            counter_name_list = 6
            users_list = []
            # user list print
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
            #
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
                                file_org = element.show_org()
                                print(' ' * 12 + 'File: ' + file_org + ' :' + element.show_log())
                            print('-' * 84)
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
        elif input_user == 'c':
            print('=' * 84 + '\n')
            print("Enter: All user's data")
            if input('What would you like to save?') == '':
                # Creating user objects
                users1 = user_creator(users, log_fracts)
                #
                text_lines = []
                counter = 1
                for key in users1:
                    text_lines.append(str(counter) + ': User : ' + users1[key].show_user()[0])
                    text_lines.append(' ' * 5 + 'Number of Computers: ' + str(len(users1[key].show_user()[1])))
                    text_lines.append(' ' * 5 + 'Number of logs: ' + str(len(users1[key].show_user()[2])))
                    text_lines.append(' ' * 8 + 'Computers')
                    comp_count = 0
                    comps_logs = users1[key].comps_logs()
                    for key in comps_logs:
                        computer_name = key
                        sorted_logs = log_sorter(comps_logs[key])
                        compressed_logs = log_compressor(sorted_logs)
                        dates = ['Dates']
                        for key in compressed_logs:
                            for element in compressed_logs[key][0][0]:
                                if element.show_file_name().split('_')[0] not in dates:
                                    dates.append(element.show_file_name().split('_')[0])
                            for element in compressed_logs[key][1][0]:
                                if element.show_file_name().split('_')[0] not in dates:
                                    dates.append(element.show_file_name().split('_')[0])
                            comp_all_out = 0
                            comp_all_in = 0
                            for key in compressed_logs:
                                comp_all_out += compressed_logs[key][1][1][0]
                                comp_all_in += compressed_logs[key][0][1][0]
                        text_lines.append(
                            ' ' * 10 + 'Computer: ' + computer_name + ' OUT:' + str(comp_all_out) + ' IN: ' + str(
                                comp_all_in))
                        dates = str(dates).replace('[', '')
                        dates = dates.replace(']', '')
                        dates = dates.replace("'", '')
                        dates = dates.replace(',', '')
                        for key in compressed_logs:
                            text_lines.append(
                                ' ' * 12 + dates + ' ' +
                                compressed_logs[key][0][0][0].show_license() + '  OUT:' + str(
                                    compressed_logs[key][1][1][0]) + '  IN:' + str(
                                    compressed_logs[key][0][1][0]))
                        comp_count += 1
                    counter += 1
                with open('All_User_INFO', 'w+') as opened_file:
                    for element in range(len(text_lines)):
                        opened_file.write(text_lines[element] + '\n')
        elif input_user == 'l':
            users2 = user_creator(users, log_fracts)
            print(users2['pcelejew'].show_user())


def log_sorter(array):
    Sorted_logs = {}
    for element in array:
        if 'OUT' in element.show_type():
            Sorted_logs[element.show_license() + ' : ' + str(element.show_lic_nr())] = []
            Sorted_logs[element.show_license() + ' : ' + str(element.show_lic_nr())].append(element)
    for element in array:
        if 'IN' in element.show_type():
            for key in Sorted_logs:
                if element.show_license() + ' : ' + str(element.show_lic_nr()) == key:
                    Sorted_logs[element.show_license() + ' : ' + str(element.show_lic_nr())].append(element)
    return Sorted_logs


def log_compressor(dic):
    return_dic = {
        'start': [['start'], 0]
    }
    for key in dic:
        dic_key = key
        for element in range(len(dic[key])):
            movement = dic[dic_key][element].show_type()
            dic_num = int(dic[dic_key][element].show_lic_nr())
            return_keys = []
            for key in return_dic:
                return_keys.append(key)
            if dic_key not in return_keys:
                return_dic[dic_key] = [[[], []], [[], []]]
                if movement == 'OUT:':
                    return_dic[dic_key][0][0].append(dic[dic_key][element])
                    return_dic[dic_key][0][1].append(dic_num)
                    return_dic[dic_key][1][1].append(0)
                elif movement == 'IN:':
                    return_dic[dic_key][1][0].append(dic[dic_key][element])
                    return_dic[dic_key][1][1].append(dic_num)
                    return_dic[dic_key][0][1].append(0)
            elif dic_key in return_keys:

                if 'OUT:' in movement:
                    return_dic[dic_key][0][0].append(dic[dic_key][element])
                    return_dic[dic_key][0][1][0] += dic_num
                elif 'IN:' in movement:
                    return_dic[dic_key][1][0].append(dic[dic_key][element])
                    return_dic[dic_key][1][1][0] += dic_num
    del return_dic['start']
    return return_dic


class log(object):
    def __init__(self, time, type_, license_, username, computer_, file_name, how_many_lic=1):
        self.time = time
        self.type_ = type_
        self.license_ = license_
        self.username = username
        self.computer = computer_
        self.file_name = file_name
        self.how_many_licenses = how_many_lic

    def re_comp(self):
        return self.computer

    def show_log(self):
        return self.file_name + ' ' + self.type_ + ' ' + self.license_ + ' ' + str(self.how_many_licenses)

    def show_license(self):
        return self.license_

    def show_lic_nr(self):
        return self.how_many_licenses

    def show_type(self):
        return self.type_

    def show_org(self):
        return self.file_name

    def show_file_name(self):
        return self.file_name


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


log_master()
