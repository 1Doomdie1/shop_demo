from orders import *
from clients import *
from database import *
from products_categories import *

def test_client_address():
    city_town = 'London'
    postcode = 12345
    street_name = 'Lonon Bridge'
    street_number = 1
    block_number = 12
    floor = 1
    apartment = 20

    # Create an Address object
    cl_addr = Address(city_town, postcode, street_name, street_number, block_number, floor, apartment)
    
    # Print object contents
    # print(cl_addr)

    # Return address data as a dictionary
    address_data = cl_addr.get_address_data()
    # print(address_data)

    # Returns individual attributes
    cl_city = cl_addr.get_city()
    cl_postcode = cl_addr.get_postcode()
    cl_street_name = cl_addr.get_street_name()
    cl_street_number = cl_addr.get_street_number()
    cl_block_number = cl_addr.get_block_number()
    cl_floor = cl_addr.get_floor()
    cl_apartment = cl_addr.get_apartment()
    # print(cl_city, cl_postcode, cl_street_name, cl_street_number, cl_block_number, cl_floor, cl_apartment)

def test_client():
    cl_address = Address('London', 12345, 'London Bridge', 1, 12, 1, 20)
    cl = Client(1, 'John Doe', cl_address)

    # Print object contents
    # print(cl)

    # Return client data as a dictionary
    cl_data = cl.get_client_data()
    # print(cl_data)
    
    # Get individual Client attribute
    cl_id = cl.get_id()
    cl_name = cl.get_name()
    cl_addr_object = cl.get_address_obj() # This will return a Address object. With this you could get more attributes individualy.
    # For cl_addr_object I used the get_address_data() method to get the address dictionary
    # but you could get all the address attributes using it's methods outlined in test_client_address
    # print(cl_id, cl_name, cl_addr_object.get_address_data()) 

def test_product():
    # Create an object with all exiting classes in this project.
    chicken_breast = Meat('Chicken Breast', 14.99, 3456, 1.5, '12/12/2022')
    eggs = Eggs('Chicken Eggs', 4.65, 3213, 'A', 12, '13/01/2022')
    milk = Milk('Milk', 10.0, 2345, 1.5, 12, "12/12/2022")
    cheese = Cheese('Napolact Cheese', 3.25, 3627, 0.5, 12, '12/12/2022')
    ice_cream = Ice_cream('Vanilla Ice cream', 15.0, 5654, 0.3, '12/12/2022')
    bread = Bakery('French Bread', 3.5, 4892, 0.5, '12/12/2022')
    whiskey = Alcohol('Whiskey', 20.0, 6543, 0.7, 35)
    cola = Non_Alcohol('Coca-Cola', 3.99, 7642, 0.3, True)
    apples = Fruits_and_vegetables('Rabbit Apples', 2.0, 8290, '09/12/2022', '15/12/2022')
    cigarettes = Tabaco('Some cigarettes', 15.99, 9836, 9)

    # Print any object
    # print(chicken_breast)

    # Get a dictionary back containing relevant product data
    # print(chicken_breast.get_product_data())

    # Get individual attributes via methods
    # print(chicken_breast.get_price())

    # Each object might have more methods so please use print(dir(obj_name))
    # print(dir(chicken_breast))

def test_order():
    # Define address and client object
    cl_addr = Address('London', 12345, 'London Bridge', 1, 12, 1, 20)
    cl = Client(61253, 'Doomdie', cl_addr)

    # Create some items 
    chicken_breast = Meat('Chicken Breast', 14.99, 3456, 1.5, '12/12/2022')
    eggs = Eggs('Chicken Eggs', 4.65, 3213, 'A', 12, '13/01/2022')
    milk = Milk('Milk', 10.0, 2345, 1.5, 12, "12/12/2022")

    # Create a bucketlist object
    cl_bucketlst = Bucketlist(chicken_breast, eggs, eggs, milk, milk)
    # Print the bucket list cocntents
    # print(cl_bucketlst)

    # You can get different attributes of the bucketlist.
    cost = cl_bucketlst.cost()
    lst = cl_bucketlst.get_lst()
    # print(cost)
    # print(lst)

    # You can remove a product from the bucketlist by providing the object
    # Note that we havev milk added 2 times in the bucketlist
    cl_bucketlst.remove_item(milk)
    # print(cl_bucketlst)

    # After we remove the milk object there still is one milk object.
    # For now the only way to remove any multiple objects is by using the remove_item method like so:
    cl_bucketlst.remove_item(eggs, eggs)
    # print(cl_bucketlst)

    # Create an Order object that contains a Client and Address object
    cl1_order = Order(cl, cl_bucketlst)

    # Print contents of the order
    # print(cl1_order)

    # You can get different attributes.
    total_cost = cl1_order.total_cost()
    bucketlist = cl1_order.get_bucket_list()
    cl_data = cl1_order.get_client_data()
    # print(total_cost)
    # print(bucketlist)
    # print(cl_data)

    # You can use the archive_order() method to save the order to a history file.
    # cl1_order.archive_order()


def test_sql():
    # This is an example that you can run after you created a database.
    
    # Create a DB handler object and select your desired db
    # You can pass other argumets inside this object but I try keep it simple for now
    db = DBHandler(database='store')
    
    # Connect to the database
    db.connect()

    # Create a cursor
    cursor = db.cursor

    # Disconnect from database.
    # Using the disconnect method will distroy the cursor as well
    db.disconnect()

def main():
    # Please feel free to uncomment any of those test funtions to see the output.
    # Inside those functions there are commented print statements, plese uncommnet them and run the code.

    # test_client_address()
    # test_client()
    # test_product()
    # test_order()
    # test_sql() # First create a mysql dummy db and then run this code.
    exit(0)
if __name__ == '__main__':
    main()
