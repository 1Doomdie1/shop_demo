class Address():
    '''
    This class holds information about the client's address
    '''
    def __init__(self, city_town: str, postcode: str, street_name: str, street_number: int, block_number: int, floor: int, apartment: str):
        self.__address_data = {"City/Town": city_town, "Postcode": postcode, "Street Name": street_name, "Street Number": street_number, "Block Number": block_number, "Floor": floor, "Apartment": apartment}

    def get_city(self):
        '''Returns client's City or Town data'''
        return self.__address_data["City/Town"]

    def get_postcode(self):
        '''Returns client's postcode data'''
        return self.__address_data["Postcode"]

    def get_street_name(self):
        '''Returns client's street name data'''
        return self.__address_data["Street Name"]

    def get_street_number(self):
        '''Returns client's street number data'''
        return self.__address_data["Street Number"]

    def get_block_number(self):
        '''Returns client's block number data'''
        return self.__address_data["Block Number"]

    def get_floor(self):
        '''Returns client's floor data'''
        return self.__address_data["Floor"]

    def get_apartment(self) -> int:
        '''Returns client's apartment data'''
        return self.__address_data["Apartment"]
    
    def get_address_data(self):
        '''Returns the client address as a dict'''
        return self.__address_data

    def __str__(self):
        return f"[+] City/Town: {self.__address_data['City/Town']}\n"\
                f"[+] Postcode: {self.__address_data['Postcode']}\n"\
                f"[+] Street Name: {self.__address_data['Street Name']}\n"\
                f"[+] Street Number: {self.__address_data['Street Number']}\n"\
                f"[+] Block Number: {self.__address_data['Block Number']}\n"\
                f"[+] Floor: {self.__address_data['Floor']}\n"\
                f"[+] Apartment: {self.__address_data['Apartment']}\n"\
