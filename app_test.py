from unittest.mock import patch
from dotenv import load_dotenv
from mysql_app import add_entry, delete_entry, update_entry

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