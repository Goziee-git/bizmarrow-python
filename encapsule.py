#Pay attention to the concept of @property, getters, setters, deleters
class Person:
   def __init__(self, name, age):
      self.name = name
      #self.age = age
      #to make the age attribute private
      self.__age = age

#getter method is used to access the encapsulated attribute
# Object_name.getter()

   def get_age(self):
      return self.__age

P1 = Person("Omojo", 25)

#SETTER methods
class Animal:
   def __init__(self, species, habitat):
      self.species = species
      self.__habitat = habitat

   def get_habitat(self):
      return self.__habitat

   def set_habitat(self):
      if (habitat.starstwith("t")) == 1:
         self.__habitat = habitat
      else:
         return "arboreal/acquatic"

   

animal_one = Animal("mammal", "terrestrial")
print(animal_one.get_habitat())
animal_one.set_habitat("terresterial")
print(animal_one.get_habiat())