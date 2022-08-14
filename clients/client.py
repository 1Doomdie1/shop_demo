from .address import Address


class Client():
    '''
    Every client will be initialized with:
    '''
    def __init__(self, id: int, name: str, address: Address):
        self.__id = id
        self.__name = name
        self.__address = address

    def get_id(self):
        '''Returns client's id'''
        return self.__id

    def get_name(self):
        '''Returns client's name'''
        return self.__name

    def get_address(self):
        '''Returns client's address as Address class object'''
        return self.__address.get_address_data()

    def __str__(self):
        return f'[+] ID: {self.__id}\n'\
                f'[+] Name: {self.__name}\n'\
                f'{self.__address}'
