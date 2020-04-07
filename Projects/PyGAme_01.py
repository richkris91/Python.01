from typing import Dict, List, Any

print('Welcome to the lego war game')
game = True


class Tile(object):
    def __init__(self, x, y, content='~~~'):
        self.length = x
        self.height = y
        self.content = content

    def print(self):
        return str('[' + self.content + ']')


class Unit(Tile):
    def __init__(self, x, y, health, player, movement):
        super().__init__(x, y)
        movement.self = movement
        health.self = health
        player.self = player
        if health == 0:
            del self


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
for key in field:
    counter = 0
    while counter < 10:
        counter_add = Tile(key, counter)
        field[key].append(counter_add)
        counter += 1
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
