class Animal(object):
    def __init__(self, age, colour, name):
        self.name = name
        self.colour = colour
        self.age = age


dog_01 = Animal(12, 'blue', 'rex')
dog_02 = Animal(0.5, 'red', 'pufflett')
array_01 = {'Dogs': [dog_01, dog_02]}
for element in array_01['Dogs'[:]]:
    print(str(element.name) + '  age: ' + str(element.age))
