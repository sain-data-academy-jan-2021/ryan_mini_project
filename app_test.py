from app_functions import list_index, yesno, add_product
from app_data import open_files
from unittest.mock import patch
from dotenv import load_dotenv
from mysql_app import add_entry, delete_entry, update_entry

# CSV Tests

def test_open_file_and_print_dictionaries_in_list():
    
    # assemble
    test_dictionary_list = []
    expected = [{'ID': '1', 'Product': 'Water', 'Price': '0.55'}, {'ID': '2', 'Product': 'Milk', 'Price': '1.00'}, {'ID': '3', 'Product': 'Coke', 'Price': '1.50'}, {'ID': '4', 'Product': 'Lemonade', 'Price': '1.10'}]
    # act
    open_files('test_products', test_dictionary_list)
    actual = test_dictionary_list
    print (actual)
    # assert
    assert expected == actual

#Never use the actually data files for testing, use test files instead


def test_list_index():
    
    #assemble
    test_list = [{'ID':1, 'ohafha': 'qpjrotj', 'iwrhqwhtp':'oqiwho'},
                {'ID':7, 'ohqwon':'pqwihpqhw', 'qpfhpofq':'iohfq'}]
    expected = [1,7]
    # act
    actual = list_index(test_list)
    # assert
    assert expected == actual



@patch("builtins.input")
@patch("app_data.return_data")
def test_yesno_yes_functionality(mock_return_data, mock_input):

    mock_input.return_value = 'Y'

    yesno()
        
    mock_return_data.assert_called()


@patch("app_functions.system_exit")
@patch("builtins.input")
@patch("app_data.return_data")
def test_yesno_no_functionality(mock_return_data, mock_input, mock_system_exit):

    mock_input.return_value = 'N'
    mock_system_exit.return_value = None
    
    yesno()
        
    mock_return_data.assert_called()


# Database Tests


@patch("builtins.input")
@patch("mysql_app.execute_sql")
@patch("mysql_app.print_table")
def test_add_item_to_database(mock_print, mock_execute, mock_input):

    # Assemble
    mock_input.side_effect = ["Banana", 0.65]
    mock_print.return_value = None
    expected = (f'INSERT INTO products (product_name, product_price) VALUES ("Banana", "0.65")')

    # Act
    add_entry("product", "product_price", None)
    
    # Assert
    mock_execute.assert_called_with(None, expected)




@patch("builtins.input")
@patch("mysql_app.execute_sql")
@patch("mysql_app.print_table")
def test_update_item_in_database_with_a_blank_entry(mock_print, mock_execute, mock_input):

    # Assemble
    mock_input.side_effect = [13, "", 0.65]
    mock_print.return_value = None
    expected = (f'UPDATE products SET product_price = "0.65" WHERE product_ID = "13";')

    # Act
    update_entry("product", "product_price", None)
    
    # Assert
    mock_execute.assert_called_with(None, expected)

    


@patch("builtins.input")
@patch("mysql_app.execute_sql")
@patch("mysql_app.print_table")
def test_delete_item_from_database(mock_print, mock_execute, mock_input):

    # Assemble
    mock_input.side_effect = [7]
    mock_print.return_value = None
    expected = (f'DELETE FROM couriers WHERE courier_ID = 7;')

    # Act
    delete_entry("courier", None)
    
    # Assert
    mock_execute.assert_called_with(None, expected)