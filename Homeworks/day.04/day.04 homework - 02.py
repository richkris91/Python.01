from Modules_01.Biggest_array_element import biggest_string_in_a_array
print('''Welcome to the list creator,
please enter the list components, separating them with an enter button.
To finish the list creating process enter: END''')
x = 'START'
the_list = []
while x != 'END':
    x = str(input('Enter a list component or end the process by inputting END.'))
    the_list.append(x)
else:
    the_list.remove('END')
    pass
list_size = len(the_list)
string_size = int(biggest_string_in_a_array(the_list))
final_list = []
for element in the_list:
    final_list.append('| ' + element + ' ' * (int(string_size) - len(element)))
final_list.append('|')
print(('+-' + '-' * string_size + '-') * list_size + '+')
print(*final_list)
print(('+-' + '-' * string_size + '-') * list_size + '+')
