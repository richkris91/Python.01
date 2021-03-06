import copy

rly = [1, 2, 3]
# Tile Graphics
Tile_sets = {
    'Short_Grass_1': [
        '~~~~~~~~~~~~',
        '~~~~~~~~~~~~',
        '~~~~~~~~~~~~',
        '~~~~~~~~~~~~',
        '~~~~~~~~~~~~',
        '~~~~~~~~~~~~']
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

    def show_ter(self):
        return self.graphic


# Weapons
class weapon(object):
    def __init__(self, name,
                 hand_space, reach,
                 dmg, penetration, accuracy, block_mod,
                 weight,
                 prize,
                 material,
                 graph):
        # name
        self.type = weapon
        self.name = name
        # hand_space, reach and material
        self.hand_space = hand_space
        self.reach = reach
        self.material = material
        # combat parameters
        self.dmg = dmg
        self.penetration = penetration
        self.block_mod = block_mod
        self.accuracy = accuracy
        # Rest
        self.prize = prize
        self.weight = weight
        self.graph = graph

    def return_graph(self):
        return self.graph

    def return_type(self):
        return self.type

    def return_all(self):
        re_all = [
            self.name, self.hand_space, self.reach, self.dmg, self.penetration,
            self.accuracy, self.block_mod, self.weight, self.prize, self.graph
        ]
        return re_all

    def show_all(self):
        return self.name + ': it is a: ' + str(self.hand_space) + ' handed weapon, with reach of: ' + str(self.reach) + \
               ' and it costs: ' + str(self.prize) + ' by default.\n' + '+' * 30 + '\n' + \
               'It can apply: ' + str(self.dmg) + ' dmg, and has: ' + str(self.penetration) + \
               ' penetration ratio and: ' + str(self.accuracy) + ' accuracy block\n' + \
               'It allows its wielder to block: ' + str(self.block_mod) + \
               ' out of 100 times.\n' + 'It weights: ' + str(self.weight) + ' .'

    def show_name(self):
        return self.material[1] + ' ' + str(self.name)

    def show_hand_space(self):
        return self.hand_space

    def show_speed_mod(self):
        return self.weight

    def show_prize(self):
        return self.prize

    def set_material(self, material_mod, material_name):
        self.material[0] = material_mod
        self.material[1] = material_name


class armour(object):
    def __init__(self, name, def_mod, attack_mod, speed_mod, material, graph):
        self.name = name
        self.material = material
        self.def_mod = def_mod
        self.speed_mod = speed_mod
        self.attack_mod = attack_mod
        self.type = armour
        self.graph = graph

    def return_graph(self):
        return self.graph

    def return_type(self):
        return self.type

    def return_all(self):
        re_all = [
            self.name, self.def_mod, self.attack_mod, self.speed_mod, self.graph
        ]
        return re_all

    def show_name(self):
        return self.material[1] + ' ' + str(self.name)

    def show_mods(self):
        mods = [self.def_mod, self.attack_mod, self.speed_mod]
        return mods

    def set_material(self, mod, name):
        self.material = [mod, name]


# Squads
class squad(object):
    def __init__(self, player, unit_placement, squad_formation, desc=None, graphics=None, name=None, obj_graph=None,
                 squad_movement=None):
        self.player = player
        self.squad_formation = squad_formation
        self.name = name
        self.unit_placement = unit_placement
        self.desc = desc
        self.graphics = graphics
        self.obj_graph = obj_graph
        self.squad_movement = squad_movement
        self.average_vigour = None
        self.average_morale = None

    def show_num(self):
        return self.player

    def set_obj_graph(self, new_graph):
        self.obj_graph = new_graph

    def show_ter(self):
        # Name
        if len(self.name) < 2:
            name_2 = ' '
        else:
            name_2 = str(self.name[1])
        # Weapon_g
        w4 = '.'
        w1 = self.obj_graph[0][0]
        w2 = self.obj_graph[0][1]
        w3 = self.obj_graph[0][2]
        if len(self.obj_graph[0]) > 3:
            w4 = self.obj_graph[0][3]
        # Armour_g
        a1 = self.obj_graph[1][0]
        # Shield_g
        s1 = '.'
        if len(self.obj_graph) > 2:
            s1 = self.obj_graph[2][0]
        # Unit_g
        u_g = self.graphics
        # Unit_n_g
        unit_n = 0
        for key in self.unit_placement:
            unit_n += len(self.unit_placement[key])
        ng = str(unit_count_to_str(unit_n))
        # Finale
        row_1 = w1 + '.ranks' + self.squad_formation + '.' + self.name[0] + name_2 + '.'
        row_2 = w2 + u_g[0] + a1
        row_3 = w3 + u_g[1] + '.'
        row_4 = w4 + u_g[2] + s1
        row_5 = '.' + u_g[3] + '.'
        row_6 = '.' + ng + '.'
        sq_graph = [row_1, row_2, row_3, row_4, row_5, row_6]
        return sq_graph

    def set_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

    def show_desc(self):
        return self.desc

    def move(self, where):
        pass

    def squad_value_turn_reset(self):
        # Movement
        if self.squad_movement is None:
            self.squad_movement = self.unit_placement['R'][0].set_squad_movement()
        self.squad_movement[1] = self.squad_movement[0]
        # Speed mod
        speed_mod = 0
        # Vigour
        Vigor = 0
        u_count_0 = 0
        for key in self.unit_placement:
            for element in range(len(self.unit_placement[key])):
                Vigor += self.unit_placement[key][element].show_vigor()
                u_count_0 += 1
        average_vigour = Vigor / u_count_0
        self.average_vigour = average_vigour
        # Vigour modifier
        if average_vigour >= 8:
            speed_mod -= 2
            if average_vigour >= 4:
                speed_mod -= 2
        # Morale
        Morale = 0
        u_count_1 = 0
        for key in self.unit_placement:
            for element in range(len(self.unit_placement[key])):
                Morale += self.unit_placement[key][element].show_morale()
                u_count_1 += 1
        average_morale = Morale / u_count_1
        self.average_morale = average_morale
        self.squad_movement[1] += speed_mod

    def squad_report(self):
        return str(self.name) + ' : ' + self.squad_formation + ' : ' + self.average_vigour


class unit(object):
    def __init__(self, name,
                 size, sq_size,
                 combat_skill,
                 Morale, Hp,
                 Movement, Strength, Vigor,
                 objects,
                 graph,
                 hand_space=2):
        self.name = name
        self.size = size
        self.sq_size = sq_size
        self.combat_skill = combat_skill
        self.Morale = Morale
        self.Hp = Hp
        self.Movement = Movement
        self.Strength = Strength
        self.Vigor = Vigor
        self.objects = objects
        self.hand_space = hand_space
        self.graph = graph

    def show_graph(self):
        return self.graph

    def show_sq_size(self):
        return self.sq_size

    def show_name(self):
        return self.name

    def add_weapon(self, weapon_obj):
        self.objects['weapon'].append(weapon_obj)
        self.hand_space -= weapon_obj.show_hand_space()
        self.Strength -= weapon_obj.show_speed_mod()

    def set_squad_movement(self):
        return [self.Movement, 0]

    def show_vigor(self):
        return self.Vigor

    def show_morale(self):
        return self.Morale

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

    def set_objects(self, new_objects):
        self.objects = new_objects


class formation(object):
    def __init__(self, name, sign,
                 form_cost, stability,
                 move_mod,
                 attack_mod_1, def_mod_1,
                 attack_mod_2, def_mod_2):
        self.name = name
        self.sign = sign
        self.form_cost = form_cost
        self.stability = stability
        self.move_mod = move_mod
        self.attack_mods = [attack_mod_1, attack_mod_2]
        self.def_mod = [def_mod_1, def_mod_2]


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
        counter_t_o_b = 1
        counter_t_o_a = 1
        if 'Obj' in key:
            while counter_t_o_a != 20:
                Tiles[key][0]['Obj_' + str(counter_t_o)] = []
                counter_t_o += 1
                counter_t_o_a += 1
                if counter_t_o_a != 20:
                    Tiles[key][0]['Bor_' + str(counter_t_o_b)] = []
                    counter_t_o_b += 1
                    counter_t_o_a += 1
        if 'Bor' in key:
            while counter_t_b != 11:
                Tiles[key][0]['Bor_' + str(counter_t_b)] = []
                counter_t_b += 1
        counter_t += 1
    return Tiles


def border_adder(tiles):
    add_bor = border_obj('      ')
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
    # First Line
    Index0 = ['----']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for element in letters:
        Index0.append('|___' + element + '____' + element + '___')
    Index0.append('|')
    Index0 = str(Index0).replace('[', '')
    Index0 = Index0.replace(']', '')
    Index0 = Index0.replace("'", '')
    Index0 = Index0.replace(',', '')
    Index0 = Index0.replace(' ', '')
    print(Index0)
    # Every other line
    str_num = 0
    line_num = 0
    print('====' + ('X' + ('=' * 12 + 'X') * 10))
    for key in Tiles:
        key1 = key
        row_num = 0
        if 'Obj' in key1:
            while row_num < 6:
                line = ''
                # Index1
                Index1 = ''
                if row_num == 2 or row_num == 3:
                    Index1 = '-' + str(str_num) * 2 + '-' + '|'
                    if row_num == 3:
                        str_num += 1
                elif row_num == 6:
                    Index1 = 'X==='
                else:
                    Index1 = '-' * 4 + '|'
                line += Index1
                # Rest
                new_ter = ''
                for key in Tiles[key1][0]:
                    if 'Obj' in key:
                        new_ter += Tiles[key1][0][key][-1].show_ter()[row_num]
                    elif 'Bor' in key:
                        new_ter += Tiles[key1][0][key][-1].show_ter()[row_num]
                line += new_ter + '|'
                row_num += 1
                print(line)
        else:
            new_bor = '====X'
            for key in Tiles[key1][0]:
                new_bor += '===' + Tiles[key1][0][key][0].show_ter() + '===X'
            print(new_bor)
    print('====' + ('X' + ('=' * 12 + 'X') * 10))


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


# Squad related programs
def formation_creator():
    # Formations 1name, 2sign, 3form_cost, 4stability, 5move_mod,
    # 6attack_mod_1, 7def_mod_1, 8attack_mod_2, 9def_mod_2
    formations = {}
    # Basics
    formations['Broken'] = formation('Broken', 'B', 0, 10, -2, -3, -3, -3, -3)
    formations['Lose'] = formation('Lose', 'L', 1, 10, +1, -0, -0, -0, -0)
    formations['Square'] = formation('Square', 'Q', 2, 12, -1, +2, +1, +2, +2)
    formations['Spear_head'] = formation('Spear_head', 'S', 2, 10, -1, +3, +1, +2, +1)
    # Pike, Halberd
    formations['Phalanx'] = formation('Phalanx', 'P', 3, 12, -2, 0, +3, +1, +3)
    # Shields
    formations['Shield_wall'] = formation('Shield_wall', 'W', 2, 12, -1, +2, +2, +2, +1)
    # Wild
    formations['Wild'] = formation('Wild', 'D', 1, 8, -1, +4, +3, +1, 0)
    return formations


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
    'Orc': "Give orders to gather the Biggest Army! "
}
# Races
players = {
    '1': 'Human',
    '2': 'Orc'
}
# Materials
materials = {
    'Leather': [100, 'Leather'],
    'Bronze': [140, 'Bronze'],
    'Iron': [180, 'Iron'],
    'Steel': [220, 'Steel']
}


# Units/Weapons
def print_():
    print('=' * 30)


def armour_creator():
    Chain_vest = armour('Chain vest', 30, 15, 2, [100, ''], ['#'])
    Plate_armour = armour('Plate armour', 70, 20, 5, [100, ''], ['@'])
    re_armour = [Chain_vest, Plate_armour]
    return re_armour


def weapon_creator():
    weapon_reminder = ['name', 'hand_space', 'reach', 'dmg', 'penetration', 'accuracy', 'block_mod',
                       'weight', 'prize']
    Mace = weapon('Mace', 1, 1, 16, 40, 70, 30, 2, 20, [100, ''], ['.', '*', '|', '|'])
    War_Hammer = weapon('War_Hammer', 1, 1, 16, 60, 70, 30, 3, 30, [100, ''], ['.', '#', '|', '|'])
    Axe = weapon('Axe', 1, 1, 20, 10, 70, 30, 1, 20, [100, ''], ['.', '}', '|', '|'])
    Sword = weapon('Sword', 1, 1, 14, 20, 80, 40, 2, 30, [100, ''], ['.', '/', '|', '+'])
    Long_Sword = weapon('Long_Sword', 2, 1, 24, 30, 70, 40, 4, 50, [100, ''], ['/', '|', '|', '+'])
    Pike = weapon('Pike', 2, 2, 14, 60, 60, 20, 1, 10, [100, ''], ['^', '|', '|', '|'])
    Halberd = weapon('Halberd', 2, 2, 26, 30, 60, 20, 4, 40, [100, ''], ['^', '>', '|', '|'])
    Long_Axe = weapon('Long_Axe', 2, 2, 30, 20, 60, 20, 3, 30, [100, ''], ['}', '|', '|', '|'])
    re_weapons = [Mace, War_Hammer, Axe, Sword, Long_Sword, Pike, Halberd, Long_Axe, ]
    return re_weapons


def shield_creator():
    # Shields
    Buckler = armour('Buckler', 15, 0, 1, [100, ''], ['u'])
    Shield = armour('Shield', 30, 10, 2, [100, ''], ['O'])
    Tower_shield = armour('Tower shield', 60, 40, 3, [100, ''], ['U'])
    re_shields = [Buckler, Shield, Tower_shield]
    return re_shields


def obj_array_to_dic(array):
    new_dic = {}
    for element in array:
        new_dic[element.show_name()] = element
    return new_dic


def material_obj_creator(materials, obj):
    re_array = []
    type_ = obj.return_type()
    if type_ == weapon:
        all_p = obj.return_all()
        for key in materials:
            if key != 'Leather':
                mod = materials[key][0]
                name = materials[key][1]
                material = [mod, name]
                new_obj = weapon(
                    all_p[0], all_p[1], all_p[2], all_p[3], all_p[4], all_p[5],
                    all_p[6], all_p[7], all_p[8], material, all_p[9]
                )
                re_array.append(new_obj)
    elif type_ == armour:
        all_p = obj.return_all()
        for key in materials:
            mod = materials[key][0]
            name = materials[key][1]
            material = [mod, name]
            new_obj = armour(
                all_p[0], all_p[1], all_p[2], all_p[3], material, all_p[4]
            )
            re_array.append(new_obj)
    return re_array


def material_pick(materials_):
    mat_name = ''
    weapon_mat_mod = 100
    mat_cost = 0
    chose_idiot = 1
    while chose_idiot == 1:
        materials_keys = {}
        count_mat_1 = 1
        for key in materials:
            materials_keys[str(count_mat_1)] = key
            print(
                str(count_mat_1) + ': ' + key + ': material mod :' + str(materials[key][0]) + ' cost of object :' + str(
                    materials[key][1]) + ' %')
            count_mat_1 += 1
        input_material = input('Witch material do you chose ?\n')
        for key in materials_keys:
            if input_material == key:
                weapon_mat_mod = materials[materials_keys[input_material]][0]
                mat_cost = materials[materials_keys[input_material]][1]
                mat_name = materials_keys[input_material]
                chose_idiot -= 1
        if chose_idiot != 1:
            return [weapon_mat_mod, mat_cost, mat_name]


def show_unit_re(money, chosen_unit):
    print_()
    print('You have :' + str(money) + ' gold left')
    print_()
    print(chosen_unit.show_name() + 'squad :' + str(chosen_unit.show_objects()))
    print('Units in this squad can carry ' + str(chosen_unit.show_strength()) + ' more weight units' + \
          ' and has ' + str(chosen_unit.show_hand_space()) + ' hand space left')


def unit_creator():
    objects = {
        'weapon': [],
        'armour': []
    }
    Example = ['name',
               '1size', '2sq_size',
               '3 Combat Skill',
               '4Morale', '5Hp',
               '6Movement', '7Strength', '8Vigor', '9graph']
    # Graphics
    peasant_g = ['  ///\\\\\\  ',
                 ' @ o  o @ ',
                 '  | ~  |  ',
                 '/==|++|==\\']
    mercenary_g = [' ,,,,,,,, ',
                   ' [ - ,- ] ',
                   ' \\ ==== / ',
                   '(////\\\\\\\\)']
    knight_g = [' \\\\\\\\//// ',
                ' [:=::=:] ',
                ' \\::__::/ ',
                '#/::::::\\#']
    goblin_g = ['  A,,,,A  ',
                ' \\|o >o|/ ',
                '  \\v--v/  ',
                ' /,;,,;,\\ ']
    orc_g = [' \\\\\\\\\\\\\\\\ ',
             ' \\ #  0 / ',
             '  / ^^ \\  ',
             ' [A....A] ']
    troll_g = ['/:/:||:\\:\\',
               ':\\:0::0:/:',
               ':/V-vv-V\\:',
               '\\A-A--A-A/']
    # Human
    Peasant = unit('Peasant', 1, 30, 8, 75, 20, 6, 6, 10, objects, peasant_g)
    Mercenary = unit('Mercenary', 1, 26, 13, 100, 24, 6, 8, 12, objects, mercenary_g)
    Knight = unit('Knight', 1, 20, 18, 125, 26, 8, 10, 14, objects, knight_g)
    # Orc
    Goblin = unit('Goblin', 0.75, 40, 8, 50, 24, 8, 6, 8, objects, goblin_g)
    Orc = unit('Orc', 1.25, 26, 14, 125, 36, 6, 11, 12, objects, orc_g)
    Troll = unit('Troll', 5, 6, 6, 150, 80, 4, 36, 14, objects, troll_g)
    re_units = {
        'Human': [[Peasant, 30], [Mercenary, 50], [Knight, 80]],
        'Orc': [[Goblin, 20], [Orc, 60], [Troll, 100]]
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


def create_squad(player, unit, weapon, shield, armour):
    # Object creator and squad info
    unit_list = []
    count = unit.show_sq_size()
    objects = {
        'weapon': [weapon],
        'armour': [armour]
    }
    shield_desc = ''
    if shield is not None:
        objects['weapon'].append(shield)
        shield_desc = 'and ' + shield.show_name()
    desc = unit.show_name() + ' squad, wielding ' + weapon.show_name() + ' ' + shield_desc \
           + ', armoured with ' + armour.show_name()
    while count != 0:
        new_unit = unit
        new_unit.set_objects(objects)
        unit_list.append(new_unit)
        count -= 1
    unit_placement = {
        'N': [],
        'E': [],
        'S': [],
        'W': [],
        'R': []
    }
    for element in unit_list:
        unit_placement['R'].append(element)
    formation = 'L'
    if unit.show_name() == 'Troll':
        formation = 'D'
    # Graphics
    w_g = weapon.return_graph()
    a_g = armour.return_graph()
    graphics = unit.show_graph()
    obj_graphics = [w_g, a_g]
    if shield is not None:
        s_g = shield.return_graph()
        obj_graphics.append(s_g)
    # Finale
    new_squad = squad(player, unit_placement, formation, desc, graphics)
    new_squad.set_obj_graph(obj_graphics)
    return new_squad


def unit_recruitment(race, money, units, weapons, armour):
    materials = {
        'Bronze': [100, 100],
        'Iron': [130, 150],
        'Steel': [160, 220]

    }
    shopping_cart = {}
    available_units = units[race]
    go = 1
    while go == 1:
        print_()
        if len(shopping_cart) == 0:
            print(race_recruitment[race])
        else:
            for key in shopping_cart:
                print(key + ' : ' + shopping_cart[key][0].show_name() + "'s squad " + \
                      shopping_cart[key][0].show_objects() + ' , costing you: ' + str(shopping_cart[key][1]))
        print_()
        print('You have: ' + str(money) + ' gold left')
        print_()
        print('1: Recruit new squad\n'
              '2: Remove squad from army\n'
              '0: Finish')
        command = input(': ')
        if command == '1':
            count = 1
            shop = {}
            shop_keys = []
            unit_c = 1
            chosen_unit = ''
            num = 0
            while unit_c == 1:
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
                    unit_c -= 1
            info = input('=' * 30 + '\nNow supply this squad with weapons:(Press anything to continue):')
            go_weapon = 1
            while go_weapon == 1:
                weapon_shop = {}
                weapon_keys = []
                count_w = 1
                for element in weapons:
                    print_()
                    print(str(count_w) + ' :' + element.show_all())
                    weapon_shop[str(count_w)] = [element.show_name(), element.show_prize()]
                    count_w += 1
                print_()
                for key in weapon_shop:
                    weapon_keys.append(key)
                    print(key + ': ' + weapon_shop[key][0] + "'s: cost : " + str(weapon_shop[key][1]))
                input_w = input('Which weapon do you chose?')
                if input_w in weapon_keys:
                    chosen_weapon = weapons[int(input_w) - 1]
                    print_()
                    info_1 = input('Now chose squads weapon material')
                    # Material
                    weapon_re = material_pick(materials)
                    weapon_mat = weapon_re[0] / 100
                    weapon_cost = weapon_re[1]
                    weapon_mat_name = weapon_re[2]
                    print(chosen_weapon)
                    print(str(weapon_mat) + ' ' + str(weapon_mat_name))
                    print(chosen_weapon.material)
                    chosen_weapon.set_material(weapon_mat, weapon_mat_name)
                    chosen_unit.add_weapon(chosen_weapon)
                    # Money
                    money -= weapon_shop[input_w][1] * weapon_cost / 100
                    shopping_cart[str(num)][1] += weapon_shop[input_w][1] * weapon_cost / 100
                    go_weapon -= 1
                else:
                    print('Please, try again')
            show_unit_re(money, chosen_unit)
            if chosen_unit.show_hand_space() > 0:
                pass

    return 1


def boring_squad_recruitment(units, weapons, shields, armour, race, num):
    sq_re = []
    all_w = {}
    all_a = {}
    all_s = {}
    units = units[race]
    for element in weapons:
        wm_array = material_obj_creator(materials, element)
        for element in wm_array:
            all_w[element.show_name()] = element
    for element in armour:
        am_array = material_obj_creator(materials, element)
        for element in am_array:
            all_a[element.show_name()] = element
    for element in shields:
        sm_array = material_obj_creator(materials, element)
        for element in sm_array:
            all_s[element.show_name()] = element
    if race is 'Human':
        # Peasant squads
        u_02 = create_squad(num,
                            units[0][0],
                            all_w['Bronze Mace'],
                            all_s['Bronze Buckler'],
                            all_a['Leather Plate armour'])
        sq_re.append(u_02)
        u_03 = create_squad(num,
                            units[0][0],
                            all_w['Bronze Pike'],
                            None,
                            all_a['Leather Plate armour'])
        sq_re.append(u_03)
        u_04 = create_squad(num,
                            units[0][0],
                            all_w['Iron Pike'],
                            None,
                            all_a['Leather Chain vest'])
        sq_re.append(u_04)
        # Mercenaries squad
        u_05 = create_squad(num,
                            units[1][0],
                            all_w['Iron War_Hammer'],
                            all_s['Bronze Shield'],
                            all_a['Bronze Plate armour'])
        sq_re.append(u_05)
        u_06 = create_squad(num,
                            units[1][0],
                            all_w['Iron Sword'],
                            all_s['Iron Buckler'],
                            all_a['Iron Chain vest'])
        sq_re.append(u_06)
        # Knights
        u_10 = create_squad(num,
                            units[2][0],
                            all_w['Steel Long_Sword'],
                            None,
                            all_a['Steel Plate armour'])
        sq_re.append(u_10)
        u_11 = create_squad(num,
                            units[2][0],
                            all_w['Steel Halberd'],
                            None,
                            all_a['Steel Chain vest'])
        sq_re.append(u_11)
        u_12 = create_squad(num,
                            units[2][0],
                            all_w['Steel Halberd'],
                            None,
                            all_a['Steel Chain vest'])
        sq_re.append(u_12)
        print_()
        print("Human's army has arrived")
        print_()
    elif race == 'Orc':
        # Goblin squads
        u_01 = create_squad(num,
                            units[0][0],
                            all_w['Iron Pike'],
                            None,
                            all_a['Leather Chain vest'])
        sq_re.append(u_01)
        u_02 = create_squad(num,
                            units[0][0],
                            all_w['Iron Sword'],
                            all_s['Iron Buckler'],
                            all_a['Leather Chain vest'])
        sq_re.append(u_02)
        u_04 = create_squad(num,
                            units[0][0],
                            all_w['Iron Long_Axe'],
                            None,
                            all_a['Bronze Chain vest'])
        sq_re.append(u_04)
        u_05 = create_squad(num,
                            units[0][0],
                            all_w['Bronze Pike'],
                            None,
                            all_a['Bronze Plate armour'])

        sq_re.append(u_05)
        # Orc squads
        u_06 = create_squad(num,
                            units[1][0],
                            all_w['Iron Long_Sword'],
                            None,
                            all_a['Bronze Plate armour'])
        sq_re.append(u_06)
        u_07 = create_squad(num, units[1][0],
                            all_w['Iron Halberd'],
                            None,
                            all_a['Iron Chain vest'])
        sq_re.append(u_07)
        u_08 = create_squad(num,
                            units[1][0],
                            all_w['Iron Long_Axe'],
                            None,
                            all_a['Iron Plate armour'])
        sq_re.append(u_08)
        # Ogre squads
        u_09 = create_squad(num,
                            units[2][0],
                            all_w['Bronze Mace'],
                            None,
                            all_a['Bronze Plate armour'])
        sq_re.append(u_09)
        print_()
        print('Vile forces of darkness are upon you!')
        print_()
    sq_re = numeric_squad_setter(sq_re)
    return sq_re


def numeric_squad_setter(squad_list):
    num = 0
    for element in squad_list:
        element.set_name(str(num))
        num += 1
    return squad_list


def show_players_squad(squads):
    for element in squads:
        name = element.show_name()
        print(str(name) + ': ' + element.show_desc())


def unit_count_to_str(num):
    if num <= 5:
        return '....FEW...'
    elif 5 < num <= 10:
        return '...PACK...'
    elif 10 < num <= 16:
        return '.SEVERAL..'
    elif 16 < num <= 30:
        return '...MANY...'
    elif 30 < num:
        return '..HORDE...'


def place_units_on_the_map(squad_array, blank_tiles, real_tiles, num):
    keys_l = []
    letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
    for key in letters:
        keys_l.append(key)
    stop0 = input('Now place your units on the battlefield')
    print_()
    #
    squad_dic = {}
    dic_num = 0
    for element in squad_array:
        squad_dic[str(dic_num)] = element
        dic_num += 1
    #
    can_place = []
    if num == 1:
        can_place = [0, 1, 2]
    elif num == 2:
        can_place = [7, 8, 9]
    squads_to_place = len(squad_array)
    #
    while squads_to_place != 0:
        tiles_printer(blank_tiles)
        place_u = ''
        row = ''
        fin_l = ''
        keys = []
        for key in squad_dic:
            print(str(key) + ': ' + squad_dic[key].show_desc())
            keys.append(key)
        print_()
        place_0 = 0
        while place_0 == 0:
            place_u = input('Which unit would you like to place ?:\n')
            if place_u == 'wtf':
                squads_to_place = 0
                place_0 += 1
            elif place_u in keys:
                place_0 += 1
            else:
                print('You have not managed to enter the input correctly')
        if place_u == 'wtf':
            pass
        else:
            print('You can only place your units in given rows =\n' + str(can_place))
            print_()
            place_1 = 0
            while place_1 == 0:
                row = 0
                row0 = input('Now chose your  desired row: \n')
                try:
                    row = int(row0)
                except:
                    pass
                if row in can_place:
                    place_1 += 1
                else:
                    print('You have not managed to enter the input correctly')
            print_()
            place_2 = 0
            while place_2 == 0:
                print(keys_l)
                letter = input('Now chose direct tile: \n').capitalize()
                if letter in letters:
                    place_2 += 1
                    fin_l = letters[letter]
                else:
                    print('You have not managed to enter the input correctly')
            # Logic fix
            r_row = 'Obj' + str(row + 1)
            f_col = 'Obj_' + str(fin_l)
            f_u = squad_dic[place_u]
            # Add unit obj to Tiles array
            if len(real_tiles[r_row][0][f_col]) > 1:
                print('selected tile is already occupied')
            else:
                del squad_dic[place_u]
                real_tiles[r_row][0][f_col].append(f_u)
                blank_tiles[r_row][0][f_col].append(f_u)
                squads_to_place -= 1
    return real_tiles


def players_squads_check(num, Tiles):
    squads = []
    for key in Tiles:
        key1 = key
        if 'Obj' in key1:
            for key in Tiles[key1][0]:
                if len(Tiles[key1][0][key]) > 1:
                    if int(Tiles[key1][0][key][1].show_num()) == num:
                        add_squad = copy.deepcopy(Tiles[key1][0][key][1])
                        squads.insert(int(add_squad.show_name()), add_squad)
    return squads


def vigor_to_string(vigor):
    if vigor > 8:
        return 'Fresh'
    elif 8 >= vigor > 5:
        return 'Tired'
    elif 5 >= vigor > 2:
        return 'Exhausted'
    elif vigor <= 2:
        return 'Anguished'

def morale_to_string(morale):
    if morale > 149:
        return 'Blood thirsty'
    elif 149 >= morale > 125:
        pass
def war_game():
    # Map generator
    Terrain_map = game_start()
    TILES_0 = tiles_maker()
    Tiles_1 = border_adder(TILES_0)
    Tiles_2 = terrain_adder(Tiles_1, Terrain_map)
    blank_tiles = copy.deepcopy(Tiles_2)
    #
    Tiles_F = None
    # Turn Loop
    game = 1
    Turn = 1
    current_player = ''
    player_num = 0
    # Objects stuff
    all_formations = formation_creator()
    all_armour = armour_creator()
    all_weapons = weapon_creator()
    all_shields = shield_creator()
    units = unit_creator()
    #
    player1_squads = []
    player2_squads = []
    while game == 1:
        print_()
        print('Its: ' + str(Turn) + ' Turn')
        if Turn % 2 != 0:
            current_player = 'Player 1'
            player_num = 1
            players_race = players[str(player_num)]
            print('Its ' + current_player + ' turn: ' + str(Turn) + ' , commanding ' +
                  players_race + str(race_army_title[players_race][0]))
            # Beginning turn
            if Turn <= 2:
                player1_squads = boring_squad_recruitment(units, all_weapons, all_shields, all_armour, players_race,
                                                          player_num)
                Tiles_F = place_units_on_the_map(player1_squads, blank_tiles, blank_tiles, player_num)
            # Real turn loop
            else:
                # Squad_assaign
                player1_squads = players_squads_check(player_num, Tiles_F)
                # Sow_map
                tiles_printer(Tiles_F)
                # Turn loop
            Turn += 1
            # Turn end
        else:
            current_player = 'Player 2'
            player_num = 2
            players_race = players[str(player_num)]
            print('Its ' + current_player + ' turn, commanding ' +
                  players_race + str(race_army_title[players_race][0]))
            # Beginning turn
            if Turn <= 2:
                player2_squads = boring_squad_recruitment(units, all_weapons, all_shields, all_armour, players_race,
                                                          player_num)
                Tiles_F = place_units_on_the_map(player2_squads, Tiles_2, Tiles_F, player_num)
                x = input('stop')
            else:
                player2_squads = players_squads_check(player_num, Tiles_F)
                tiles_printer(Tiles_F)
            Turn += 1
            tiles_printer(Tiles_F)


war_game()
