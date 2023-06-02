class Item:
    def __init__(self, card_id, card_name, status = 'To Do'):
        self.card_id = card_id
        self.card_name = card_name
        self.card_status = status
        
    @classmethod
    def from_a_card(cls, card_values, status_values):
        return cls(card_values['id'], card_values['name'], status_values['name'])