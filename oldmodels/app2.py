import os #works with os.system('clear') to make the terimal cleaner
import sys #works with sys.exit() to close the program

#getting the list from the txt files:

drinks = [] #empty lists created to store the data from the txt files
couriers = []

drinks_file_name = 'drinks' #needed so the name of the txt files can be called at any point in the code without using strings
couriers_file_name = 'couriers'

drinks_file = open ('drinks.txt', 'r') #opens and reads the txt file

for line in drinks_file.readlines():
    drinks.append(line.strip()) #adds each line from the txt file into a list

couriers_file = open ('couriers.txt', 'r')

for line in couriers_file.readlines():
    couriers.append(line.strip()) #prevents \n appearing in the lists


#defining the functions

#sending data back to txt files

def return_data(items, items_file): #items is the the list, items_file is the name of the txt files
    try:
        with open(f'{items_file}.txt', 'w') as items_file: #using 'w' overwrites the previous file and replaces it with the new data
            for item in items:
                items_file.write(item + '\n') # + '\n' needed to print txt file line by line
    except:
        print('Failed to open file')


def yesno(): #offers the courier the oppotunity to continue using the program or not
    did_you_answer = False # by setting the question to false it means unless a correct input is uses the question will keep being re-asked
    while did_you_answer == False :
        answer = input ('\nWould you like to do anything else y/n')
        if answer == 'y' or answer == 'n' :
            did_you_answer = True
            if answer == 'y':
                main_menu()
            elif answer == 'n':
                return_data(drinks, drinks_file_name)  
                return_data(couriers, couriers_file_name)
                os.system('clear')
                print ('Thank You' '\nHave a Nice Day')
                sys.exit 
    

def add_item(item, item_list): #by defining functions as item, item_list it stops me having to write out the function multiple times for drinks and couriers
    if item in item_list: #this stops the same item being added twice
        os.system('clear')
        print (f'\nSorry {item} already exists')     
    else:
        item_list.append(item) #anything not in the current list will be added
        os.system('clear')
        print (f'\n{item} has been added')
        

def delete_item(item, item_list):
    if item not in item_list:
        os.system('clear')
        print (f"\nSorry, {item} does not exist") 
    else:
        item_list.remove(item)
        os.system('clear')
        print (f'\n{item} has been removed')


def update_item(item, item_list):
    os.system('clear')
    print ('\n'.join(item_list))
    try:
        position_item = input ('Choose numerically what you would like to update') #has to be set numerically so the item can be replaced at the same index point 
        position_item = int(position_item) -1 #int changes string to integer and must be -1 as index values start at 0
        if position_item in range (0, len(item_list)):#by setting the range to len the range will always be the same length as the list as it grows or shrinks
            item_list[position_item] = input ('What would you like to update it to?')
            print ('\n'.join(item_list))     
        else:
            print('Invalid entry')
    except:
        print ('Invalid entry')


def main_menu(): 
    os.system('clear')
     #using ''' means you can write anything you want within it and that's what will be printed in the terminal
    menu = input ('''
Welcome to RSAIWDBMP v0.2

Please select an option by entering a number  
        
1. Product Menu 
2. Courier Menu 
0. Exit''') 

    #while True: 

    if menu == '1':
        os.system('clear')
        option1 = input ('\n' 'Select Option' '\n' '\n1. Drinks List' '\n2. Add a Drink' '\n3. Update a Drink'  '\n4. Remove a Drink' '\n0. Main Menu')
        
        if option1 == '1':
            os.system('clear')
            print ('\n'.join(drinks))
            answer = yesno()
                
        elif option1 == '2':
            os.system('clear')
            print ('\n'.join(drinks))
            new_drink = input ('What drink would you like to add?')
            add_item(new_drink, drinks) #uses the add_item function to add a new drink to the list of drinks
            answer = yesno()

        elif option1 == '3':
            os.system('clear')
            update_drink = input ('Select Option' '\n1. List of Drinks' '\n0. Cancel')
            if update_drink == '1':
                update_item(update_drink, drinks)
                answer = yesno()
            else:
                os.system('clear')
                main_menu() #returns you straight to the starter menu 

        elif option1 == '4':
            os.system('clear')
            print ('\n'.join(drinks))
            delete_drink = input('What drink would you like to remove?')
            delete_item(delete_drink, drinks)
            answer = yesno()

        elif option1 == '0':
            os.system('clear')
            main_menu()

        else:
            os.system('clear')
            print ('\nInvalid input, please try again')
            main_menu()
            
    elif menu == '2':
        os.system('clear')
        option2 = input ('\nSelect Option' '\n' '\n1. Current Couriers' '\n2. Create New Courier' '\n3. Update Existing Courier' '\n4. Remove a Courier' '\n0. Main Menu')

        if option2 == '1':
            os.system('clear')
            print ('\n'.join(couriers))
            answer = yesno()

        elif option2 == '2':
            os.system('clear')
            print ('\n'.join(couriers))
            new_courier = input ('What is your name?')
            add_item(new_courier, couriers)
            answer = yesno()

        elif option2 == '3':
            os.system('clear')
            update_courier = input ('Select Option' '\n1. List of Couriers' '\n0. Cancel')
            if update_courier == '1':
                update_item(update_courier, couriers)
                answer = yesno()
            else:
                os.system('clear')
                main_menu()

        elif option2 == '4':
            os.system('clear')
            print ('\n'.join(couriers))
            delete_courier = input ('Who would you like to remove?')
            delete_item(delete_courier, couriers)
            answer = yesno()
        
        elif option2 == '0':
            os.system('clear')
            main_menu() 
            

        else:
            os.system('clear')
            print ('\nInvalid input, please try again')
            main_menu()
            
    elif menu == '0':
        os.system('clear')
        print('Thank You' '\nHave a Nice Day')
        return_data(drinks, drinks_file_name)  #also needed here as this option does not include the y/n question
        return_data(couriers, couriers_file_name)
        sys.exit
    
    else:
        os.system('clear')
        main_menu()

main_menu() #must be put here as the last 100 lines were all within a def function and this then runs the program
    