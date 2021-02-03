#store all the functionality in here
import os
import app_data

app_data.products  #brings in the lists from the data module
app_data.couriers
app_data.orders


app_data.products_file_name
app_data.couriers_file_name
app_data.orders_file_name

def yesno(): #offers the courier the oppotunity to continue using the program or not
    did_you_answer = False # by setting the question to false it means unless a correct input is uses the question will keep being re-asked
    while did_you_answer == False :
        answer = input ('\nWould you like to do anything else y/n').title()
        if answer == 'Y' or answer == 'N' :
            did_you_answer = True
            if answer == 'Y':
                return #returning the function allows you user to continue using the app after selecting yes
            elif answer == 'N':
                app_data.return_data()  
                os.system('clear')
                print ('Thank You' '\nHave a Nice Day')
                exit()            
    

    
def add_product():
   
    valid_number = False
    while valid_number == False:
        product_number = len(app_data.products)+1
    
        product = input("Insert New Product").title()

        price = float(input('Price?'))
        if float(price) and price > 0:
            valid_number = True
            new_product = dict(Product_Number = product_number, Product = product, Price = price)
            app_data.products.append(new_product)
        else:
            print("price must be a number greater than 0")

def add_courier():
    
    courier_number = len(app_data.couriers)+1

    courier = input("Insert Courier Name").title

    contact_number = input("Insert Courier's Contact Number")

    new_courier = dict(Courier_Number = courier_number, Courier = courier, Contact_Number = contact_number)
    app_data.couriers.append(new_courier)


def update_item(item, item_list):
    os.system('clear')
    print ('\n'.join(item_list))
    try:
        position_item = input ('Choose numerically what you would like to update') #has to be set numerically so the item can be replaced at the same index point 
        position_item = int(position_item) -1 #int changes string to integer and must be -1 as index values start at 0
        if position_item in range (0, len(item_list)):#by setting the range to len the range will always be the same length as the list as it grows or shrinks
            item_list[position_item] = input ('What would you like to update it to?').title()
            print ('\n'.join(item_list))     
        else:
            print('Invalid entry')
    except:
        print ('Invalid entry')
    return item_list


#order stuff

def new_order():
    
    customer_name = input("What is your name").title()
    customer_address = input("What is your Address?").title()
    customer_phone = input("What is your telephone or mobile number?")
    courier = input("Which courier would you like to use?")
    status = 'Preparing'
    new_order = dict(customer_name = customer_name, customer_address = customer_address, customer_phone = customer_phone, courier = courier, status = status)
    app_data.orders.append(new_order)


def edit_order():
      
    edit_order = input ('Which order would you like to edit')
    customer_name = input ('Type new name or leave blank to skip').title()
    if customer_name == '':
        pass
    else:
        app_data.orders[int(edit_order)-1]['customer_name'] = customer_name
    customer_address = input ('Type new address or leave blank to skip').title()
    if customer_address == '':
        pass
    else:
        app_data.orders[int(edit_order)-1]['customer_address'] = customer_address
    customer_phone = input ('Type new number or leave blank to skip')
    if customer_phone == '':
        pass
    else:
        app_data.orders[int(edit_order)-1]['customer_phone'] = customer_phone
    
    new_loop = True
    while new_loop:
        print ('\n', app_data.couriers)
        courier = input ('Type new courier of leave blank to skip').title()
        if courier == '':
            new_loop = False
        elif courier not in app_data.couriers:
            print ('Invalid option, please try again')
        else:
            app_data.orders[int(edit_order)-1]['courier'] = courier
            new_loop = False
















def delete_item (item_list):
    remove_item = int(input(f'Which number would you like to delete?'))
    if remove_item not in (item_list):
        print('Invalid entry')
    else:
        item_list.remove(remove_item)