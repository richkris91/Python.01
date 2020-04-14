def hello_(name: str = 'Kris') -> None:
    print("Hello " + name)


class Car(object):
    def __init__(self, brand: str, colour: str, capacity: float, nett_cost: float):
        self.brand = brand
        self.colour = colour
        self.capacity = capacity
        self.nett_cost = nett_cost
        self.__vat = 34
        self.__gross_cost = self.nett_cost + self.nett_cost * self.__vat/100

    def present(self):
        return 'Its brand new ' + self.brand + ' ' + self.colour + ' with ' + str(
            self.capacity) + ' cubic cm capacity for only ' + str(self.nett_cost) + '!'

    def buy(self):
        print('Congratulations, You have bought ' + self.brand + ' for only ' + str(self.__gross_cost) + ' pounds!')


car1 = Car('BMW_x6', 'black', 6592, 240000.00)
# print(car1.__vat)
# print(car1.__gross_cost)
print(car1.present())
car1.buy()
