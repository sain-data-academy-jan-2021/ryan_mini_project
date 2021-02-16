import os 

drinks = ['water', 'lemonade', 'coffee', 'coke', 'gin', 'beer', 'vodka', 'wine']
users = ['Ryan', 'Dan', 'Chris', 'Rachel', 'Nicki', 'Hani']

# \n allows you to shift the output down a line
# ''' allows you to type however you want and that is how it is printed

def get_menu(): #def function used to prevent rewriting multiple inputs 
        return input ('''Welcome to the RSAIWDBMP App v0.1

Please select an option by entering a number  
        
1. Product Menu 
2. User Menu 
0. Exit''') #return works with def ie when you ask for get_input it "returns" your input

menu = get_menu() #prints the inital input

def yesno():
    did_you_answer = False
    while did_you_answer == False :
        answer = input ('Would you like to do anything else y/n')
        if answer == 'y' or answer == 'n' :
            did_you_answer = True
    return answer #by setting this to false until true it means the question is asked until it's answered correctly
    
    
#input = False
#While input != True
while True: #programme will only run while the input is true
    if menu == '1':
        option1 = input ('\n' 'Select Option' '\n' '\n1. Drinks List' '\n2. Add a Drink' '\n3. Update a Drink'  '\n4. Remove a Drink' '\n0. Main Menu')
        
        if option1 == '1':
            print (drinks)
            answer = yesno()
            if answer == 'y':
                menu = get_menu()
            elif answer == 'n':
                break
                
                #input = True
            #exit()# prevents the infitine loop caused by the while True and ends the programme, needed after every if and elif that isn't returning you to main menu
    
        elif option1 == '2':
            print (drinks)
            new_drink = input ('What drink would you like to add?')
            if new_drink in drinks:
                print ('\nThis is already in our drinks selection, please try again') #this prevents the same element being added to the list again
            else:    
                drinks.append(new_drink) #.append(list) adds an element to a pre-existing list
                print (drinks)
                print ('\nThank you for adding ' + new_drink + ' to our collection') #setting up for later storage possibilities
                

        elif option1 == '3':

            update_drink = input ('Select Option' '\n1. List of Drinks' '\n0. Cancel')
            if update_drink == '1':

                print(drinks)
                try :
                    position_drink = input ('What drink numerically would you like to update?')
                    position_drink = int(position_drink) - 1 # converts the input from a string to an interger
                    if position_drink in range (0, len(drinks)): #sets the range to the length of the list 
                        drinks[position_drink] = input ('What would you like to update it to')
                        print (drinks)
                        print ('we have printed the drinks')
                        
                        print ('post exit')
                    else :
                        print('Invalid entry + 1')
                except :
                    print ('Invalid entry + 2')
            else:
                menu = get_menu()

        elif option1 == '4':
            print (drinks)
            delete_drink = input ('What drink would you like to remove?')
            if delete_drink in drinks: #since a programme cannot remove an element that is not in the list adding an additional if and else means the progranne can keep running no matter what the input is
                drinks.remove(delete_drink) #.remove(list) removes an element from a pre-existing list
                print (drinks)
                print ('\nThank you, ' + delete_drink + ' has been removed from our collection')
            
            else:
                print ('\ninvalid selection, please try again')

        elif option1 == '0':
            menu = get_menu() #returns you to the original input from the top

        else:
            print ('\ninvalid input, please try again')
            #by not putting exits at the end of an if elif or else the while True statement is still in effect so the user can still input again

    
    elif menu == '2':
        option2 = input ('Select Option' '\n1. Current Users' '\n2. Create New User' '\n3. Update Existing User' '\n4. Remove a User' '\n0. Main Menu')

        if option2 == '1':
            print (users)
            
        
        elif option2 == '2':
            new_user = input ('What is your name?')
            if new_user in users:
                print ('\nThis user already exists, please try again')
            else:    
                users.append(new_user)
                print (users)
                print ('\nWelcome ' + new_user) 
                

        elif option2 == '3':
            update_user = input ('Select Option' '\n1. List of Users' '\n0. Cancel')

            if update_user == '1':
                print(users)
                try :
                    position_user = input ('What drink numerically would you like to update?')
                    position_user = int(position_user) - 1 # converts the input from a string to an interger
                    if position_user in range (0, len(users)): #sets the range to the length of the list 
                        users[position_user] = input ('What would you like to update it to')
                        print (users)
                        
                    else :
                        print('Invalid entry')
                except :
                    print ('Invalid entry')
            else: 
                menu = get_menu()

        elif option2 == '4':
            print (users)
            delete_user = input ('What user would you like to remove?')
            if delete_user in users: 
                users.remove(delete_user) 
                print (users)
                print ('\nThank you, ' + delete_user + ' has been removed')
                
            else:
                print ('\ninvalid selection, please try again')

        elif option2 == '0':
            menu = get_menu()

        else:
            print('invalid selection, please try again')

    else:
        print ('Thank You' '\nHave a Nice Day')
        break