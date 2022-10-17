class ViewModel:
    
    def __init__(self, do_items, doing_items, done_items):
        self._do_items = do_items
        self._doing_items = doing_items
        self._done_items = done_items

    @property
    def do_items(self):
       return self._do_items

    @property
    def doing_items(self):
       return self._doing_items
   
    @property
    def done_items(self):
       return self._done_items