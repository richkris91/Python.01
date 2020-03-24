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
