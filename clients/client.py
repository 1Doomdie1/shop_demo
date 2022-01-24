class Client():
    def __init__(self, id, name, address):
        self.__id = id
        self.__name = name
        self.__address = address

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address.get_address_data()

    def __str__(self):
        return f'[+] ID: {self.__id}\n'\
                f'[+] Name: {self.__name}\n'\
                f'{self.__address}'
