from .item import Item


class Drink(Item):
    def __init__(self, name, price, IBAN, bottle_size):
        super().__init__(name, price, IBAN)
        self.__bottle_size = bottle_size

    def get_bottle_size(self):
        return self.__bottle_size

    def __str__(self):
        return super().__str__() + f'[+] Bottle size: {self.__bottle_size}\n'


class Alcohol(Drink):
    def __init__(self, name, price, IBAN, bottle_size, alcohol_lvl):
        super().__init__(name, price, IBAN, bottle_size)
        self.__alcohol_lvl = alcohol_lvl

    def get_alcohol_lvl(self):
        return self.__alcohol_lvl

    def __str__(self):
        return super().__str__() + f'[+] Alcohol level: {self.__alcohol_lvl}%'


class Non_Alcohol(Drink):
    def __init__(self, name, price, IBAN, bottle_size, fizzy=False):
        super().__init__(name, price, IBAN, bottle_size)
        self.__fizzy = fizzy

    def is_fizzy(self):
        return self.__fizzy

    def __str__(self):
        return super().__str__() + f'[+] Fizzy: {self.__fizzy}'
