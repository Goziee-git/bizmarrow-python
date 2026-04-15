class Name:
    """a class called Name"""
    #object properties
    def __init__(self, fname, lname):
        self.fname = f"my first name is:" + fname
        self.lname = f"My last name is:" + lname

    #__init__(dunder) 
    def changeFname(self):
        if self.fname == "Jane":
            self.fname = "Paul"
        else:
            print(f"Name not equal to Jane")



    

    # objectName = ClassName
