import json
import base64
from time import time
from clients.address import Address
from orders.bucket_list import Bucket_list

class Order:
    '''Creates an order with the client's address and bucket list objects'''
    def __init__(self, client_data:Address, bucket_list:Bucket_list):
        self.__client_data = client_data
        self.__bucket_list = bucket_list

    def __save_order(self, order_data):
        '''Saves an order to orders_history.json by passing a order_data tuple'''
        with open('orders/history/orders_history.json', 'r+') as history_file:
            data = json.load(history_file)
            has_older_order, order_index = self.__check_client_old_orders(data)
            if has_older_order:
                data[order_index]['Orders'] += order_data['Orders']
            else:
                data.append(order_data)
            history_file.seek(0)
            json.dump(data, history_file, indent=2)

    def __check_client_old_orders(self, orders:json):
        '''Checks if a client has older orders by passing all previous orders as a json dump'''
        for order in orders:
            if order["Client ID"] == self.__client_data.get_id():
                return True, orders.index(order)
        return False, None

    def __encode_dict(self, data:dict):
        '''Returns a base64 encoded dictionary'''
        return base64.b64encode(str(data).encode('utf-8')).decode('utf-8')

    def get_client_data(self):
        '''Returns the client information object'''
        return self.__client_data

    def get_bucket_list(self):
        '''Returns the client bucket list as a tuple'''
        return self.__bucket_list.get_lst()

    def total_cost(self):
        '''Returns the client bucket list total cost'''
        return self.__bucket_list.cost()

    def archive_order(self):
        '''Saves the order object to orders_history.json'''
        order_ID = int(time())
        order_data = {"Client ID": self.__client_data.get_id(), 
                      "Orders": [{"Order ID": order_ID, 
                                  "Name": self.__client_data.get_name(), 
                                  "Address": self.__encode_dict(self.__client_data.get_address()), 
                                  "Products": self.__encode_dict(self.get_bucket_list()), 
                                  "Total": self.total_cost()}]}
        self.__save_order(order_data)

    def __str__(self):
        addr = self.__client_data.get_address()
        return f'[+] Name: {self.__client_data.get_name()}\n'\
                f'[+] Address: {addr["City/Town"]}, pc. {addr["Postcode"]}, {addr["Street Name"]} nr. {addr["Street Number"]}, bl. {addr["Block Number"]}, fl. {addr["Floor"]}, ap. {addr["Apartment"]}\n'\
                f'{self.__bucket_list.__str__()}\n'\
                f'[+] Total: {self.total_cost()}£'
