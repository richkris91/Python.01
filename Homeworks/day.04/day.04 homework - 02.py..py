input_1 = input('Enter listed objects')
input_2 = input('Enter how many characters make up the largest element of the list')
a = len(input_1)
y = []
counter = 0
while counter <= a:
    y.append('+' + str(input_1[counter]))
    counter += 1
else:
    y.append('|')
    pass
print(('+' + '-' * int(input_2) + '+') * a)
print(y)
print(('+' + '-' * int(input_2) + '+') * a)

