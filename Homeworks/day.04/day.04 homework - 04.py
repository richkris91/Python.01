from Modules_01.multitool_functions import celsius_into_fahrenheit, fahrenheit_into_celsius, validator, square_maker
functions = {
    '1': 'celsius into fahrenheit', '2': 'fahrenheit into celsius',
    '3': 'square maker', '4': 'egyptian special'
}


def menu(function_list):
    print('''Welcome to '0.1 Royal Multitool',
to access one of the given functions enter a representative number''')
    for key in function_list:
        print(key + ': ' + function_list[key])


menu(functions)
input_1 = (input(': '))
int(functions[input_1])


# if validator(input_1) and 0 < int(input_1) <= 4:
#    number = int(input_1)
#   if number == 1:
#        print('You have chosen the Square maker ')
#        input_square = input('Enter square height/length: ')
#        if validator(input_square):
#            square_maker(input_square)
#    elif number == 2:
#        print('You have chosen the Egyptian special')
#        input_Egyptian = input('Enter pyramid height: ')
#        if validator(input_Egyptian):
#         x_2 = int(input_Egyptian)
#            counter_2 = 0
#            while counter_2 < x_2:
#                print(' ' * 14 + ' ' * (x_2 - 1 - counter_2) + (counter_2 + 1) * '[]')
#                counter_2 += 1
#            print('End')
#    elif number == 3:
#        print('Coming soon')
#    elif number == 4:
#        input_4 = input('Enter degrees in Celsius: ')
#        if validator(input_4):
#           celsius_into_fahrenheit(input_4)
#    elif number == 5:
#        pass
# else:
#   print('You have not entered a correct number')
