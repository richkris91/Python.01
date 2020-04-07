from copy import copy

from Modules_01.validator_01 import validator


class Tile(object):
    def __init__(self, x, y, content):
        self.x = x
        self.y = y
        self.content = content

    def print(self):
        return str('[' + self.content + ']')

    def content(self):
        return self.content

    def replace(self, other):
        xre = copy(self.x)
        yre = copy(self.y)
        del self
        field[yre].insert(xre, other)


class Grass(Tile):
    def __init__(self, x, y, content='~~~'):
        super().__init__(x, y, content)
        self.x = x
        self.y = y
        self.content = content
class Unit(Tile):
    def __init__(self, x, y, health, player, movement, content):
        super().__init__(x, y, content)
        self.movement = movement
        self.player = health
        self.player = player
        self.content = content
        if health == 0:
            del self
        else:
            pass

    def moving(self):
        if self.movement == 0:
            print('This unit is out of moves')
        else:
            input1 = input('''vertically or horizontally ?
            v or h : ''')
            if input1 == 'v' or 'h':
                input2 = input('By how many tiles?')
                if validator(input2) and int(input2) <= self.movement:
                    if input1 == 'v':
                        counter_move = 1
                        while counter_move <= int(input2):
                            if field[self.y + 1][self.x].content == '~~~':
                                field[self.y + 1][self.x].content = self.content
                                field[self.y][self.x].content = '~~~'
                                counter_move += 1
                                self.movement -= 1
                            else:
                                print('You have chosen an occupied tile')
                    elif input1 == 'h':
                        counter1 = 1
                        while counter1 <= int(input2):
                            if field[self.y][self.x + 1].content == '~~~':
                                field[self.y][self.x + 1].content = self.content
                                field[self.y][self.x].content = '~~~'
                                counter1 += 1
                                self.movement -= 1
                            else:
                                print('You have chosen an occupied tile')




class Gob(Unit):
    def __init__(self, x, y, player, health=10, movement=6, content='Gob'):
        super().__init__(x, y, health, player, movement, content)
        self.x = x
        self.y = y
        self.health = health
        self.player = player
        self.movement = movement
        self.content = content


field = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: []
}
# Creating map for the first time
for key in field:
    counter = 0
    while counter < 10:
        counter_add = Grass(key, counter)
        field[key].append(counter_add)
        counter += 1


# Map making engine
def map_making():
    counter1 = 0
    cords1 = []
    while counter1 < 10:
        cords1.append('  ' + str(counter1) + '  ')
        counter1 += 1
    print('x >' + ''.join(cords1) + ' y ^')
    for key in field:
        graphics = []
        for element in field[key]:
            graphics.append(element.print())
        print(str(key) + ': ' + ''.join(graphics[:]))


game = 0
turns = 1
player_counter = 2
while game == 0:
    print('Turn: ' + str(turns))
    if turns % 2 != 0:
        print('Its First Player turn')
        player_counter -= 1
        player1 = 1
        map_making()
        x = input('stop')
        turns += 1
        # Units dic
        Units_1 = ['nothing']
        # Adding a unit
        input_placing_1 = input('''Select unit type
        Gob :''')
        if input_placing_1 == 'Gob':
            Units_1.append('Gob_' + str(Units_1.count('Gob')))
            input_placing_1x = int(input('Where would you like to place it? x  0 - 9'))
            if validator(input_placing_1x) and input_placing_1x <= 9:
                input_placing_1y = int(input('Where would you like to place it? y 0 - 1'))
                if validator(input_placing_1y) and input_placing_1y <= 1:
                    AddGob = Gob(input_placing_1x, input_placing_1y, player1)
                    del field[input_placing_1y][input_placing_1x]
                    field[input_placing_1y][input_placing_1x].replace(AddGob)

    else:
        print('Its Second player turn')
        player_counter += 1
        map_making()
        x = input('stop')
        turns += 1
