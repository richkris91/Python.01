# Tile Graphics
Tile_sets = {
    'Short_Grass_1': [
        '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~',
        '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~',
        '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~',
        '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~',
        '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~',
        '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~', '~'
    ]
}


# Static map objects
class terrain_obj(object):
    def __init__(self, ter, move_mod=1):
        self.terrain = ter
        self.movement_modifier = move_mod

    def show_ter(self):
        return self.terrain

    def move_mod(self):
        return self.move_mod


class border_obj(object):
    def __init__(self, graphic):
        self.graphic = graphic

    def show_graphics(self):
        return self.graphic


# Squads
class squad(object):
    def __init__(self, player, units, squad_formation):
        self.player = player
        self.units = units
        self.squad_formation = squad_formation

    def move(self, where):
        pass


# Game setter
def tiles_maker():
    Tiles = {
        'Obj1': [],
        'Bor1': [],
        'Obj2': [],
        'Bor2': [],
        'Obj3': [],
        'Bor3': [],
        'Obj4': [],
        'Bor4': [],
        'Obj5': [],
        'Bor5': [],
        'Obj6': [],
        'Bor6': [],
        'Obj7': [],
        'Bor7': [],
        'Obj8': [],
        'Bor8': [],
        'Obj9': [],
        'Bor9': [],
        'Obj10': [],
    }
    counter_t = 1
    for key in Tiles:
        Tiles[key].append({})
        counter_t_o = 1
        counter_t_b = 1
        if 'Obj' in key:
            while counter_t_o != 20:
                Tiles[key][0]['Obj_' + str(counter_t_o)] = []
                counter_t_o += 1
                if counter_t_o != 20:
                    Tiles[key][0]['Bor_' + str(counter_t_o)] = []
                    counter_t_o += 1
        if 'Bor' in key:
            while counter_t_b != 11:
                Tiles[key][0]['Bor_' + str(counter_t_b)] = []
                counter_t_b += 1
        counter_t += 1
    return Tiles


def border_adder(tiles):
    add_bor = border_obj(['+', '+', '+', '+', '+', '+'])
    for key in tiles:
        key1 = key
        if 'Bor' in key1:
            for key in tiles[key1][0]:
                tiles[key1][0][key].append(add_bor)
        if 'Obj' in key1:
            for key in tiles[key1][0]:
                if 'Bor' in key:
                    tiles[key1][0][key].append(add_bor)
    return tiles


def terrain_adder(Tiles, Terrain_map):
    ter_count = 0
    for key in Tiles:
        key1 = key
        if 'Obj' in key1:
            for key in Tiles[key1][0]:
                if 'Obj' in key:
                    Tiles[key1][0][key].append(Terrain_map[ter_count])
                    ter_count += 1
    return Tiles


def tiles_printer(Tiles):
    Index = ['====']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for element in letters:
        Index.append('|___' + element + '____' + element + '___')
    Index.append('|')
    Index = str(Index).replace('[', '')
    Index = Index.replace(']', '')
    Index = Index.replace("'", '')
    Index = Index.replace(',', '')
    Index = Index.replace(' ', '')
    print(Index)
    Lines = []
    line_c = 0
    while line_c != 69:
        Lines.append([])
        line_c += 1
    counter_min = 0
    for key in Tiles:
        key1 = key
        if 'Obj' in key1:
            for key in Tiles[key1][0]:
                if_unit = len(Tiles[key1][0][key]) - 1
                if 'Obj' in key:
                    obj_graphics = Tiles[key1][0][key][if_unit].show_ter()
                    Lines[counter_min].append(list_str(obj_graphics[0:12]))
                    Lines[counter_min + 1].append(list_str(obj_graphics[12:24]))
                    Lines[counter_min + 2].append(list_str(obj_graphics[24:36]))
                    Lines[counter_min + 3].append(list_str(obj_graphics[36:48]))
                    Lines[counter_min + 4].append(list_str(obj_graphics[48:60]))
                    Lines[counter_min + 5].append(list_str(obj_graphics[60:72]))
                if 'Bor' in key:
                    bor_graphics = Tiles[key1][0][key][0].show_graphics()
                    Lines[counter_min].append(list_str(bor_graphics[0]))
                    Lines[counter_min + 1].append(list_str(bor_graphics[1]))
                    Lines[counter_min + 2].append(list_str(bor_graphics[2]))
                    Lines[counter_min + 3].append(list_str(bor_graphics[3]))
                    Lines[counter_min + 4].append(list_str(bor_graphics[4]))
                    Lines[counter_min + 5].append(list_str(bor_graphics[5]))
            counter_min += 6
        if 'Bor' in key1:
            for key in Tiles[key1][0]:
                bor_graphics = Tiles[key1][0][key][0].show_graphics()
                Lines[counter_min].append(
                    '+++' +
                    str(bor_graphics[0]) + str(bor_graphics[1]) + str(bor_graphics[2]) +
                    str(bor_graphics[3]) + str(bor_graphics[4]) + str(bor_graphics[5]) +
                    '+++' + 'X')
            counter_min += 1
    Final_Lines = []
    for element in Lines:
        element = str(element).replace(' ', '')
        element = element.replace('[', '')
        element = element.replace(']', '')
        element = element.replace("'", '')
        element = element.replace(',', '')
        element = element + '|'
        Final_Lines.append(element)
    Final_Lines.append(('=' * 12 + 'X') * 10)
    Final_line_count = 0
    for element in numbers:
        print('----|' + Final_Lines[Final_line_count])
        print('----|' + Final_Lines[Final_line_count + 1])
        print('_' + element * 2 + '_|' + Final_Lines[Final_line_count + 2])
        print('_' + element * 2 + '_|' + Final_Lines[Final_line_count + 3])
        print('----|' + Final_Lines[Final_line_count + 4])
        print('----|' + Final_Lines[Final_line_count + 5])
        print('====|' + Final_Lines[Final_line_count + 6])
        Final_line_count += 7


# Maps
def map_vanilla():
    Terrain_map = []
    counter_map_vanilla = 1
    while counter_map_vanilla != 101:
        add_terr = terrain_obj(Tile_sets['Short_Grass_1'])
        Terrain_map.append(add_terr)
        counter_map_vanilla += 1
    return Terrain_map


# Useful programs
def list_str(list_):
    list_1 = str(list_).replace(' ', '')
    list_2 = list_1.replace('[', '')
    list_3 = list_2.replace(']', '')
    list_4 = list_3.replace("'", '')
    list_5 = list_4.replace(',', '')
    return list_5


# Squads programs
def can_move(Tiles_2, key1, key2, direction):
    letters_key = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers_key = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9}
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    if direction == 'w':
        if key1 == 'A':
            return False
        if len(Tiles_2[letters[letters_key[key1] + 1]][0][key2]) == 1:
            return True
        else:
            return False
    if direction == 's':
        if key1 == 'J':
            return False
        if len(Tiles_2[letters[letters_key[key1] - 1]][0][key2]) == 1:
            return True
        else:
            return False
    if direction == 'd':
        if key2 == '10':
            return False
        if len(Tiles_2[key1][0][numbers[numbers_key[key2]]] + 1) == 1:
            return True
        else:
            return False
    if direction == 'a':
        if key2 == '1':
            return False
        if len(Tiles_2[key1][0][numbers[numbers_key[key2]]] - 1) == 1:
            return True
        else:
            return False


# The game itself
race_army_title = {
    'Human': ["s' Righteous Legions"],
    'Orc': ["s' Vile Forces"]
}
players = {
    '1': 'Human',
    '2': 'Orc'
}


def game_start():
    print('____Welcome to war game 01____\n' +
          '==============================')
    maps = {
        '1': ['Vanilla - Plain field with no mayor obstacles', map_vanilla]
    }
    for key in maps:
        print(key + ': ' + maps[key][0])
    print('=' * 30)
    map_info = 1
    while map_info == 1:
        input_map = input('Please chose one from available maps: ')
        for key in maps:
            if input_map in key:
                MAP = maps[key][1]()
                return MAP
        else:
            print('You have not managed to chose map properly')


def war_game():
    Terrain_map = game_start()
    TILES_0 = tiles_maker()
    Tiles_1 = border_adder(TILES_0)
    Tiles_2 = terrain_adder(Tiles_1, Terrain_map)
    # Turn Loop
    game = 1
    Turn = 1
    current_player = ''
    player_num = 0
    while game == 1:
        print('Its: ' + str(Turn) + ' Turn')
        if Turn % 2 != 0:
            current_player = 'Player 1'
            player_num = 1
        else:
            current_player = 'Player 2'
            player_num = 2
        players_race = players[str(player_num)]
        print('Its ' + current_player + ' turn, commanding ' +
              players_race + str(race_army_title[players_race][0]))


war_game()