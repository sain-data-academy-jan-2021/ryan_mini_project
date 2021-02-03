#put the actual interface in here

import os
import tabulate
import app_data
import app_functions #imports all the functionality if the seperate modules

app_data.products  #brings in the lists from the data module
app_data.couriers
app_data.orders


app_data.products_file_name
app_data.couriers_file_name
app_data.orders_file_name

def main_menu(): 
   
     #using ''' means you can write anything you want within it and that's what will be printed in the terminal
    menu = input ('''
Welcome to RSAIWDBMP v0.3

Please select an option by entering a number  
        
1. Product Menu 
2. Courier Menu 
3. Order Menu
0. Exit''') 

    if menu == '1':
        os.system('clear')
        while True:
            
            option1 = input ('\n' 'Select Option' '\n' '\n1. Products List' '\n2. Add a Product' '\n3. Update a Product'  '\n4. Remove a Product' '\n0. Main Menu')
            
            if option1 == '1':
                os.system('clear')
                app_data.print_table(app_data.products)
                app_functions.yesno()
                os.system('clear')
                continue
                    
            elif option1 == '2':
                os.system('clear')
                app_data.print_table(app_data.products)
                app_functions.add_product()
                app_functions.yesno()
                os.system('clear')
                continue

            elif option1 == '3':
                os.system('clear')
                update_product = input ('Select Option' '\n1. List of Products' '\n0. Cancel')
                if update_product == '1':
                    app_functions.update_item(update_product, app_data.products)
                    app_functions.yesno()
                    os.system('clear')
                    continue
                else:
                    os.system('clear')
                    continue

            elif option1 == '4':
                os.system('clear')
                print ('\n'.join(app_data.products))
                delete_product = input('What product would you like to remove?').title()
                app_functions.delete_item(delete_product, app_data.products)
                app_functions.yesno()
                os.system('clear')
                continue

            elif option1 == '0':
                os.system('clear')
                main_menu()

            else:
                os.system('clear')
                print ('\nInvalid input, please try again')
                continue
            
    elif menu == '2':
        os.system('clear')
        while True:

            option2 = input ('\nSelect Option' '\n' '\n1. Current Couriers' '\n2. Create New Courier' '\n3. Update Existing Courier' '\n4. Remove a Courier' '\n0. Main Menu')

            if option2 == '1':
                os.system('clear')
                app_data.print_table(app_data.couriers)
                app_functions.yesno()
                os.system('clear')
                continue

            elif option2 == '2':
                os.system('clear')
                app_data.print_table(app_data.couriers)
                app_functions.add_courier()
                app_functions.yesno()
                os.system('clear')
                continue

            elif option2 == '3':
                os.system('clear')
                update_courier = input ('Select Option' '\n1. List of Couriers' '\n0. Cancel')
                if update_courier == '1':
                    app_functions.update_item(update_courier, app_data.couriers)
                    app_functions.yesno()
                    os.system('clear')
                    continue
                else:
                    os.system('clear')
                    continue

            elif option2 == '4':
                os.system('clear')
                app_data.print_table(app_data.couriers)
                delete_courier = input ('Who would you like to remove?').title()
                app_functions.delete_item(delete_courier, app_data.couriers)
                app_functions.yesno()
                os.system('clear')
                continue
            
            elif option2 == '0':
                os.system('clear')
                main_menu()            

            else:
                os.system('clear')
                print ('\nInvalid input, please try again')
                continue
    
    elif menu == '3':
        os.system('clear')
        while True:

            option3 = input('\n' 'Select Option' '\n' '\n1. Print Orders to Screen' '\n2. Create New Order' '\n3. Update Order Status' '\n4. Edit an Order' '\n5. Delete an Order' '\n0. Main Menu')

            if option3 == '1':
                os.system('clear')
                app_data.print_table(app_data.orders)
                app_functions.yesno()
                os.system('clear')
                continue

            elif option3 == '2':
                os.system('clear')
                app_functions.new_order()
                app_functions.yesno()
                os.system('clear')
                continue

            elif option3 == '3':
                os.system('clear')
                update_menu = input ('Select Option' '\n1. List of Orders' '\n0. Cancel')
                if update_menu == '1':
                    app_data.print_orders()
                    update_status = input('Which order would you like to update?')
                    status_loop = True
                    while status_loop:
                        status_question = input("Update Status").title()
                        if status_question in app_data.order_status:
                            app_data.orders[int(update_status)-1]['status'] = status_question
                            is_loop = False
                            break
                        else:
                            print('Invalid option please try again')
                    app_functions.yesno()
                    os.system('clear')
                    continue
                else:
                    os.system('clear')
                    continue
                    
            elif option3 == '4':
                os.system('clear')
                update_order = input ('Select Option' '\n1. List of Orders' '\n0. Cancel')
                

                if update_order == '0':
                    os.system('clear')
                    continue    
                    
                elif update_order == '1':
                    app_data.print_orders()
                    while True: #while loop needed here and not in the functions module as the main menu is also needed within the loop and is not defined in the dunctions module
                        app_functions.edit_order()
                        app_functions.yesno()
                        os.system('clear')
                        break
                    continue
                else:
                    os.system('clear')
                    print ('\nInvalid entry please try again')
                    continue

            elif option3 == '5':
                os.system('clear')
                app_data.print_table(app_data.orders)
                # remove_order = input('Which order would you like to delete?')
                # del app_data.orders[int(remove_order)-1]
                app_functions.delete_item(app_data.orders)
                app_functions.yesno()
                os.system('clear')
                continue

            elif option3 == '0':
                os.system('clear')
                main_menu() 
                
            else:
                os.system('clear')
                print ('\nInvalid input, please try again')
                continue

    elif menu == '0':
        os.system('clear')
        print('Thank You' '\nHave a Nice Day')
        app_data.return_data()  #also needed here as this option does not include the y/n question
        exit()
    
    else:
        os.system('clear')
        print ('\nInvalid input, please try again')
        main_menu()

main_menu()
