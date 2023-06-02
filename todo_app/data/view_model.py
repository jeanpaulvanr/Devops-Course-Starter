class ViewModel:
    
    def __init__(self, items):
        self.items = items   #pass list of items to view model through here...

    @property
    def do_items(self):
      
      vm_list_of_cards = []           
           
      for item in self.items:
         if item.card_status == "To Do":
            vm_list_of_cards.append(item)
            
      return vm_list_of_cards

    @property
    def doing_items(self):
           
      vm_list_of_cards = []           
           
      for item in self.items:
         if item.card_status == "Doing":
            vm_list_of_cards.append(item)
            
      return vm_list_of_cards          
   
    @property
    def done_items(self):
           
      vm_list_of_cards = []           
           
      for item in self.items:
         if item.card_status == "Done":
            vm_list_of_cards.append(item)
            
      return vm_list_of_cards    