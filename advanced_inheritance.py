"""
Advanced Inheritance Concepts in Python
Demonstrates super(), MRO, and multiple inheritance
"""

# ============================================================================
# SINGLE INHERITANCE WITH super()
# ============================================================================
# This is the most basic form of inheritance where a child class inherits
# from exactly one parent class. super() is used to:
# 1. Call the parent class constructor to initialize inherited attributes
# 2. Access parent class methods while extending or modifying their behavior
# 3. Maintain the inheritance chain properly for future subclassing
#
# Key benefits of using super():
# - Makes code more maintainable (no need to hardcode parent class names)
# - Supports cooperative inheritance in complex hierarchies
# - Automatically handles method resolution order (MRO)
# ============================================================================

class Animal:
    def __init__(self, creature_id, habitat, species):
        self.creature_id = creature_id  # Changed from 'name' to 'creature_id'
        self.habitat = habitat          # New attribute
        self.species = species
    
    def speak(self):
        return f"Creature {self.creature_id} from {self.habitat} makes a sound"

class Dog(Animal):
    def __init__(self, pet_name, owner, breed):
        # super() calls Animal.__init__() - attribute names can be different
        super().__init__(pet_name, "Domestic", "Canine")
        self.owner = owner    # Different attribute name
        self.breed = breed
    
    def speak(self):
        # Access inherited attributes with their actual names
        parent_sound = super().speak()
        return f"{parent_sound} - Woof! (Owner: {self.owner})"

# ============================================================================
# MULTIPLE INHERITANCE
# ============================================================================
# Multiple inheritance allows a class to inherit from more than one parent class.
# This creates a complex hierarchy where method resolution becomes critical.
# 
# Important concepts:
# 1. Method Resolution Order (MRO): Python uses C3 linearization algorithm
#    to determine which method to call when multiple parents have the same method
# 2. Cooperative inheritance: All classes should use super() consistently
# 3. Diamond problem: When multiple inheritance paths lead to the same base class
#
# Best practices:
# - Use super() in all classes, even if they don't inherit from anything
# - Be explicit about constructor calls when super() doesn't work cleanly
# - Understand your class's MRO using ClassName.__mro__
# ============================================================================

class Flyable:
    def __init__(self, flight_ceiling=1000, wing_span=50):
        self.flight_ceiling = wing_span    # Changed attribute names
        self.wing_span = wing_span
    
    def fly(self):
        return f"Flying with {self.wing_span}cm wings up to {self.flight_ceiling}m"

class Swimmable:
    def __init__(self, dive_limit=10, swim_speed=5):
        self.dive_limit = dive_limit      # Different from previous 'max_depth'
        self.swim_speed = swim_speed      # New attribute
    
    def swim(self):
        return f"Swimming at {self.swim_speed}km/h down to {self.dive_limit}m"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, duck_tag, pond_location):
        # Parameters can have completely different names
        Animal.__init__(self, duck_tag, pond_location, "Waterfowl")
        Flyable.__init__(self, 500, 80)
        Swimmable.__init__(self, 2, 3)
    
    def speak(self):
        return f"Duck {self.creature_id} from {self.habitat} says Quack!"

# ============================================================================
# DIAMOND PROBLEM AND METHOD RESOLUTION ORDER (MRO)
# ============================================================================
# The diamond problem occurs when a class inherits from multiple classes that
# share a common base class, creating a diamond-shaped inheritance hierarchy:
#
#       A
#      / \
#     B   C
#      \ /
#       D
#
# Without proper resolution, it's unclear which path to follow when calling
# methods. Python solves this using MRO (Method Resolution Order):
#
# 1. Uses C3 linearization algorithm
# 2. Ensures each class appears only once in the resolution order
# 3. Preserves the order specified in the class definition
# 4. Guarantees that parent classes come after child classes
#
# When super() is called, it follows the MRO chain, ensuring each method
# is called exactly once in the correct order.
# ============================================================================

class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")
        super().method()  # This will call A.method due to MRO

class C(A):
    def method(self):
        print("C.method")
        super().method()  # This will call A.method due to MRO

class D(B, C):
    def method(self):
        print("D.method")
        super().method()  # This follows MRO: D -> B -> C -> A
        # Output will be: D.method, B.method, C.method, A.method

# ============================================================================
# PROPERTY INHERITANCE WITH super()
# ============================================================================
# Properties (getters/setters) can also be inherited and extended using super().
# This is useful when you want to:
# 1. Add validation or processing to inherited properties
# 2. Modify the behavior of property access in child classes
# 3. Maintain the original property behavior while extending it
#
# Key points:
# - Use super().property_name to access the parent's property
# - You can override getters, setters, or deleters independently
# - Properties maintain the same interface while changing implementation
# ============================================================================

class Vehicle:
    def __init__(self, manufacturer, year_made):
        self._manufacturer = manufacturer  # Changed from 'brand'
        self._year_made = year_made       # New attribute
    
    @property
    def manufacturer(self):              # Changed property name
        return self._manufacturer
    
    @property
    def age(self):                       # New property
        return 2026 - self._year_made

class Car(Vehicle):
    def __init__(self, manufacturer, year_made, car_model, engine_type):
        super().__init__(manufacturer, year_made)
        self._car_model = car_model      # Different attribute names
        self._engine_type = engine_type
    
    @property
    def manufacturer(self):
        # Extend the parent's property behavior
        return f"Automobile by: {super().manufacturer}"
    
    @property
    def full_description(self):          # New property combining attributes
        return f"{self.manufacturer} {self._car_model} ({self._engine_type}) - {self.age} years old"

if __name__ == "__main__":
    print("=" * 60)
    print("SINGLE INHERITANCE EXAMPLE - FLEXIBLE ATTRIBUTE NAMES")
    print("=" * 60)
    dog = Dog("Buddy", "John Smith", "Golden Retriever")
    print(f"Dog info: ID={dog.creature_id}, Habitat={dog.habitat}, Species={dog.species}")
    print(f"Owner: {dog.owner}, Breed: {dog.breed}")
    print(dog.speak())
    
    print("\n" + "=" * 60)
    print("MULTIPLE INHERITANCE EXAMPLE - DIFFERENT PARAMETER NAMES")
    print("=" * 60)
    duck = Duck("D001", "Central Park Pond")
    print(f"Duck info: ID={duck.creature_id}, Location={duck.habitat}, Species={duck.species}")
    print(f"Wing span: {duck.wing_span}cm, Flight ceiling: {duck.flight_ceiling}m")
    print(f"Dive limit: {duck.dive_limit}m, Swim speed: {duck.swim_speed}km/h")
    print(duck.speak())
    print(duck.fly())
    print(duck.swim())
    
    print("\n" + "=" * 60)
    print("METHOD RESOLUTION ORDER (MRO)")
    print("=" * 60)
    print(f"Duck MRO: {[cls.__name__ for cls in Duck.__mro__]}")
    print("This shows the order Python searches for methods")
    
    print("\n" + "=" * 60)
    print("DIAMOND PROBLEM RESOLUTION")
    print("=" * 60)
    d = D()
    print("Calling d.method() - watch the order:")
    d.method()
    print(f"D's MRO: {[cls.__name__ for cls in D.__mro__]}")
    print("Notice how A.method is called only once, at the end")
    
    print("\n" + "=" * 60)
    print("PROPERTY INHERITANCE - FLEXIBLE NAMING")
    print("=" * 60)
    car = Car("Toyota", 2020, "Camry", "Hybrid")
    print(f"Original manufacturer: {super(Car, car).manufacturer}")
    print(f"Extended manufacturer: {car.manufacturer}")
    print(f"Car age: {car.age} years")
    print(f"Full description: {car.full_description}")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHT: ATTRIBUTE NAMES ARE COMPLETELY FLEXIBLE!")
    print("=" * 70)
    print("- Parent class uses: creature_id, habitat, species")
    print("- Child class uses: pet_name, owner, breed")
    print("- Parameter names in constructors can be anything")
    print("- What matters is how you map them in super().__init__()")
    print("- The actual stored attribute names are defined in the class")
