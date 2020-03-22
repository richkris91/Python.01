def array_printer(x):
    for element in range(len(x)):
        print(x[element] + ' ' + str(len(x[element])))


a = ['a' ,'b']
b = ['aa', 'bb']
array_printer(a)
array_printer(b)