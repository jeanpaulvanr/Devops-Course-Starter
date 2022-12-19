from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel 
import pytest

# Arrange
@pytest.fixture
def do_items_list(): 
    return [
        Item(1, "My Todo Item 1", "To Do"),
        Item(2, "My Todo Item 2", "To Do"),
        Item(3, "My Todo Item 3", "To Do")
    ]
 
@pytest.fixture   
def doing_items_list():
    return [Item(1, "My Doing Item 1", "Doing"),Item(2, "My Doing Item 2", "Doing"),Item(3, "My Doing Item 3", "Doing")]

@pytest.fixture    
def done_items_list():
    return [
        Item(1, "My Done Item 1", "Done"),
        Item(2, "My Done Item 2", "Done"),
        Item(3, "My Done Item 3", "Done")
    ]    

def test_do_items_property_only_shows_do_items(do_items_list):
    
    # Arrange
    view_model = ViewModel(do_items_list, doing_items_list, done_items_list)
        
    # Act
    returned_do_items = view_model.do_items

    # Assert
    assert len(returned_do_items) == 3
    do_item = returned_do_items[0]
    assert do_item.list_name == "To Do"

def test_doing_items_property_only_shows_doing_items(doing_items_list):
    
    # Arrange
    view_model = ViewModel(do_items_list, doing_items_list, done_items_list)
        
    # Act
    returned_doing_items = view_model.doing_items

    # Assert
    assert len(returned_doing_items) == 3
    doing_item = returned_doing_items[0]
    assert doing_item.list_name == "Doing"
    
def test_done_items_property_only_shows_done_items(done_items_list):
    
    # Arrange
    view_model = ViewModel(do_items_list, doing_items_list, done_items_list)
        
    # Act
    returned_done_items = view_model.done_items

    # Assert
    assert len(returned_done_items) == 3
    done_item = returned_done_items[0]
    assert done_item.list_name == "Done"