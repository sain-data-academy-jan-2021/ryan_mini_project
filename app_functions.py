#store all the functionality in here
import os
import app_data
from unittest.mock import patch

app_data.products  #brings in the lists from the data module
app_data.couriers
app_data.orders


app_data.products_file_name
app_data.couriers_file_name
app_data.orders_file_name

def system_exit():
    exit()


def yesno(): #offers the courier the oppotunity to continue using the program or not
    did_you_answer = False # by setting the question to false it means unless a correct input is uses the question will keep being re-asked
    while did_you_answer == False :
        answer = input ('\nWould you like to do anything else y/n').title()
        print(answer)
        if answer == 'Y' or answer == 'N' :
            did_you_answer = True
            if answer == 'Y':
                app_data.return_data('products', 'couriers', 'orders')
                return #returning the function allows you user to continue using the app after selecting yes
            elif answer == 'N':
                app_data.return_data('products', 'couriers', 'orders')  
                os.system('clear')
                print ('Thank You' '\nHave a Nice Day')
                system_exit()          


def list_index(item_list):
    index_list = []
    for item in item_list:
        index_list.append(item['ID'])
    return index_list 
    

def add_product():

    product_number = int(app_data.products[-1]['ID'])+1
        
    product = input("Insert New Product").title()
        
    price = float(input('Price?'))
        
    new_product = dict(ID = str(product_number), Product = product, Price = price)
    app_data.products.append(new_product)


def add_courier():
    
    courier_number = int(app_data.couriers[-1]['ID'])+1

    courier = input("Insert Courier Name").title()

    contact_number = input("Insert Courier's Contact Number")

    new_courier = dict(ID = str(courier_number), Courier = courier, Contact_Number = contact_number)
    app_data.couriers.append(new_courier)


def update_dictionary(name, number, item, item_list):
    app_data.print_table(item_list)
    update_item = input (f'Which {item} would you like to update?')
    existing_item = list_index(item_list)
    while update_item not in existing_item:
        print ('Invalid entry, please try again')
        update_item = input (f'Which {item} would you like to update?')
    for dict in item_list:
        if dict['ID'] == update_item:
            dict [f'{name}'] = input (f'Insert new {name}').title()
            dict [f'{number}'] = input (f'Insert new {number}').title()


def delete_dictionary(item, item_list):
    app_data.print_table(item_list)
    remove_item = input(f'Which {item} would you like to delete or press 0 to cancel?')
    if remove_item == '0':
        pass
    else:
        existing_item = list_index(item_list)
        while remove_item not in existing_item:
            print ('Invalid entry, please try again')
            remove_item = input(f'Which {item} would you like to delete?')
        
        for dict in item_list:
            if dict['ID'] == remove_item:
                item_list.remove(dict)


def new_order():
    
    customer_index = int(app_data.products[-1]['ID'])+1
    customer_name = input("What is your name").title()
    customer_address = input("What is your Address?").title()
    customer_phone = input("What is your telephone or mobile number?")
    
    app_data.print_table(app_data.products)
    ordered_products = []
    each_product = input ("Select a Product to add to your order or press 0 to finish")
    if each_product == '0':
        pass
    else:
        existing_product = list_index(app_data.products)
        while each_product in existing_product:
            ordered_products.append(each_product)
            each_product = input ("Select a Product to add to your order or press 0 to finish")
    
    app_data.print_table(app_data.couriers)
    courier = input("Which courier would you like to use?")
    exsisting_couriers = list_index(app_data.couriers)
    while courier not in exsisting_couriers:
        print ("Invalid entry, please try again")
        courier = input("Which courier would you like to use?")
    
    status = 'Preparing'
    new_order = dict(ID = customer_index, customer_name = customer_name, customer_address = customer_address, customer_phone = customer_phone, order = ordered_products, courier = courier, status = status)
    app_data.orders.append(new_order)


def edit_order_status():
    os.system('clear')
    app_data.print_table(app_data.orders)
    update_order_status = input ('Which order would you like to edit?')
    exsisting_orders = list_index(app_data.orders)
    while update_order_status not in exsisting_orders:
        print ("Invalid entry, please try again")
        update_order_status = input ('Which order would you like to edit?')
    for dict in app_data.orders:
        if dict['ID'] == update_order_status:
            status_loop = True
            order_status = order_status = ["Preparing", "Ready", "With Courier", "Delivered"] 
            while status_loop:
                status_question = input("Is this order preparing, ready, with courier or delivered?").title()
                if status_question in order_status:
                    dict ['status'] = status_question
                    status_loop = False
                    break
                else:
                    print('Invalid option please try again')
            break


def edit_order():
    os.system('clear')
    app_data.print_table(app_data.orders)
    edit_order = input ('Which order would you like to edit?')
    exsisting_orders = list_index(app_data.orders)
    while edit_order not in exsisting_orders:
        print ("Invalid entry, please try again")
        edit_order = input ('Which order would you like to edit?')
    for dict in app_data.orders:
        if dict['ID'] == edit_order:

            customer_name = input ('Type new name or leave blank to skip').title()
            if customer_name == '':
                pass
            else:
                dict['customer_name'] = customer_name
            
            customer_address = input ('Type new address or leave blank to skip').title()
            if customer_address == '':
                pass
            else:
                dict['customer_address'] = customer_address
            
            customer_phone = input ('Type new number or leave blank to skip')
            if customer_phone == '':
                pass
            else:
                dict['customer_phone'] = customer_phone

            app_data.print_table(app_data.couriers)
            customer_courier = input ('Input the Number of the Courier you want or leave blank to skip')
            if customer_courier == '':
                pass
            else:
                exsisting_couriers = list_index(app_data.couriers)
                while customer_courier not in exsisting_couriers:
                    print ("Invalid entry, please try again")
                    courier = input("Which courier would you like to use?")
                for courier_dict in app_data.couriers:
                    if courier_dict['ID'] == customer_courier:
                        dict['courier'] = customer_courier