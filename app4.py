import os
import tabulate
import mysql_app
import app_data
import app_functions 
import app_menu
import csv_app_menu

print('''
HELLO LADIES AND GENTLEMEN

THIS AFTERNOON I WILL BE SHOWING YOU THE PROGRESS I'VE MADE OVER THE PAST 7 WEEKS

IT HAS BEEN A FANTASTIC EXPERIENCE FOR ME SO FAR AND CAN'T WAIT TO START THE NEXT PROJECT

HOPE YOU ENJOY''')

CSV_OR_DATA = input ("")


if CSV_OR_DATA == '':
    csv_app_menu.main_menu()
else:
    csv_app_menu.main_menu()

