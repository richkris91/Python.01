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
        Tiles[key].sort()


def making_the_tiles_1_time():
    for key in Tiles:
        counter_making1 = 0
        while counter_making1 <= 9:
            add_tile = Tile(key, counter_making1)
            Tiles[key].append(add_tile)
            counter_making1 += 1


def unit_creating_menu(player_counter):
    print('Select an unit witch you want to place.')
    units_list = {1: ['Goblin', Goblin, ]
                  }
    for key in units_list:
        print(str(key) + ': ' + units_list[key][0])
    unit_type_input = int(input('Witch unit would you like to recruit?'))
    if player_counter == 1:
        print('Remember you can only place units on y 0 or 1 lines')
        y = int(input('Select y line: '))
        x = int(input('Select  x line'))
        unit_create(int(player_counter), Units_1, units_list[unit_type_input][1], y, x)
    elif player_counter == 2:
        print('Remember you can only place units on y 8 or 9 lines')
        y = int(input('Select y line: '))
        x = int(input('Select  x line'))
        unit_create(int(player_counter), Units_2, units_list[unit_type_input][1], y, x)


def unit_create(player, player_units_list, sup_class, y, x):
    print(str(Tiles[y][x]))
    if Tiles[y][x].content is None:
        del Tiles[y][x]
        number = 0
        for element in player_units_list:
            number += 1
        new_unit = sup_class(y, x, int(number))
        Tiles[y].insert(x, new_unit)
        setattr(Tiles[y][x], 'nr', int(number))
        setattr(Tiles[y][x], 'player', int(player))
        Units_1.append(str(str(sup_class) + str(number)))
    else:
        print("You can't place units on each other")
    map_making()


def turn_menu():
    turn_counter = 1
    player_counter = 1
    command = None
    while command != 0:
        print('=====================================================')
        print('Its player_ ' + str(player_counter) + ' turn = ' + str(turn_counter))
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        map_making()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++')
        command = None
        while command != 0 and command != 9:
            choices_list = {1: [': Recruit an unit = 1', unit_creating_menu],
                            2: [': Move an unit = 2', moving_an_unit],
                            3: [': Attack with an unit = 3', ],
                            4: [': End turn = 9', ],
                            5: [': End Game = 0', ]
                            }
            for key in choices_list:
                print(str(key) + choices_list[key][0])
            command = int(input('What do you want to do?: '))
            print('=====================================================')
            if command != 9 and command != 0:
                if command == 1 or command == 2:
                    choices_list[command][1](player_counter)
                else:
                    choices_list[command][1]()

            elif command == 9:
                turn_counter += 1
                if player_counter == 1:
                    player_counter += 1
                else:
                    player_counter -= 1
            else:
                pass


def moving_an_unit(player_counter):
    y = int(input('Select y line unit: '))
    x = int(input('Select  x line unit'))
    if Tiles[y][x].content is None:
        print('Its not an unit')
    unit_belonging = getattr(Tiles[y][x], 'player')
    if str(unit_belonging) == str(player_counter):
        unit_movement = Tiles[y][x].movement
        if unit_movement == 0:
            print('This unit is out of moves!')
        move_dir = input("How would you like to move?"
                         "Vertically or Horizontally? v or h:  ")
        if move_dir == 'v':
            up_down = input('Up or down, u or d: ')
            how_much = int(input('By how many tiles?: '))
            movement_counter = 0
            if up_down == 'u':
                while unit_movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[y + 1][x].content is None:
                            obj_class = Tiles[y][x].__class__.__name__
                            del Tiles[y][x]
                            del Tiles[y + 1][x]
                            y += 1
                            object_u = obj_class(Tiles[y][x].return_to_move())
                            Tiles[y + 1][x].insert(object_u)
                            map_making()
                    else:
                        adding_empty_tiles()
            elif up_down == 'd':
                while unit_movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[y - 1][x].content is None:
                            obj_class = Tiles[y][x].__class__.__name__
                            new_movement = (Tiles[y][x]).__init__.__movement__ - 1
                            nr = (Tiles[y][x]).__init__.__nr__
                            hp = (Tiles[y][x]).__init__.__hp__
                            del Tiles[y][x]
                            del Tiles[y - 1][x]
                            y -= 1
                            object_d = obj_class(y, x, nr, new_movement, hp)
                            Tiles[y - 1][x].insert(object_d)
                            map_making()
                    else:
                        adding_empty_tiles()
        elif move_dir == 'h':
            left_right = input('Left or right - l or r:  ')
            how_much = int(input('By how many tiles? '))
            movement_counter = 0
            if left_right == 'l':
                while unit_movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[y][x - 1].content is None:
                            obj_class = Tiles[y][x].__class__.__name__
                            new_movement = int(getattr(Tiles[y][x], 'movement')) - 1
                            nr = int(getattr(Tiles[y][x], 'nr'))
                            hp = int(getattr(Tiles[y][x], 'hp'))
                            del Tiles[y][x]
                            del Tiles[y][x - 1]
                            x -= 1
                            object_l = obj_class(y, x, nr, new_movement, hp)
                            Tiles[y][x - 1].insert(object_l)
                            map_making()
                    else:
                        adding_empty_tiles()

            if left_right == 'r':
                while unit_movement != 0:
                    if movement_counter <= how_much:
                        if Tiles[y][x + 1].content is None:
                            obj_class = Tiles[y][x].__class__.__name__
                            new_movement = int(getattr(Tiles[y][x], 'movement')) - 1
                            nr = int(getattr(Tiles[y][x], 'nr'))
                            hp = int(getattr(Tiles[y][x], 'hp'))
                            del Tiles[y][x]
                            del Tiles[y][x + 1]
                            x += 1
                            object_r = obj_class(y, x, nr, new_movement, hp)
                            Tiles[y][x + 1].insert(object_r)
                            map_making()

                    else:
                        adding_empty_tiles()
    else:
        print('This unit does not follow four commands!')


def war_game():
    Gold_1 = 10
    Gold_2 = 10
    making_the_tiles_1_time()
    game = 0
    turn_menu()
    print('You have left the game')


class Tile(object):
    def __init__(self, y, x, content=None):
        self.t_content = content
        self.x = x
        self.y = y

    def print(self):
        if self.t_content is None:
            return '[~~~]'
        else:
            return '[' + self.t_content + ']'


class Unit(Tile):
    def __init__(self, y, x, content, hp):
        super().__init__(y, x, content)
        self.hp = hp

    def surviving(self):
        if self.hp <= 0:
            del self
    def moving(self):
        pass

class Goblin(Unit):
    def __init__(self, y, x, player=None, nr=None, movement=5, hp=10, content='Gob'):
        super().__init__(y, x, content, hp)
        self.movement = movement
        self.content = content
        self.hp = hp
        self.player = player
        self.nr = nr

# war_game()
