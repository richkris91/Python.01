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

