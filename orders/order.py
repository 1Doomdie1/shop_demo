import json


class Order:
    def __init__(self, client_data, bucket_list):
        self.__client_data = client_data
        self.__bucket_list = bucket_list

    def __save_order(self, order_data):
        with open('orders/history/orders_history.json', 'r+') as history_file:
            data = json.load(history_file)
            has_older_order, order_index = self.__check_client_old_orders(data)
            if has_older_order:
                data[order_index]['Orders'] += order_data['Orders']
            else:
                data.append(order_data)
            history_file.seek(0)
            json.dump(data, history_file, indent=1)

    def __check_client_old_orders(self, orders):
        for order in orders:
            if order["Client ID"] == self.__client_data.get_id():
                return True, orders.index(order)
        return False, None

    def get_client_data(self):
        return self.__client_data

    def get_bucket_list(self):
        return self.__bucket_list.get_lst()

    def total_cost(self):
        return self.__bucket_list.cost()

    def archive_order(self):
        order_ID = hash(self)
        order_data = {"Client ID": self.__client_data.get_id(), "Orders": [{"Order ID": order_ID, "Name": self.__client_data.get_name(), "Address": self.__client_data.get_address(), "Products": self.get_bucket_list(), "Total": self.total_cost()}]}
        self.__save_order(order_data)

    def __str__(self):
        addr = self.__client_data.get_address()
        return f'[+] Name: {self.__client_data.get_name()}\n'\
                f'[+] Address: {addr["City/Town"]}, pc. {addr["Postcode"]}, {addr["Street Name"]} nr. {addr["Street Number"]}, bl. {addr["Block Number"]}, fl. {addr["Floor"]}, ap. {addr["Apartment"]}\n'\
                f'[+] Ordered Products: {self.get_bucket_list()}\n'\
                f'[+] Total: {self.total_cost()}£'
