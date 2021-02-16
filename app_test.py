from app_functions import list_index, yesno, add_product
from app_data import open_files
from unittest.mock import patch

def test_list_index():

    #assemble
    test_list = [{'ID':1, 'ohafha': 'qpjrotj', 'iwrhqwhtp':'oqiwho'},
                {'ID':2, 'ohqwon':'pqwihpqhw', 'qpfhpofq':'iohfq'}]
    expected = [1,2]
    # act
    actual = list_index(test_list)
    # assert
    assert expected == actual
    print(actual)

test_list_index()

# def test_open_file_and_print_dictionaries_in_list():
    
#     # assemble
#     test_dictionary_list = []
#     expected = []
#     # act
#     open_files('test_products', test_dictionary_list)
#     actual = test_dictionary_list
#     print (actual)
#     # assert
#     assert expected == actual
#     print('another great success')

# test_open_file_and_print_dictionaries_in_list()
#Never use the actually data files for testing, use test files instead



@patch("app_functions.system_exit")
@patch("builtins.input")
@patch("app_data.return_data")
def test_yesno(mock_return_data, mock_input, mock_system_exit):

    mock_input.return_value = 'N'
    mock_system_exit.return_value = None
    
    yesno()
    
    
    mock_return_data.assert_called()

