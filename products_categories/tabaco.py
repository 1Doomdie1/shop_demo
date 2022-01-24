from .item import Item


class Tabaco(Item):
    def __init__(self, name, price, IBAN, nicotine):
        super().__init__(name, price, IBAN)
        self.__nicotine = nicotine

    def get_nicotine(self):
        return self.__nicotine

    def __str__(self):
        return super().__str__() + f'[+] Nicotine level: {self.__nicotine}mg'
