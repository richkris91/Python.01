def validator(maybe_a_number):
    try:
        float(maybe_a_number)/2
        1 / float(maybe_a_number)
    except ZeroDivisionError:

        return True
    except:
        return False
    else:
        return True
