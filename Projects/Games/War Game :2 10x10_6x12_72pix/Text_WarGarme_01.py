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


# Weapons
class weapon(object):
    def __init__(self, name,
                 hand_space, reach,
                 raw_dmg, penetration,
                 def_mod, block_mod, speed_mod,
                 prize,
                 material=None):
        if material is None:
            material = [1, None]
        self.name = name
        self.hand_space = hand_space
        self.reach = reach
        self.material = material
        self.raw_dmg = raw_dmg + raw_dmg * int(self.material[0] / 2)
        self.penetration = penetration * self.material[0]
        self.def_mod = def_mod
        self.block_mod = block_mod
        self.prize = prize
        self.speed_mod = speed_mod

    def show_all(self):
        return self.name + ': it is a: ' + str(self.hand_space) + ' handed weapon, with reach of: ' + str(self.reach) + \
               ' and it costs: ' + str(self.prize) + ' by default.\n' + '+' * 30 + '\n' + \
               'It can apply: ' + str(self.raw_dmg) + ' dmg, and has: ' + str(
            self.penetration) + ' penetration ratio.\n' + \
               'It allows its wielder to block: ' + str(self.def_mod) + ' % of hits, and it can be blocked: ' + \
               str(self.block_mod) + ' out of 100 times.\n' + 'It weights: ' + str(self.speed_mod) + ' .'

    def show_name(self):
        material = ''
        if self.material[1] is not None:
            material = str(self.material[1])
        return material + ' ' + str(self.name)

    def show_hand_space(self):
        return self.hand_space

    def show_speed_mod(self):
        return self.speed_mod

    def show_prize(self):
        return self.prize


# Squads
class squad(object):
    def __init__(self, player, units, squad_formation, name=None):
        self.player = player
        self.units = units
        self.squad_formation = squad_formation
        self.name = name

    def show_name(self):
        return self.name

    def move(self, where):
        pass


class unit(object):
    def __init__(self, name,
                 size, sq_size,
                 Attack_skill, Defence_Skill,
                 Morale, Hp,
                 Movement, Strength, Vigor,
                 objects, hand_space=2):
        self.name = name
        self.size = size
        self.sq_size = sq_size
        self.Attack_skill = Attack_skill
        self.Defence_Skill = Defence_Skill
        self.Morale = Morale
        self.Hp = Hp
        self.Movement = Movement
        self.Strength = Strength
        self.Vigor = Vigor
        self.objects = objects
        self.hand_space = hand_space

    def show_sq_size(self):
        return self.sq_size

    def show_name(self):
        return self.name

    def add_weapon(self, weapon_obj):
        self.objects['weapon'].append(weapon_obj)
        self.hand_space -= weapon_obj.show_hand_space()
        self.Strength -= weapon_obj.show_speed_mod()

    def show_strength(self):
        return self.Strength

    def show_hand_space(self):
        return self.hand_space

    def show_objects(self):
        weapon_print = ''
        armour_print = ''
        shield_print = ''
        if len(self.objects['weapon']) >= 1:
            weapon = self.objects['weapon'][0]
            weapon_print = weapon.show_name()
        if len(self.objects['weapon']) > 1:
            shield = self.objects['weapon'][1]
            shield_print = shield.show_name()
        if len(self.objects['armour']) >= 1:
            armour = self.objects['armour'][0]
            armour_print = armour.show_name()
        return 'weapon: ' + weapon_print + ' shield: ' + shield_print + ' armour: ' + armour_print

    def add_shield(self, shield):
        self.objects['weapon'][0].append()
        self.hand_space -= shield.show_hand_space()
        self.Strength -= shield.show_speed_mod()


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


# Map printer
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
# ? bugs/features ?
race_army_title = {
    'Human': ["s' Righteous Legions"],
    'Orc': ["s' Vile Forces"]
}
race_recruitment = {
    'Human': "Your army is not ready to battle commander!",
    'Orc': "Send orders to gather the Biggest Army! "
}
# Races
players = {
    '1': 'Human',
    '2': 'Orc'
}


# Units/Weapons
def armour_creator():
    armour = {
        'Bronze Chain_mail': [100, -1, 30],
        'Bronze Plate_Armour': [150, -4, 50],
        'Iron Chain_mail': [150, -2, 60],
        'Iron Plate_Armour': [200, -4, 100]
    }
    return armour


def weapon_creator():
    weapon_reminder = ['1name', '2hand_space', '3reach', '4raw_dmg', '5penetration',
                       '6def_mod', '7block_mod', '8speed_mod', '9prize']
    Mace = weapon('Mace', 1, 1, 12, 30, 20, 30, 2, 20)
    War_Hammer = weapon('War_Hammer', 1, 1, 10, 60, 15, 20, 3, 30)
    Axe = weapon('Axe', 1, 1, 16, 10, 15, 15, 2, 20)
    Sword = weapon('Sword', 1, 1, 12, 20, 25, 15, 2, 30)
    Long_Sword = weapon('Long_Sword', 2, 1, 24, 20, 30, 30, 4, 50)
    Pike = weapon('Pike', 2, 2, 10, 60, 10, 10, 3, 10)
    Halberd = weapon('Halberd', 2, 2, 20, 20, 20, 20, 4, 40)
    Long_Axe = weapon('Long_Axe', 2, 2, 26, 20, 20, 40, 3, 30)
    re_weapons = [Mace, War_Hammer, Axe, Sword, Long_Sword, Pike, Halberd, Long_Axe, ]
    return re_weapons


def unit_creator():
    objects = {
        'weapon': [],
        'armour': []
    }
    Example = ['name',
               '1size', '2sq_size',
               '3Attack_skill', '4Defence_Skill',
               '5Morale', '6Hp',
               '7Movement', '8Strength', '9Vigor']
    # Human
    Peasant = unit('Peasant', 1, 30, 8, 10, 75, 20, 6, 6, 24, objects)
    Mercenary = unit('Mercenary', 1, 26, 13, 15, 100, 24, 8, 8, 28, objects)
    Knight = unit('Knight', 1, 20, 18, 18, 150, 26, 8, 10, 30, objects)
    # Orc
    Goblin = unit('Goblin', 0.75, 40, 6, 8, 75, 24, 10, 6, 24, objects)
    Orc = unit('Orc', 1.25, 26, 14, 14, 150, 36, 8, 10, 30, objects)
    Ogre = unit('Ogre', 6, 6, 12, 6, 200, 80, 6, 36, 30, objects)
    re_units = {
        'Human': [[Peasant, 30], [Mercenary, 50], [Knight, 80]],
        'Orc': [[Goblin, 20], [Orc, 60], [Ogre, 100]]
    }
    return re_units


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


def unit_recruitment(race, money, units, weapons, armour):
    shopping_cart = {}
    available_units = units[race]
    go = 1
    while go == 1:
        print('=' * 30)
        if len(shopping_cart) == 0:
            print(race_recruitment[race])
        else:
            for key in shopping_cart:
                print(key + ' : ' + shopping_cart[key][0].show_name() + "'s squad " + \
                      shopping_cart[key][0].show_objects() + ' , costing you: ' + str(shopping_cart[key][1]))
        print('=' * 30)
        print('You have: ' + str(money) + ' gold left')
        print('=' * 30)
        print('1: Recruit new squad\n'
              '2: Remove squad from army\n'
              '0: Finish')
        command = input(': ')
        if command == '1':
            count = 1
            shop = {}
            shop_keys = []
            for element in available_units:
                print(str(count) + ': ' + element[0].show_name() + "'s squad - costs " + str(element[1]))
                shop[str(count)] = element
                count += 1
            for key in shop:
                shop_keys.append(key)
            input_rec = input('Chose desirable squad: ')
            if input_rec not in shop_keys:
                print('Try again)')
            else:
                num = len(shopping_cart) + 1
                chosen_unit_cost = available_units[int(input_rec) - 1][1]
                chosen_unit = available_units[int(input_rec) - 1][0]
                shopping_cart[str(num)] = [chosen_unit, chosen_unit_cost]
                money -= chosen_unit_cost
                print('You have :' + str(money) + ' gold left')
                print('=' * 30)
                print(chosen_unit.show_name() + 'squad :' + str(chosen_unit.show_objects()))
                print('Units in this squad can carry ' + str(chosen_unit.show_strength()) + ' more weight units' + \
                      ' and has ' + str(chosen_unit.show_hand_space()) + ' hand space left')
                info = input('=' * 30 + '\nNow supply this squad with weapons:(Press anything to continue):')
                go_weapon = 1
                while go_weapon == 1:
                    weapon_shop = {}
                    weapon_keys = []
                    count_w = 1
                    for element in weapons:
                        print('=' * 30)
                        print(str(count_w) + ' :' + element.show_all())
                        weapon_shop[str(count_w)] = [element.show_name(), element.show_prize()]
                        count_w += 1
                    print('=' * 30)
                    for key in weapon_shop:
                        weapon_keys.append(key)
                        print(key + ': ' + weapon_shop[key][0] + "'s: cost : " + str(weapon_shop[key][1]))
                    input_w = input('Which weapon do you chose?')
                    if input_w in weapon_keys:
                        chosen_unit.add_weapon(weapons[int(input_w) - 1])
                        money -= weapon_shop[input_w][1]
                        shopping_cart[str(num)][1] += weapon_shop[input_w][1]
                        print('=' * 30)
                        print('You have :' + str(money) + ' gold left')
                        print('=' * 30)
                        print(chosen_unit.show_name() + 'squad :' + str(chosen_unit.show_objects()))
                        print('This unit can carry ' + str(chosen_unit.show_strength()) + ' more weight units' + \
                              ' and has ' + str(chosen_unit.show_hand_space()) + ' hand space left')
                    else:
                        print('Please, try again')

    return 1


def war_game():
    Terrain_map = game_start()
    TILES_0 = tiles_maker()
    Tiles_1 = border_adder(TILES_0)
    Tiles_2 = terrain_adder(Tiles_1, Terrain_map)
    tiles_printer(Tiles_2)
    # Turn Loop
    game = 1
    Turn = 1
    current_player = ''
    player_num = 0
    while game == 1:
        armour = armour_creator()
        weapons = weapon_creator()
        units = unit_creator()
        player1_money = 1000
        player2_money = 1000
        player1_squads = []
        player2_squads = []
        print('Its: ' + str(Turn) + ' Turn')
        if Turn % 2 != 0:
            current_player = 'Player 1'
            player_num = 1
            players_race = players[str(player_num)]
            print('Its ' + current_player + ' turn, commanding ' +
                  players_race + str(race_army_title[players_race][0]))
            if Turn <= 2:
                player1_squads = unit_recruitment(players_race, player1_money, units, weapons, armour)
            Turn += 1
        else:
            current_player = 'Player 2'
            player_num = 2
            players_race = players[str(player_num)]
            print('Its ' + current_player + ' turn, commanding ' +
                  players_race + str(race_army_title[players_race][0]))
            if Turn <= 2:
                player2_squads = unit_recruitment(players_race, player2_money, units, weapons, armour)
                print(player2_squads)
            Turn += 1


war_game()
