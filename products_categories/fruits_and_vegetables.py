from .item import Item


class Fruits_and_vegetables(Item):
    '''
    Creates an object that stores furits and vegetables products information.\n 
    Parrent class <Item>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, packing_date: str, expiration_date: str, bio: bool = True):
        super().__init__(name, price, IBAN)
        self.__packing_date = packing_date
        self.__expiration_date = expiration_date
        self.__bio = bio

    def get_packing_date(self):
        '''Returns product packaging date.'''
        return self.__packing_date

    def get_expiration_date(self):
        '''Returns products expiration date.'''
        return self.__expiration_date

    def get_bio_status(self):
        '''Returns a bolean value if the product is bio or not.'''
        return self.__bio

    def __str__(self):
        return super().__str__() + f'[+] Bio: {self.__bio}\n'\
            f'[+] Packing date: {self.__packing_date}\n'\
            f'[+] Expiration date: {self.__expiration_date}'
