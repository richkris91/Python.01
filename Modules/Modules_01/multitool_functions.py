def celsius_into_fahrenheit(c):
    f = (float(c)) * 9 / 5 + 32
    print('''The formula for converting Celsius into Fahrenheit is
    x= x * 9 / 5 +32
    when x represents Celsius
    so''')
    print(str(c) + '*9/5+32=' + str(f))
    print(str(c) + ':_Celsius equals ' + str(f) + ':_Fahrenheit')
    print('End')


def fahrenheit_into_celsius(f):
    c = (float(f) - 32) / 1.8
    print('''The formula for converting Fahrenheit into Celsius is
    x = (x-32)/1.8
    when x represents Fahrenheit
    so''')
    print(str(f) + '-32)/1.8 = ' + str(c))
    print(str(f) + ':Fahrenheit equals ' + str(c) + ':Celsius')


def entry_counter():
    with open('counter_txt', "r+") as test:
        x = test.read()
        test.seek(0)
        if x == '':
            x = 0
        else:
            x = int(test.read())
            x += 1
        test.seek(0)
        test.write(str(x))
        test.seek(0)
        return test.read()


def square_maker(input_square):
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

