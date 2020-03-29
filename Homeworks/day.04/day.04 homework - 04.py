from Modules_01.multitool_functions import celsius_into_fahrenheit, fahrenheit_into_celsius, validator, square_maker, egyptian_special, entry_counter
functions = {
    '1': ['Celsius into Fahrenheit', celsius_into_fahrenheit],
    '2': ['Fahrenheit into celsius', fahrenheit_into_celsius],
    '3': ['Square maker', square_maker],
    '4': ['Egyptian special', egyptian_special]
}


def menu(function_list):
    print('''Welcome to '0.2 Royal Multitool',
to access one of the given functions enter a representative number''')
    for key in function_list:
        print(key + ': ' + str(function_list[key][0]))
    print('PS, '
          'You have opened this program ' + entry_counter() + ' times')


menu(functions)
input_1 = (input(': '))
if validator(input_1):
    if int(input_1) <= 4:
        functions[str(input_1)][1]()
    else:
        print('But it did not represent any of the given functions')
