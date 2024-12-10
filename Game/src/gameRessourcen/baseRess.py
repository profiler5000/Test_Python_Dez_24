



class BaseRess:
    def __init__(self):
        self.name =__class__.__name.get(self)
        self.description = self.check()
        

    def create_description(self):
            pass
    
    def check(self):
         if self.description is None:
              self.discription = self.create_description()

              


