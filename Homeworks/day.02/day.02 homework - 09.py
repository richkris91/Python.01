num = input('Enter Your number')
if float(num) == 0:
    print('You are not allowed to divide by 0')
elif float(num)%3 == 0 and float(num)%5 == 0 and float(num)%7 == 0:
    print('Your number can be divided by 3,5and 7')
else:
    print("Your number can't be divided by 3, 5 and 7")