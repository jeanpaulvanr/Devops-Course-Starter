class ViewModel:
    
    def __init__(self, items):
        self.items = items

    @property
    def do_items(self):
      
      list_of_cards = []           
           
      for item in self.items:
         if item.list_name == "To Do":
            list_of_cards.append(item)
            
      return list_of_cards

    @property
    def doing_items(self):
           
      list_of_cards = []           
           
      for item in self.items:
         if item.list_name == "Doing":
            list_of_cards.append(item)
            
      return list_of_cards          

   
    @property
    def done_items(self):
           
      list_of_cards = []           
           
      for item in self.items:
         if item.list_name == "Done":
            list_of_cards.append(item)
            
      return list_of_cards    