class ViewModel:
    
    def __init__(self, vm_items):
        self.vm_items = vm_items   #pass list of items to view model through here...

    @property
    def vm_do_items(self):
      
      vm_list_of_items = []           
           
      for fl_item in self.vm_items:
         if fl_item.data_item_status == "To Do":
            vm_list_of_items.append(fl_item)
            
      return vm_list_of_items

    @property
    def vm_doing_items(self):
           
      vm_list_of_items = []           
           
      for fl_item in self.vm_items:
         if fl_item.data_item_status == "Doing":
            vm_list_of_items.append(fl_item)
            
      return vm_list_of_items        
   
    @property
    def vm_done_items(self):
           
      vm_list_of_items = []           
           
      for fl_item in self.vm_items:
         if fl_item.data_item_status == "Done":
            vm_list_of_items.append(fl_item)
            
      return vm_list_of_items    