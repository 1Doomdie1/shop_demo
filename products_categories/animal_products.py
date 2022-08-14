from .item import Item


class Animal_products(Item):
    '''
    General products that can be obtained from an animal.\n
    Should be used if there is no predefined class.\n
    Parrent class <Item>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, expiration_date: str):
        super().__init__(name, price, IBAN)
        self.__expiration_date = expiration_date

    def get_expiration_date(self):
        '''Returns the expiration date the product.'''
        return self.__expiration_date

    def __str__(self):
        return super().__str__() + f'[+] Expiration date: {self.__expiration_date}\n'


class Meat(Animal_products):
    '''
    Creates an object that stores meat products information derived from any animal.\n 
    Parrent class <Animal_products>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity

    def get_qunatity(self):
        '''Returns the product quantity.'''
        return self.__quantity

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}'


class Eggs(Animal_products):
    '''
    Creates an object that stores egg porducts information.\n 
    Parrent class <Animal_products>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, inc_type: str, box_size: int, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__inc_type = inc_type
        self.__box_size = box_size

    def get_inc_type(self):
        '''Returns the product incubation type (A, B, C, D, E, F).'''
        return self.__inc_type

    def get_box_size(self):
        '''Returns the product box size.'''
        return self.__box_size

    def __str__(self):
        return super().__str__() + f'[+] Incubation Type: {self.__inc_type}\n'\
            f'[+] Box Size: {self.__box_size}'


class Milk(Animal_products):
    '''
    Creates an object that stores milk products information.\n 
    Parrent class <Animal_products>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, fatness: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity
        self.__fatness = fatness

    def get_qunatity(self):
        '''Returns the product quantity.'''
        return self.__quantity

    def get_fatness(self):
        '''Returns the product fatness percenage.'''
        return self.__fatness

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}L\n'\
            f'[+] Fatness: {self.__fatness}%'


class Cheese(Animal_products):
    '''
    Creates an object that stores cheese products information.\n 
    Parrent class <Animal_products>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, fatness: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity
        self.__fatness = fatness

    def get_quantity(self):
        '''Returns the product quantity.'''
        return self.__quantity

    def get_fatness(self):
        '''Returns the product fatness percenage.'''
        return self.__fatness

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}kg\n'\
            f'[+] Fatness: {self.__fatness}%'


class Ice_cream(Animal_products):
    '''
    Creates an object that stores ice cream products information.\n 
    Parrent class <Animal_products>.
    '''
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity

    def get_qunatity(self):
        '''Returns the product quantity.'''
        return self.__quantity

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}g'
