from todo_app.data.data_item import Data_Item
from todo_app.data.view_model import ViewModel 
import pytest

# Arrange
@pytest.fixture
def items_list(): 
    return [
        Data_Item(1, "My Todo Item 1", "To Do"),
        Data_Item(2, "My Doing Item 1", "Doing"), 
        Data_Item(3, "My Done Item", "Done")
    ]
 
def test_do_items_property_only_shows_do_items(items_list):
    
    # Arrange
    view_model = ViewModel(items_list)
        
    # Act
    returned_do_items = view_model.vm_do_items

    # Assert
    assert len(returned_do_items) == 1
    do_item = returned_do_items[0]
    assert do_item.list_name == "To Do"

def test_doing_items_property_only_shows_doing_items(items_list):
    
    # Arrange
    view_model = ViewModel(items_list)
        
    # Act
    returned_doing_items = view_model.vm_doing_items

    # Assert
    assert len(returned_doing_items) == 1
    doing_item = returned_doing_items[0]
    assert doing_item.list_name == "Doing"
    
def test_done_items_property_only_shows_done_items(items_list):
    
    # Arrange
    view_model = ViewModel(items_list)
        
    # Act
    returned_done_items = view_model.vm_done_items

    # Assert
    assert len(returned_done_items) == 1
    done_item = returned_done_items[0]
    assert done_item.list_name == "Done"