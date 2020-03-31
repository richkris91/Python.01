from Modules_01.validator_01 import validator


def money_exchanger():
    print('Welcome to the Royal money exchanger')
    input_01 = (input('Input money: '))
    if validator(input_01):
        money = float(input_01)
        TwoPounds = 0
        OnePounds = 0
        FiftyPence = 0
        TwentyPence = 0
        TenPence = 0
        FifePence = 0
        TwoPence = 0
        OnePence = 0
        if money >= 2:
            TwoPounds = int(money/2)
            money -= TwoPounds * 2
        while money >= 1:
            money -= 1
            OnePounds += 1
        while money >= 0.5:
            money -= 0.5
            FiftyPence += 1
        while money >= 0.2:
            money -= 0.2
            FiftyPence += 1
        while money >= 0.1:
            money -= 0.1
            TwentyPence += 1
        while money >= 0.05:
            money -= 0.05
            FifePence += 1
        while money >= 0.02:
            money -= 0.02
            TwoPence += 1
        while money >= 0.01:
            money -= 0.01
            OnePence += 1
        print('You have: ' + str(TwoPounds) + ' TwoPounds')
        print('You have: ' + str(OnePounds) + ' OnePounds')
        print('You have: ' + str(FiftyPence) + ' FiftyPence')
        print('You have: ' + str(TwentyPence) + ' TwentyPence')
        print('You have: ' + str(TenPence) + ' TenPence')
        print('You have: ' + str(FifePence) + ' FifePence')
        print('You have: ' + str(TwoPence) + ' TwoPence')
        print('You have: ' + str(OnePence) + ' OnePence')
    else:
        pass

