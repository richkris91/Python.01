class terrain_obj(object):
    def __init__(self, ter, move_mod=1):
        self.terrain = ter
        if self.terrain == '~':
            self.terrain = []
            counter_ter = 36
            while counter_ter != 0:
                self.terrain.append(ter)
                counter_ter -= 1
        self.movement_modifier = move_mod

    def show_ter(self):
        return self.terrain

    def move_mod(self):
        return self.move_mod


class border_obj(object):
    def __init__(self, graphic='+'):
        self.graphic = graphic

    def show_graphic(self):
        return self.graphic


def graphic_map_creator(Input_terrain='~'):
    Terrain = Input_terrain
    # Terrain obj maker
    ter_obj = terrain_obj(Terrain)
    # Terrain Adder
    Tiles = {
        'A': [],
        'B': [],
        'C': [],
        'D': [],
        'E': [],
        'F': [],
        'G': [],
        'H': [],
        'I': [],
        'J': []
    }
    for key in Tiles:
        counter = 0
        if counter == 0:
            Tiles[key].append({})
        while counter != 10:
            Tiles[key][0][str(counter)]: [ter_obj]
            counter += 1
    # Border maker
    bor_obj = border_obj()
    # Battlefield_border_maker
    Borders = {
        'Horizontally':
            [{
                'A': [],
                'B': [],
                'C': [],
                'D': [],
                'E': [],
                'F': [],
                'G': [],
                'H': [],
                'I': [],
                'J': []
            }],
        'Vertically':
            [{
                'A': [],
                'B': [],
                'C': [],
                'D': [],
                'E': [],
                'F': [],
                'G': [],
                'H': [],
                'I': [],
                'J': []
            }]
    }
    for key in Borders['Horizontally'][0]:
        counter = 0
        if counter == 0:
            Borders['Horizontally'][0][key].append({})
        while counter != 9:
            Borders['Horizontally'][0][key][0][str(counter)]: bor_obj
            counter += 1
    for key in Borders['Vertically'][0]:
        counter = 0
        if counter == 0:
            Borders['Vertically'][0][key].append({})
        while counter != 9:
            Borders['Vertically'][0][key][0][str(counter)]: bor_obj
            counter += 1
    return [Tiles, Borders]


def map_printer():
    pass


def war_game():
    MAP = graphic_map_creator()
    map_printer()


war_game()
