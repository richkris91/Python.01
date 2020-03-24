from Modules_01.celsius_fahrenheit import celsius_into_fahrenheit, fahrenheit_into_celsius
from Modules_01.validator_01 import validator
print('''Welcome to '0.1 Royal Multitool',
to access one of the given functions enter a representative number
1): Square maker,
2): Egyptian special,
3): Dog age
4): Celsius into Fahrenheit
5): Fahrenheit into Celsius
''')
input_1 = input(': ')
if validator(input_1) and 0 < int(input_1) <= 5:
    number = int(input_1)
    if number == 1:
        print('You have chosen the Square maker ')
        input_square = input('Enter square height/length: ')
        if validator(input_square):
            x_1 = int(input_square)
            if x_1 == 1:
                print('+')
                print('End')
            else:
                print('+' + '--' * (x_1 - 2) + '+')
                for i in range((x_1-2)):
                    print('|' + '  ' * (x_1-2) + '|')
                print('+' + '--' * (x_1 - 2) + '+')
                print('End')
        else:
            pass
    elif number == 2:
        print('You have chosen the Egyptian special')
        input_Egyptian = input('Enter pyramid height: ')
        if validator(input_Egyptian):
            x_2 = int(input_Egyptian)
            counter_2 = 0
            while counter_2 < x_2:
                print(' ' * 14 + ' ' * (x_2 - 1 - counter_2) + (counter_2 + 1) * '[]')
                counter_2 += 1
            print('End')
    elif number == 3:
        print('Coming soon')
    elif number == 4:
        input_4 = input('Enter degrees in Celsius: ')
        if validator(input_4):
            celsius_into_fahrenheit(input_4)
    elif number == 5:
        pass
    else:
        print('You have not entered a correct number')
