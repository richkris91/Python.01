a = float(input('Input your money'))


def money_exchanger(money):
    global q, w, e, r, t, y, u, i, o
    q = 0
    w = 0
    e = 0
    r = 0
    t = 0
    y = 0
    u = 0
    i = 0
    o = 0
    if money >= 5:
        q = int(money / 5)
        money_1 = money - 5 * q
    else:
        money_1 = money
    if money_1 >= 2:
        w = int(money_1 / 5)
        money_2 = money_1 - 2 * w
    else:
        money_2 = money_1
    if money_2 >= 1:
        e = int(money_2 / 5)
        money_3 = money_2 - 1 * e
    else:
        money_3 = money_2
    if money_3 >= 0.5:
        r = int(money_3 / 0.5)
        money_4 = money_3 - 0.5 * r
    else:
        money_4 = money_3
    if money_4 >= 0.2:
        t = int(money_4 / 0.2)
        money_5 = money_4 - 0.2 * t
    else:
        money_5 = money_4
    if money_5 >= 0.1:
        y = int(money_5 / 0.1)
        money_6 = money_5
    else:
        money_6 = money_5
    if money_6 >= 0.05:
        u = int(money_6 / 0.05)
        money_7 = money_6 - u * 0.05
    else:
        money_7 = money_6
    if money_7 >= 0.02:
        i = int(money_7)
        money_8 = money_7 - 0.02 * i
    else:
        money_8 = money_7
    o = int(money_8 / 0.01)
    return q, w, e, r, t, y, u, i, o


print('You own:{} 5, {} 2, {} 1, {} 0.5, {} 0.2, {} 0.1,'
      '{} 0.05, {} 0.02, {} 0.01'(money_exchanger(a)))