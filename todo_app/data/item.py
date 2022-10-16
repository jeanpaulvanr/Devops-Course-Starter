class Item:
    def __init__(self, card_id, card_name, board_list = 'To Do'):
        self.card_id = card_id
        self.card_name = card_name
        self.list_name = board_list
        
    @classmethod
    def from_trello_card(cls, board_card_values, board_list_values):
        return cls(board_card_values['id'], board_card_values['name'], board_list_values['name'])