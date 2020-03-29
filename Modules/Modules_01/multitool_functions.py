def validator(maybe_a_number):
    try:
        float(maybe_a_number)/2
        1 / float(maybe_a_number)
    except ZeroDivisionError:
        print('You can not enter 0 in the input')
        return False
    except:
        print('You have not managed to enter the input correctly')
        return False
    else:
        print('You have maneged to properly enter the input')
        return True


def celsius_into_fahrenheit():
    c = input('Enter degrees in celsius: ')
    if validator(input):
        f = (float(c)) * 9 / 5 + 32
        print('''The formula for converting Celsius into Fahrenheit is
        x = x * 9 / 5 + 32
        when x represents Celsius
        so''')
        print(str(c) + '*9/5+32=' + str(f))
        print(str(c) + ':_Celsius equals ' + str(f) + ': Fahrenheit')
        print('End')


def fahrenheit_into_celsius():
    f = input('Enter degrees in fahrenheit')
    if validator(input):
        c = (float(f) - 32) / 1.8
        print('''The formula for converting Fahrenheit into Celsius is
        x = (x-32)/1.8
        when x represents Fahrenheit
        so''')
        print(str(f) + '-32)/1.8 = ' + str(c))
        print(str(f) + ':Fahrenheit equals ' + str(c) + ':Celsius')


def entry_counter():
    try:
        with open('counter_txt', "r+") as test_1:
            x = test_1.read()
            test_1.seek(0)
            if x == '':
                x = 0
            else:
                x = int(test_1.read())
                x += 1
            test_1.seek(0)
            test_1.write(str(x))
            test_1.seek(0)
            return test_1.read()
    except:
        with open('counter_txt', "w") as test_2:
            test_2.write(str(0))
            test_2.seek(0)
            return test_2.read()


def square_maker():
    input_square = input('Enter square height/length ')
    x_1 = int(input_square)
    if x_1 == 1:
        print('+')
        print('End')
    else:
        print('+' + '--' * (x_1 - 2) + '+')
        for i in range((x_1 - 2)):
            print('|' + '  ' * (x_1 - 2) + '|')
        print('+' + '--' * (x_1 - 2) + '+')
        print('End')


def egyptian_special():
    input_egyptian = input('Enter pyramid height: ')
    if validator(input_egyptian):
        x_2 = int(input_egyptian)
        counter_2 = 0
        while counter_2 < x_2:
            print(' ' * 14 + ' ' * (x_2 - 1 - counter_2) + (counter_2 + 1) * '[]')
            counter_2 += 1
        print('End')

