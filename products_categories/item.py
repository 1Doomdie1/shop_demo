class Item():
    def __init__(self, name, price, IBAN):
        self.__name = name
        self.__price = price
        self.__IBAN = IBAN

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_IBAN(self):
        return self.__IBAN

    def __str__(self):
        return f'[+] Name: {self.__name}\n'\
            f'[+] Price: {self.__price}£\n'\
            f'[+] IBAN: {self.__IBAN}\n'
