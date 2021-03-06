class Bucket_list():
    def __init__(self, lst: list):
        self.__lst = lst

    def get_lst(self):
        tmp = {}
        for product in set(self.__lst):
            tmp[product.get_name()] = {'qnt': self.__lst.count(product), 'price': product.get_price()}
        return tmp

    def cost(self):
        return round(sum([i.get_price() for i in self.__lst]), 2)

    def remove_item(self, *args):
        items = self.__lst
        for item_to_remove in args:
            items.remove(item_to_remove)

    def __str__(self):
        lst = ''
        for product, qnt in self.get_lst().items():
            lst += f'{product} x{qnt["qnt"]}, '
        return f'[+] Bucket list: {lst[:-2]}'
