from Modules_01.validator_02 import validator
from copy import copy

Tiles = {
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
Units_1 = []
Units_2 = []


def map_making():
    counter1 = 0
    cords1 = []
    while counter1 < 10:
        cords1.append('  ' + str(counter1) + '  ')
        counter1 += 1
    print('y ^' + ''.join(cords1) + ' x >')
    for key in Tiles:
        graphics = []
        for element in Tiles[key]:
            graphics.append(element.print())
        print(str(key) + ': ' + ''.join(graphics[:]))


def adding_empty_tiles():
    for key in Tiles:
        if len(Tiles[key]) != 10:
            if Tiles[key].count(10) == 0:
                tile_add = Tile(key, 10)
                Tiles[key].append(tile_add)
            if Tiles[key].count(9) == 0:
                tile_add = Tile(key, 9)
                Tiles[key].append(tile_add)
            if Tiles[key].count(8) == 0:
                tile_add = Tile(key, 8)
                Tiles[key].append(tile_add)
            if Tiles[key].count(7) == 0:
                tile_add = Tile(key, 7)
                Tiles[key].append(tile_add)
            if Tiles[key].count(6) == 0:
                tile_add = Tile(key, 6)
                Tiles[key].append(tile_add)
            if Tiles[key].count(5) == 0:
                tile_add = Tile(key, 5)
                Tiles[key].append(tile_add)
            if Tiles[key].count(4) == 0:
                tile_add = Tile(key, 4)
                Tiles[key].append(tile_add)
            if Tiles[key].count(3) == 0:
                tile_add = Tile(key, 3)
                Tiles[key].append(tile_add)
            if Tiles[key].count(2) == 0:
                tile_add = Tile(key, 2)
                Tiles[key].append(tile_add)
            if Tiles[key].count(1) == 0:
                tile_add = Tile(key, 1)
                Tiles[key].append(tile_add)


def making_the_tiles_1_time():
    for key in Tiles:
        counter_making1 = 0
        while counter_making1 <= 9:
            add_tile = Tile(key, counter_making1)
            Tiles[key].append(add_tile)
            counter_making1 += 1


def unit_create(player, units_list, sup_class, y, x):
    if Tiles[y][x].content is None:
        del Tiles[y][x]
        number = 0
        for element in units_list:
            number += 1
        new_unit = sup_class(y, x, player, number)
        Tiles[y].insert(x, new_unit)
    else:
        print("You can't place units on each other")


class Tile(object):
    def __init__(self, y, x, content=None):
        self.content = content
        self.x = x
        self.y = y

    def print(self):
        if self.content is None:
            return '[~~~]'
        else:
            return '[' + self.content + ']'


class Unit(Tile):
    def __init__(self, y, x, hp, nr, movement, player, content=None):
        super().__init__(y, x, content)
        self.hp = hp
        self.movement = movement
        self.player = player
        self.nr = nr
        if hp == 0:
            del self

    def menu_view(self):
        text = self.print
        return text

    def move_unit(self, y, x):
        if Tiles[y][x].content is None:
            print('Its not an unit')
        if self.movement == 0:
            print("This unit does not have any leftover movement points")
        move_dir = input('How would you like to move?'
                         'Vertically or Horizontally? v or h:  ')
        if move_dir == 'v':
            up_down = input('Up or down, u or d: ')
            how_much = int(input('By how many tiles? '))
            movement_counter = 0
            if up_down == 'u':
                while self.movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[self.y + 1][x].content is None:
                            del Tiles[self.y + 1][x]
                            unit_create(self.player, Units_1, self.__class__, self.y + 1, self.x)
                            Tiles[self.y + 1][x].movement -= 1
                            del self
                            movement_counter += 1
                    else:
                        adding_empty_tiles()
            elif up_down == 'd':
                while self.movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[self.y - 1][x].content is None:
                            del Tiles[self.y - 1][x]
                            unit_create(self.player, Units_1, self.__class__, self.y - 1, self.x)
                            Tiles[self.y - 1][x].movement -= 1
                            del self
                            movement_counter += 1
                    else:
                        adding_empty_tiles()
        elif move_dir == 'h':
            left_right = input('Left or right - l or r:  ')
            how_much = int(input('By how many tiles? '))
            movement_counter = 0
            if left_right == 'l':
                while self.movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[self.y][x - 1].content is None:
                            del Tiles[self.y][x - 1]
                            unit_create(self.player, Units_1, self.__class__, self.y, self.x - 1)
                            Tiles[self.y][x - 1].movement -= 1
                            del self
                            movement_counter += 1
                    else:
                        adding_empty_tiles()
            if left_right == 'r':
                while self.movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[self.y][x + 1].content is None:
                            del Tiles[self.y][x + 1]
                            unit_create(self.player, Units_1, self.__class__, self.y, self.x + 1)
                            Tiles[self.y][x + 1].movement -= 1
                            del self
                            movement_counter += 1
                    else:
                        adding_empty_tiles()


class Goblin(Unit):
    def __init__(self, y, x, player, nr, movement=5, taken_dmg=0, hp=10, content='Gob'):
        super().__init__(y, x, hp, nr, movement, player, content)
        self.content = content
        self.hp = hp - taken_dmg
        self.nr = nr
        self.player = player


making_the_tiles_1_time()
# Actual Game
unit_create(1, Units_1, Goblin, 7, 6)
map_making()
Tiles[7][6].move_unit(7, 6)
