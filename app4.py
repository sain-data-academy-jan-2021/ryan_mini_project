import os
import tabulate
import mysql_app
import app_data
import app_functions 

import csv_app_menu

# print('''
# HELLO LADIES AND GENTLEMEN

# THIS AFTERNOON I WILL BE SHOWING YOU THE PROGRESS I'VE MADE OVER THE PAST 7 WEEKS.

# BIG CONGRATULATIONS TO EVERYONE ELSE ON THEIR PRENSENTATIONS TODAY AND A MASSIVE

# THANK YOU TO ALL OF THEM AND THE INFINITY WORKS TEAM FOR ALL THE HELP THEY'VE 

# GIVEN ME IN THE DEVELOPMENT OF THE PROJECT I'M ABOUT TO PRESENT. 

# HOPE YOU ENJOY!!!''')

CSV_OR_DATA = input ("")


if CSV_OR_DATA == '':
    csv_app_menu.main_menu()
else:
    csv_app_menu.main_menu()

