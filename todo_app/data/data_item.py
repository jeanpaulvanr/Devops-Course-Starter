class Data_Item:
    def __init__(self, data_item_id, data_item_name, data_item_status = 'To Do' ):
        self.data_item_id = data_item_id
        self.data_item_name = data_item_name
        self.data_item_status = data_item_status
        
    @classmethod
    def from_a_data_item(cls, data_values, status_values):
        return cls(data_values['_id'], data_values['item name'], status_values['status'])