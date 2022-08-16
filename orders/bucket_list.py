from ast import arg


class Bucketlist():
    '''Stores a bucketlist populated with objects'''
    def __init__(self, *args):
        self.__lst = list(args)

    def get_lst(self):
        '''Returns a bucketlist as a dictionary'''
        tmp = {}
        for product in set(self.__lst):
            tmp[product.get_name()] = {'qnt': self.__lst.count(product), 'price': product.get_price()}
        return tmp

    def cost(self):
        '''Returns the total cost of the bucketlist'''
        return round(sum([i.get_price() for i in self.__lst]), 2)

    def remove_item(self, *args):
        '''Removes one or more items from the bucketlist by providing a product object'''
        items = self.__lst
        for item_to_remove in args:
            items.remove(item_to_remove)

    def __str__(self):
        lst = ''
        for product, qnt in self.get_lst().items():
            lst += f'{product} x{qnt["qnt"]}, '
        return f'[+] Bucketlist: {lst[:-2]}'
