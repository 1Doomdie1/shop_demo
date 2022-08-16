from .item import Item
from datetime import datetime


class Bakery(Item):
    '''
    Creates an object that holds general bakery product information.\n
    Parrent class <Item>
    '''
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, expiration_date: str):
        super().__init__(name, price, IBAN)
        self.__quantity = quantity
        self.__expiration_date = datetime.strptime(expiration_date, "%d/%m/%Y").date()
        self.data = {'expiration date': self.__expiration_date, 'quantity':self.__quantity}

    def get_qunatity(self):
        '''Returns the product quantity.'''
        return self.__quantity

    def get_expiration_date(self):
        '''Returns the product expiration date.'''
        return self.__expiration_date

    def get_product_data(self):
        return {**super().get_item_data(), **self.data}

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}kg\n'\
            f'[+] Expiration date: {self.__expiration_date}'
