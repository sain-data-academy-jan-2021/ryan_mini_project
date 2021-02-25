from app_functions import list_index, yesno, add_product
from app_data import open_files
from unittest.mock import patch


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


