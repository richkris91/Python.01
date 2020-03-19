def salamander():
    input_1 = input('Enter list arguments')
    input_2 = int(input('Enter how many characters make up the largest element of the list'))
    x = len(input_1)
    y = []
    counter = 1
    while counter <= x:
        y.append('|' + input_1[counter])
        counter += 1
        return
    else:
        y.append('|')
        return[x, input_2]


print(('+' + '-' * int((salamander())[2]) + '+') * int((salamader())[2]))
print(salamander[1])
print(('+' + '-' * int((salamander())[2]) + '+') * int((salamader())[2]))