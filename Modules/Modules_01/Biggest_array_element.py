def biggest_string_in_a_array(list1):
    biggest_str = list1[0]
    for element in range(len(list1)):
        if len(list1[element]) > len(biggest_str):
            biggest_str = list1[element]
            print('Biggest element in the list detected')
    return len(biggest_str)

