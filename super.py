# OVeriding means altering or replacing a method of the superclass
# a new method(with the same name) in the class. The suclass method is automatically 
# called instead of the superclass's method

class Contact:
    all_contact = []

    def __init__(self, name, email):
        self.name = "prospa"
        self.email = email
        self.location = self.supplier
        Contact.all_contact.append(self)

    def supplier(self, location):
        return f"{self.name} lives at {self.location}"

class Friend(Contact):
    def __init__(self, name, email, phone):
        
        self.name = name
        self.email = email
        self.phone = phone

    def supplier(self, location):
        return f"{self.name} comes from  {self.location}"
