

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


print(entry_counter())
