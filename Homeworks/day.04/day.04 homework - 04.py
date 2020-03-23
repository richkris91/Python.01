from Modules_01.validator_01 import validator
print('''Welcome to '0.1 Royal Multitool',
to access one of the given functions enter a representative number
1): Square maker,
2): Egyptian special,
3): Dog age
''')
input_1 = input(': ')
if validator(input_1) and 0 < int(input_1) <= 3:
    number = int(input_1)
    if number == 1:
        print('You have chosen the Square maker ')
        input_Square = input('Enter square height/length: ')
        if validator(input_Square):
            x_1 = int(input_Square)
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
            print('You have not managed to enter the input correctly')
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
    else:
        print('You have not entered a correct number')
