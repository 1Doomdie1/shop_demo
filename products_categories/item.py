class Item():
    '''Parrent class that holds general information about an item.'''
    def __init__(self, name: str, price: float, IBAN: int):
        self.__name = name
        self.__price = price
        self.__IBAN = IBAN

    def get_name(self):
        '''Returns the product name'''
        return self.__name

    def get_price(self):
        '''Returns the product price'''
        return self.__price

    def get_IBAN(self):
        '''Returns the product IBAN'''
        return self.__IBAN

    def __str__(self):
        return f'[+] Name: {self.__name}\n'\
            f'[+] Price: {self.__price}£\n'\
            f'[+] IBAN: {self.__IBAN}\n'
