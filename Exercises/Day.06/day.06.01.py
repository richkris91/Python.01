# file = open('test.txt', 'r')
# print(type(file))
# # print(file.read())
# file.seek(0)
# print(file.tell())
# file.close()
with open('test.txt', 'a+') as file_1:
    file_1.writelines(['\n a', '\n b'])
    print(file_1.read())
