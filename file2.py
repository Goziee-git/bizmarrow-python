# classes: blueprint --> attributes, behaviours (methods)
class Animal: #parent class
    class_variable = "class_variable_value" #class_attribute

    def __init__(self, name, color, height, weight):
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight


    #methods
    def move(self):
        pass

    def run(self):
        return "animal can run"

    def fly(self): #always usethe self parameter
        print("animal can fly")

class Habitat(Animal):
     #child class
     def__init__(self, aqua, arboreal, terrestrial):
        super().
        self.aqua = aqua
        self.arboreal = arboreal
        self.terrestrial = "Desert"



#objects - instances of a class
#instantiate an object of the class Animal
Bird = Animal("eagle", "Brown", "45", "456")
Sheep = Animal("african-brown", "black", "79", "89")

#accessing attributs of the bird object
Bird.name #--> "eagle"
Bird.color #--> Brown

# accessing methods
Bird.move()



