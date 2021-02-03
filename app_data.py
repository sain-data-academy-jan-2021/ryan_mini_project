#put lists and dictionaries in here
#put read files in here
#put data presisitence in here

import tabulate
import os
import csv 

#getting the list from the txt files:

products = [] #empty lists created to store the data from the txt files

couriers = []

orders = []
order_status = ["Preparing", "Ready", "With Courier", "Delivered"] 


products_file_name = 'products' #needed so the name of the csv files can be called at any point in the code without using strings
couriers_file_name = 'couriers'
orders_file_name = 'orders'

with open("products.csv", 'r') as file:
    product_list = csv.DictReader(file) 
    for row in product_list:
        products.append(row)

with open("couriers.csv", 'r') as file:
    couriers_list = csv.DictReader(file) 
    for row in couriers_list:
        couriers.append(row)


with open("orders.csv", 'r') as file:
    order_list = csv.DictReader(file) 
    for row in order_list:
        orders.append(row)


#sending data back to txt files

def return_data():

    with open('products.csv', mode='w') as file:
        header_names = ['Product_Number', 'Product', 'Price']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader() 
        for row in products:
            writer.writerow(row)

    with open('couriers.csv', mode='w') as file:
        header_names = ['Courier_Number', 'Courier', 'Contact_Number']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader() 
        for row in couriers:
            writer.writerow(row)
    
    with open('orders.csv', mode='w') as file:
        header_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        writer = csv.DictWriter(file, fieldnames=header_names)
        writer.writeheader() 
        for row in orders:
            writer.writerow(row)

def print_table(items):
    header = items[0].keys()
    rows =  [x.values() for x in items]
    print ('\n', tabulate.tabulate(rows, header))

