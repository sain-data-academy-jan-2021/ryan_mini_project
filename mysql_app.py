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


def add_entry(item, number):
    print_table(item, number)
    name = input (f'Insert new {item} name').title()
    value = input (f'Insert {number} for {name}?')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO {item}s ({item}_name, {number}) VALUES ("{name}", "{value}");')
    cursor.close()
    connection.commit()


def update_entry(item, number):
    print_table(item, number)
    ID = input (f'Select which {item} to Update')
    
    name = input (f'Insert new {item} name or leave blank to skip').title()
    if name == '':
        pass
    else:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE {item}s SET {item}_name = "{name}" WHERE {item}_ID = "{ID}";')
    
    value = input (f'Insert new {number} or leave blank to skip?')
    if value == '':
        pass
    else:
        cursor = connection.cursor()
        cursor.execute(f'UPDATE {item}s SET {number} = "{value}" WHERE {item}_ID = "{ID}";')

    cursor.close()
    connection.commit()


def delete_entry(item):
    if item == "product":
        print_table('product', 'product_price')
    elif item == "courier":
        print_table('courier', 'contact_number')
    deletion = input (f'Select the ID of the {item} you would like to delete?')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM {item}s WHERE {item}_ID = {deletion}')
    cursor.close()
    connection.commit()
