from orders import *
from clients import *
from products_categories import *


def main():
    cl1_addr = Address('London', 12345, 'London Bridge', 1, 12, 1, 20)
    cl1 = Client(61253, 'Doomdie', cl1_addr)

    # cl2_addr = Address('London', 12345, 'London Bridge', 1, 12, 1, 20)
    # cl2 = Client(1234, 'Doomdie', cl2_addr)

    chicken_breast = Meat('Chicken Breast', 14.99, 3456, 1.5, '12.12.2022')
    eggs = Eggs('Chicken Eggs', 4.65, 3213, 'A', 12, '12.12.2022')
    milk = Milk('Milk', 10.0, 2345, 1.5, 12, "12.12.2022")
    cheese = Cheese('Napolact Cheese', 3.25, 3627, 0.5, 12, '12.12.2022')
    ice_cream = Ice_cream('Vanilla Ice cream', 15.0, 5654, 0.3, '12.12.2022')
    bread = Bakery('French Bread', 3.5, 4892, 0.5, '12.12.2022')
    whiskey = Alcohol('Whiskey', 20.0, 6543, 0.7, 35)
    cola = Non_Alcohol('Coca-Cola', 3.99, 7642, 0.3, True)
    apples = Fruits_and_vegetables('Rabbit Apples', 2.0, 8290, '09.12.2022', '15.12.2022')
    cigarettes = Tabaco('Some cigarettes', 15.99, 9836, 9)

    cl1_products = [chicken_breast, eggs, milk, milk, cheese, ice_cream, bread, whiskey, cola, apples, cigarettes]
    # cl2_products = [bread, whiskey, whiskey, cola, apples, cigarettes]

    cl1_bucket_lst = Bucket_list(cl1_products)
    # cl2_bucket_lst = Bucket_list(cl2_products)

    cl1_order = Order(cl1, cl1_bucket_lst)
    # cl2_order = Order(cl2, cl2_bucket_lst)

    # cl1_order.archive_order()
    # cl2_order.archive_order()

if __name__ == '__main__':
    main()
