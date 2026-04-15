class Parent:

    def __init__(self, fname, lname):
        self.fname= fname
        self.lname = lname

    def bio(self):
        return "{self.fname} {self.lname}"

class Child(Parent):
    def __init__(self, fname, lname, school, hobby):
        super().__init__(fname, lname)
        self.school = school
        self.hobby = hobby

class Relative(Child):
    def __init__(self, fname, lname, school, hobby, location):
        super().__init__(fname, lname, hobby, location)

















class Parent:
    """A Parent class"""
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname
#comments
class Child(Parent):
    """A Child class inherited from the parent class"""
    def __init__(self, fname, lname, age, hobby):
        super().__init__(fname, lname)
        self.age = age
        self.hobby = hobby

class Relative(Child):
    """A Relative child class inherited from the Child class"""
    def __init__(self, fname, lname, age, hobby, location):
        super().__init__(lname, fname, age, hobby)
        self.location = location