from orders import *
from clients import *
from products_categories import *


def main():
    # cl1_addr = Address('London', 12345, 'London Bridge', 1, 12, 1, 20)
    # cl1 = Client(61253, 'Doomdie', cl1_addr)

    cl2_addr = Address('London', 12345, 'London Bridge', 1, 12, 1, 20)
    cl2 = Client(1234, 'Doomdie', cl2_addr)

    milk = Milk('Milk', 10, 2345, '1.5L', 12, "12.12.2022")
    ice_cream = Ice_cream('Vanila Ice cream', 15, 5654, '300g', '12.12.2022')
    cola = Non_Alcohol('Coca-Cola', 3.99, 7642, 0.3, True)

    products = [ice_cream, milk, cola, cola, milk]
    bucket_lst = Bucket_list(products)
    order = Order(cl2, bucket_lst)
    print(order.get_client_data().get_address())
    # order.archive_order()


if __name__ == '__main__':
    main()
