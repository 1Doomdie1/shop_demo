from .item import Item


class Bakery(Item):
    def __init__(self, name: str, price: float, IBAN: int, quantity: float, expiration_date: str):
        super().__init__(name, price, IBAN)
        self.__quantity = quantity
        self.__expiration_date = expiration_date

    def get_qunatity(self):
        return self.__quantity

    def get_expiration_date(self):
        return self.__expiration_date

    def __str__(self):
        return super().__str__() + f'[+] Quantity: {self.__quantity}kg\n'\
            f'[+] Expiration date: {self.__expiration_date}'
