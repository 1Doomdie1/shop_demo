class Bucket_list():
    def __init__(self, lst):
        self.__lst = lst

    def get_lst(self):
        return [i.get_name() for i in self.__lst]

    def cost(self):
        return sum([i.get_price() for i in self.__lst])

    def remove_item(self, *args):
        items = self.__lst
        for item_to_remove in args:
            items.remove(item_to_remove)

    def __str__(self):
        return f'[+] Bucket list: {self.get_lst()}'
