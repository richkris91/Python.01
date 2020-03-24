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

