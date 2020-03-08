a = input('enter your rectangles height')
b = input('enter your rectangles length')
c = (int(b)-2)*'-'
d = (int(b)-2)*' '
print('+'+str(c)+'+')
for i in range (int(a)-2):
    print('|'+str(d)+'|')
print('+'+str(c)+'+')