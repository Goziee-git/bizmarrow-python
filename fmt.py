class Person:
   def setName(self, firstname, lastname):
      """this is a method of attributes"""
      self.firstname = firstname
      self.lastname = lastname
      fullname = firstname + " " + lastname
      return fullname
      

   def getName(self):
       return 
   
firstname = "prospa".upper()
lastname = "John"
fullname = firstname + " " + lastname
print(f"{fullname}")


prospa = Person() #this is calling the class on the object
prospa.name("prospa", "muicheal")
somto = Person() # is calling the Person class on the somto object



