from .item import Item


class Drink(Item):
    '''
    Creates a Drink object that holds general drinkable product information.\n
    This class should be used only of there is no predefined class.\n
    Parrent class <Item>. 
    '''
    def __init__(self, name: str, price: float, IBAN: int, bottle_size: float):
        super().__init__(name, price, IBAN)
        self.__bottle_size = bottle_size

    def get_bottle_size(self):
        '''Returns product bottle size.'''
        return self.__bottle_size

    def __str__(self):
        return super().__str__() + f'[+] Bottle size: {self.__bottle_size}L\n'


class Alcohol(Drink):
    '''
    Creates an object that holds drinkable alcoholic drinks products information.\n
    Parrent class <Drink>
    '''
    def __init__(self, name: str, price: float, IBAN: int, bottle_size: float, alcohol_lvl: float):
        super().__init__(name, price, IBAN, bottle_size)
        self.__alcohol_lvl = alcohol_lvl

    def get_alcohol_lvl(self):
        '''Returns product alcohol percentage.'''
        return self.__alcohol_lvl

    def __str__(self):
        return super().__str__() + f'[+] Alcohol level: {self.__alcohol_lvl}%'


class Non_Alcohol(Drink):
    '''
    Creates an object that holds drinkable non-alcoholic drinks products information.\n
    Parrent class <Drink>
    '''
    def __init__(self, name: str, price: float, IBAN: int, bottle_size: float, alcohol_lvl: float, fizzy: bool = False):
        super().__init__(name, price, IBAN, bottle_size)
        self.__fizzy = fizzy

    def is_fizzy(self):
        '''Returns a boolean value if a drink is fuzzy or not.'''
        return self.__fizzy

    def __str__(self):
        return super().__str__() + f'[+] Fizzy: {self.__fizzy}'
