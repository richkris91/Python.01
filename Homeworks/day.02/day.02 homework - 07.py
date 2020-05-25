number = input('Enter your number')
if int(number) == 0:
    print("0 is an even number")
elif int(number) % 2 == 0:
    print('It is an even number')
else:
    print("It is an odd number")
