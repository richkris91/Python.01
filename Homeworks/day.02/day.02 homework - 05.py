a = input('enter your rectangles height')
b = input('enter your rectangles length')
c = (int(b)-2)*'-'
d = (int(b)-2)*' '
print('+'+str(c)+'+')
print(int(a)*('|'+str(d)+'|' + '\n'  )+'+' +str(c)+ '+')