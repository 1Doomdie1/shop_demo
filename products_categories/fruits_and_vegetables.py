from .item import Item


class Fruits_and_vegetables(Item):
    def __init__(self, name: str, price: float, IBAN: int, packing_date: str, expiration_date: str, bio: bool = True):
        super().__init__(name, price, IBAN)
        self.__packing_date = packing_date
        self.__expiration_date = expiration_date
        self.__bio = bio

    def get_packing_date(self):
        return self.__packing_date

    def get_expiration_date(self):
        return self.__expiration_date

    def get_bio_status(self):
        return self.__bio

    def __str__(self):
        return super().__str__() + f'[+] Bio: {self.__bio}\n'\
            f'[+] Packing date: {self.__packing_date}\n'\
            f'[+] Expiration date: {self.__expiration_date}'
