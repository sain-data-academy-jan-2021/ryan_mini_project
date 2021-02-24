import pymysql
import os
from dotenv import load_dotenv
import prettytable

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")



# Establish a database connection
connection = pymysql.connect(
  host,
  user,
  password,
  database
)



def print_table(item, number):
    cursor = connection.cursor()
    cursor.execute(f'SELECT {item}_ID, {item}_name, {number} FROM {item}s')
    mytable = prettytable.from_db_cursor(cursor)
    print (mytable)


def add_entry(item, number, connection):
    print_table(item, number)
    name = input (f'Insert new {item} name ').title()
    value = input (f'Insert {number} for {name}? ')
    execute_sql(connection, f'INSERT INTO {item}s ({item}_name, {number}) VALUES ("{name}", "{value}")')


def update_entry(item, number, connection):
    print_table(item, number)
    existing_ids = get_ids(item)
    while True:
        ID = input (f'Select which {item} to Update ')
        try:
            selected_id = int(ID)
        except ValueError:
            print ('Input must be a number')
            continue
    
        if int(selected_id) not in existing_ids:
            print ('Invalid entry, please try again')
            continue
        
        else: 
    
            name = input (f'Insert new {item} name or leave blank to skip ').title()
            if name == '':
                pass
            else:
                execute_sql(connection, f'UPDATE {item}s SET {item}_name = "{name}" WHERE {item}_ID = "{ID}";')
            
            value = input (f'Insert new {number} or leave blank to skip? ')
            if value == '':
                pass
            else:
                execute_sql(connection, f'UPDATE {item}s SET {number} = "{value}" WHERE {item}_ID = "{ID}";')
            break


def delete_entry(item, connection):
    if item == "product":
        print_table('product', 'product_price')
    elif item == "courier":
        print_table('courier', 'contact_number')
    
    existing_ids = get_ids(item)
    while True:
        deletion = input (f'Select the ID of the {item} you would like to delete? ')
        try:
            selected_id = int(deletion)
        except ValueError:
            print ('Input must be a number')
            continue
    
        if int(selected_id) not in existing_ids:
            print ('Invalid entry, please try again')
            continue
        
        else: 
            execute_sql(connection, f'DELETE FROM {item}s WHERE {item}_ID = {selected_id};')
            break


def print_order():
    cursor = connection.cursor()
    cursor.execute(f'SELECT order_ID, name, address, phone_number, courier_ID, status FROM orders')
    mytable = prettytable.from_db_cursor(cursor)
    print (mytable)
    
    
def view_order():
    existing_ids = get_ids('order')
    while True:
        basket = input("Which Order would you like to view?")
        try:
            selected_id = int(basket)
        except ValueError:
            print ('Order must be selected as a number')
            continue

        if int(selected_id) not in existing_ids:
            print ("Invalid entry, please try again")
            continue
        else:
            current_basket = execute_sql_select(connection, f'SELECT o.name, p.product_name FROM basket b JOIN orders o ON b.order_ID = o.order_ID JOIN products p ON b.product_ID = p.product_ID WHERE o.order_ID = "{selected_id}";')          
            products_list = []
            for row in current_basket:
                products_list.append(row[1])
            
            print('Here is your current order')
            for product in products_list:
                print(product)
            break


def add_order(connection):
    user_name = input ('Insert your name here ').title()
    user_address = input ('Insert your address here ').title()
    user_phone_number = input ('What is your contact number? ')
    
    print_table('courier', 'contact_number')
    existing_ids = get_ids('courier')
    while True:
        courier = input('Please select the number of the courier you would like to use ')
        try:
            selected_id = int(courier)
        except ValueError:
            print ('Courier must me selected by number')
            continue

        if int(selected_id) not in existing_ids:
            print ('Invalid entry please try again')
            continue

        else:
            user_courier = courier
            break
    
    os.system('clear')
    
    items = list_of_ordered_products()

    user_status = 'Pending'

    execute_sql(connection, f'INSERT INTO orders (name, address, phone_number, courier_ID, status) VALUES ("{user_name}", "{user_address}", "{user_phone_number}", "{user_courier}", "{user_status}" );')

    order_ID = execute_sql_select(connection, "SELECT MAX(order_ID) from orders")[0][0]
    for item in items:
            execute_sql(connection, f"INSERT INTO basket (order_ID, product_ID) values ('{order_ID}', '{item}');")
           

def update_order_status(connection):
    print_order()
    existing_ids = get_ids('order')
    while True:
        update_status = input('Which order would you like to update? ')
        try:
            selected_id = int(update_status)
        except ValueError:
            print ('Order must be selected as a number')
            continue

        if int(selected_id) not in existing_ids:
            print ("Invalid entry, please try again")
            continue
    
        else:
    
            status_loop = True
            order_status = order_status = ["Preparing", "Ready", "With Courier", "Delivered"] 
            while status_loop:
                status_question = input("Is this order preparing, ready, with courier or delivered? ").title()
                if status_question in order_status:
                    execute_sql(connection, f'UPDATE orders SET status = "{status_question}" WHERE order_ID = "{selected_id}";')
                    status_loop = False
                    break
                else:
                    print('Invalid option please try again')
            break


def edit_order(connection):
    while True:
        existing_ids = get_ids('order')
        print_order()
        deletion = input (f'Select the ID of the order you would like to edit or press 0 to cancel? ')
        
        if deletion == '0':
            os.system('clear')
            break     
        
        try:
            selected_id = int(deletion)
        except ValueError:
            print ('Input must be a number')
            continue
    
        if int(selected_id) not in existing_ids:
            print ('Invalid entry, please try again')
            continue

        
        else:
            while True:
                question = input ('\n' 'Select Option' '\n' '\n1. Edit Personal Information' '\n2. Edit Courier' '\n3. Edit Products' '\n0. Exit ')

                if question == '0':
                    break
                
                if question == '1':
                    customer_name = input ('Type new name or leave blank to skip ').title()
                    if customer_name == '':
                        pass
                    else:
                        execute_sql(connection, f'UPDATE orders SET name = "{customer_name}" WHERE order_ID = "{selected_id}";')
                        
                    customer_address = input ('Type new address or leave blank to skip ').title()
                    if customer_address == '':
                        pass
                    else:
                        execute_sql(connection, f'UPDATE orders SET name = "{customer_address}" WHERE order_ID = "{selected_id}";')
                    
                    customer_phone = input ('Type new number or leave blank to skip ')
                    if customer_phone == '':
                        pass
                    else:
                        execute_sql(connection, f'UPDATE orders SET name = "{customer_phone}" WHERE order_ID = "{selected_id}";')
                
                if question == '2':
                    existing_ids = get_ids('courier')
                    print_table('courier', 'contact_number')
                    while True:
                        new_courier = input("Select the number of the courier you would like to use ")

                        try:
                            selected_courier_id = int(new_courier)
                        except ValueError:
                            print ('Input must be a number')
                            continue
                    
                        if int(selected_courier_id) not in existing_ids:
                            print ('Invalid entry, please try again')
                            continue

                        else:
                            execute_sql(connection, f'UPDATE orders SET courier_ID = "{selected_courier_id}" WHERE order_ID = "{selected_id}";')
                            break

                if question == '3': 

                    current_basket = execute_sql_select(connection, f'SELECT o.name, p.product_name FROM basket b JOIN orders o ON b.order_ID = o.order_ID JOIN products p ON b.product_ID = p.product_ID WHERE o.order_ID = "{selected_id}";')          
                    products_list = []
                    for row in current_basket:
                        products_list.append(row[1])
                    
                    print('Here is your current order')
                    for product in products_list:
                        print(product)
                    
                    while True:
                        basket_question = input('Leave blank to keep this order or press 0 to delete this order and create a new one ')
                        if basket_question == '':
                            os.system('clear')
                            break
                        
                        elif basket_question == '0':
                            os.system('clear')
                            execute_sql(connection, f'DELETE FROM basket WHERE order_ID = {selected_id}')
                            items = list_of_ordered_products()
                            order_ID = selected_id
                            for item in items:
                                execute_sql(connection, f"INSERT INTO basket (order_ID, product_ID) values ('{order_ID}', '{item}');")
                            break
                        
                        else:
                            print('Invalid entry please try again')
                            continue


def delete_order(connection):
    print_order()
    existing_ids = get_ids('order')
    while True:
        deletion = input (f'Select the ID of the order you would like to delete? ')
        try:
            selected_id = int(deletion)
        except ValueError:
            print ('Input must be a number')
            continue
    
        if int(selected_id) not in existing_ids:
            print ('Invalid entry, please try again')
            continue
        
        else: 
            execute_sql(connection, f'DELETE FROM basket WHERE order_ID = {selected_id}')
            
            execute_sql(connection, f'DELETE FROM orders WHERE order_ID = {selected_id}')
            break


def execute_sql_select(connection, action):
    cursor = connection.cursor()
    cursor.execute(action)
    cursor.close()
    return cursor.fetchall()


def execute_sql(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    connection.commit()


def get_ids(item):
    existing_ids = [id[0] for id in execute_sql_select(connection, f'select {item}_id from {item}s')]
    return existing_ids


def list_of_ordered_products():
    print_table('product', 'product_price')
    existing_ids = get_ids('product')
    ordered_products = []
    while True:
        ordered_product = input ("From the list of available Products please select the number of a product you would like to add. When you are finished press 0 ")
        try:
            selected_id = int(ordered_product)
        except ValueError:
            print ('Product must be selected as a number')

        if int(selected_id) == 0:
            break

        elif int(selected_id) not in existing_ids:
            print ('Invalid entry please try again')
            continue

        else:
            ordered_products.append(selected_id)
    
    return ordered_products