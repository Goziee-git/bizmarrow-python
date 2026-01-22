class Person:
   def __init__(self, firstname, lastname, hobby, community="Owerri-North"):
      self.firstname = firstname 
      self.lastname = lastname
      self.community = community
      self.hobby = hobby
    

   def introduction(self):
      return f"My name is {self.firstname} {self.lastname}"

   def identities(self):
      return f"Hello , good evening {self.community}"

   def likes(self):
      return f"{self.hobby}"

class Student(Person):
   def __init__(self, firstname, lastname, location, interest, hobby):
      super().__init__(firstname, lastname, "skating")
      self.location = location
      self.interest = interest
      self.hobby = super().likes()

   def bio(self):
      my_identity = super().identities() + " " + super().introduction()
      return f"{my_identity} - I am an igbo man " + "from " + self.location + " my favourite activity is " + self.hobby

   def introduction(self):
      return "Intro here in Student class"

   def identities(self):
      return "Identity in Student class"

class Multiple(Student):
   pass


Prospa = Person("Prospa", "Anyanwu", "dancing")
Student_one = Student("Nnena", "Anyanwu", "Imo-state", "dancing", "football")


#MRO
class Parent:
   def method(self):
      return "Base"

class Left(Parent):
   def method(self):
      return "Left"

class Right(Parent):
   def method(self):
      return "Right"
   
class Child(Left, Right):
   pass

obj = Child()
print(obj.method())