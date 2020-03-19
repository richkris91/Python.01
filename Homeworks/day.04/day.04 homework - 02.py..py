input_1= input[('Enter listed objects')]
input_2 = input('Enter how many characters make up the largest element of the list')
a = len(input_1)
def hard_part(z):
    y = []
    counter = 0
    while counter <= z:
        y.append('| ',input_1[counter])
        counter += 1
        return
    else:
        y.append('|')
        return y


hard_part("5")

