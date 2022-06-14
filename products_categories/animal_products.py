from .item import Item


class Animal_products(Item):
    def __init__(self, name: str, price: float, IBAN: int, expiration_date: str):
        super().__init__(name, price, IBAN)
        self.__expiration_date = expiration_date

    def get_expiration_date(self):
        return self.__expiration_date

    def __str__(self):
        return super().__str__() + f'[+] Expiration date: {self.__expiration_date}\n'


class Meat(Animal_products):
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity

    def get_qunatity(self):
        return self.__quantity

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}'


class Eggs(Animal_products):
    def __init__(self, name: str, price: float, IBAN: int, inc_type: str, box_size: int, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__inc_type = inc_type
        self.__box_size = box_size

    def get_inc_type(self):
        return self.__inc_type

    def get_box_size(self):
        return self.__box_size

    def __str__(self):
        return super().__str__() + f'[+] Incubation Type: {self.__inc_type}\n'\
            f'[+] Box Size: {self.__box_size}'


class Milk(Animal_products):
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, fatness: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity
        self.__fatness = fatness

    def get_qunatity(self):
        return self.__quantity

    def get_fatness(self):
        return self.__fatness

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}\n'\
            f'[+] Fatness: {self.__fatness}%'


class Cheese(Animal_products):
    def __init__(self, name: str, price: float, IBAN: int, weight: float, fatness: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__weight = weight
        self.__fatness = fatness

    def get_weight(self):
        return self.__weight

    def get_fatness(self):
        return self.__fatness

    def __str__(self):
        return super().__str__() + f'[+] Weight: {self.__weight}\n'\
            f'[+] Fatness: {self.__fatness}%'


class Ice_cream(Animal_products):
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, expiration_date: str):
        super().__init__(name, price, IBAN, expiration_date)
        self.__quantity = quantity

    def get_qunatity(self):
        return self.__quantity

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}'
