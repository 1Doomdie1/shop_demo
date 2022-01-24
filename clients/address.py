class Address():
    def __init__(self, city_town, postcode, street_name, street_number, block_number, floor, apartment):
        self.__address_data = {"City/Town": city_town, "Postcode": postcode, "Street Name": street_name, "Street Number": street_number, "Block Number": block_number, "Floor": floor, "Apartment": apartment}

    def get_address_data(self):
    	return self.__address_data

    def __str__(self):
        return f"[+] City/Town: {self.__address_data['City/Town']}\n"\
        		f"[+] Postcode: {self.__address_data['Postcode']}\n"\
        		f"[+] Street Name: {self.__address_data['Street Name']}\n"\
                f"[+] Street Number: {self.__address_data['Street Number']}\n"\
                f"[+] Block Number: {self.__address_data['Block Number']}\n"\
                f"[+] Floor: {self.__address_data['Floor']}\n"\
                f"[+] Apartment: {self.__address_data['Apartment']}\n"\
