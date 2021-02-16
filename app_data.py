import tabulate
import os
import csv 

#getting the list from the txt files:

products = [] #empty lists created to store the data from the csv files

couriers = []

orders = []

order_status = ["Preparing", "Ready", "With Courier", "Delivered"] 


products_file_name = 'products' #needed so the name of the csv files can be called at any point in the code without using strings
couriers_file_name = 'couriers'
orders_file_name = 'orders'


def open_files(items, item_list):
    with open(f'{items}.csv', 'r') as file:
        list = csv.DictReader(file)
        for row in list:
            item_list.append(row)

open_files(products_file_name, products)
open_files(couriers_file_name, couriers)
open_files(orders_file_name, orders)

#sending data back to txt files

def return_data(products_path, couriers_path, orders_path):

    with open(f'{products_path}.csv', mode='w') as file:
        header_names = ['ID', 'Product', 'Price']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader() 
        for row in products:
            writer.writerow(row)

    with open(f'{couriers_path}.csv', mode='w') as file:
        header_names = ['ID', 'Courier', 'Contact_Number']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader() 
        for row in couriers:
            writer.writerow(row)
    
    with open(f'{orders_path}.csv', mode='w') as file:
        header_names = ['ID', 'customer_name', 'customer_address', 'customer_phone', 'order', 'courier', 'status']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader() 
        for row in orders:
            writer.writerow(row)

def print_table(items):
    header = items[0].keys()
    rows =  [x.values() for x in items]
    print ('\n', tabulate.tabulate(rows, header))

