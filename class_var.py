class Contact(list):

   contact_list = []

   def __init__(self, name, location):
      self.name = name
      self.location = location

   def add_contact(self):
      Contact.contact_list.append(self.name)
      return f"Contact Name: {self.name}, Contact Location: {self.location}"

   @classmethod
   def favourites(cls, origin):
      cls.origin = origin #class method attribute
      add_new_contact = Contact.contact_list.append(cls.origin)
      return f"{cls.contact_list} "

class Supplier(Contact):
   supplier_list = {}

   def __init__(self, name, location, product, quantity):
      super().__init__(name, location)
      self.product = product
      self.quantity = quantity

   def add_contact(self):
      Supplier.supplier_list[self.product] = self.quantity
      contact = super().add_contact()
      

      
   
