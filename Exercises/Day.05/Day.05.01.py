# x = [
#    {'Name': 'Kris', 'Surname': 'Gorny'},
#    {'Name': 'Tom', 'Surname': 'Gorny'},
# ]
# for element in x:
#    print(element['Name'] + ' ' + element['Surname'])
# from Modules.salamander import hello_world
# hello_world()
# import send2trash
# send2trash.send2trash(/home/kris/Desktop/Everyting_bad)
from Modules.Modules_01.validator_01 import validator
a = input('Enter a number')
if validator(a):
    print(a)
