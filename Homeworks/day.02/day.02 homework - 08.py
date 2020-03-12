num = input('Enter your number')
if int(num)== 0:
    print('You are not allowed to divide by 0')
elif int(num)%3 == 0 or int(num)%5 == 0 or int(num)%7 == 0:
    print('Your number can be divided by 3,5 or 7')
else:
    print("Your number can't be divided by 3, 5 or 7")
