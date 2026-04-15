# Super() Examples for Inheritance in Python

# Example 1: Basic Method Inheritance with super()
class Animal:
    species_count = 0  # Class attribute
    species_name = []
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age
        Animal.species_count += 1
        Animal.species_name.append(self.name)
    
    def speak(self):
        return f"{self.name} makes a sound"

    def color(self):
        return f"{self.name} often has ash-brown color"
    
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Dog(Animal):
    breed_count = 0  # Child class attribute
    
    def __init__(self, name, age, breed):
        # Using super() to call parent's __init__
        super().__init__(name, age)  # Inherits name and age initialization
        self.breed = breed  # Additional instance attribute
        Dog.breed_count += 1
    
    def speak(self):
        # Using super() to extend parent method
        parent_sound = super().speak()  # Gets "Buddy makes a sound"
        return f"{parent_sound} - specifically barks!"

        # inherit/extend the color() of the parent class using super() in the child
    def color(self):
        parent_color = super().color()
        return f"{parent_color}, specifically a {self.breed}"
    
    def info(self):
        # Using super() to extend parent method with additional info
        basic_info = super().info()  # Gets parent's info method result
        return f"{basic_info}, Breed: {self.breed}"

# Example 2: Multiple Inheritance with super()
class Flyable:
    def __init__(self, max_altitude=1000):
        self.max_altitude = max_altitude
    
    def fly(self):
        return f"Flying at max altitude: {self.max_altitude}m"

class Bird(Animal, Flyable):
    def __init__(self, name, age, wingspan, max_altitude=500):
        # super() handles multiple inheritance properly
        Animal.__init__(self, name, age)  # Could use super() but explicit for clarity
        Flyable.__init__(self, max_altitude)
        self.wingspan = wingspan
    
    def speak(self):
        return f"{self.name} chirps"
    
    def fly(self):
        # Using super() in multiple inheritance
        flight_info = super().fly()  # Gets Flyable's fly method
        return f"{self.name} {flight_info.lower()} with {self.wingspan}cm wingspan"

# Example 3: Using super() in Class Methods and Static Methods
class Vehicle:
    total_vehicles = 0
    
    def __init__(self, make, model):
        self.make = make
        self.model = model
        Vehicle.total_vehicles += 1
    
    # A class method is a decorator in Python that creates a method bound to the class rather than
    # the instance,
    # ======================characteristics =======================
    # class-bound: it takes the class itself as the first parameter(conventionally cls) instead of an instance(self)
    # Accessible without instantiation: can be called directly on the class without creating an object
    # Inheritance-aware: when called on a sub-class, cls refers to that subclass, not the parent 
    @classmethod
    def get_total_vehicles(cls):
        return f"Total vehicles: {cls.total_vehicles}"
    
    @staticmethod
    def vehicle_type():
        return "Generic Vehicle"

class Car(Vehicle):
    total_cars = 0
    
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call parent constructor
        self.doors = doors
        Car.total_cars += 1
    
    @classmethod
    def get_total_vehicles(cls):
        # Using super() in class method
        parent_info = super().get_total_vehicles()
        return f"{parent_info}, Cars: {cls.total_cars}"
    

    # A @staticmethod is a decorator in python that creates a method that belongs to a class
    # but doesn't recieve any automatic first argument (no self, no cls). it essentially a regular
    # function that happens to be defined inside a class

    @staticmethod
    def vehicle_type():
        return "Car"
    
    def start_engine(self):
        return f"{self.make} {self.model} engine started"

# for creating objects in different ways

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def from_string(cls, person_str):
        name = person_str.split('-')
        return cls(name, int(age))  # cls creates the right class type
    
    @classmethod
    def baby(cls, name):
        return cls(name, 0)

# Example 4: Using super() in Property Methods
class Shape:
    def __init__(self, color):
        self._color = color
        self._area = 0
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
    
    @property
    def area(self):
        return self._area

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  # Initialize parent
        self.width = width
        self.height = height
        self._calculate_area()
    
    def _calculate_area(self):
        self._area = self.width * self.height
    
    @property
    def area(self):
        # Using super() in property getter
        base_area = super().area  # Gets parent's area property
        return f"Rectangle area: {base_area} square units"
    
    @Shape.color.setter
    def color(self, value):
        # Using super() in property setter
        if value in ['red', 'blue', 'green']:
            super(Rectangle, self.__class__).color.__set__(self, value)
        else:
            print(f"Warning: {value} is not a primary color")
            super(Rectangle, self.__class__).color.__set__(self, value)

# Example 5: Complex Inheritance Chain with super()
class LivingBeing:
    def __init__(self, lifespan):
        self.lifespan = lifespan
    
    def live(self):
        return "Living being exists"

class Mammal(LivingBeing):
    def __init__(self, lifespan, body_temp=37):
        super().__init__(lifespan)
        self.body_temp = body_temp
    
    def live(self):
        base_life = super().live()  # Gets "Living being exists"
        return f"{base_life} as a warm-blooded mammal"

class Primate(Mammal):
    def __init__(self, lifespan, body_temp=37, intelligence_level=5):
        super().__init__(lifespan, body_temp)
        self.intelligence_level = intelligence_level
    
    def live(self):
        mammal_life = super().live()  # Gets mammal's live method
        return f"{mammal_life} with intelligence level {self.intelligence_level}"
    
    def use_tools(self):
        return "Can use basic tools"

class Human(Primate):
    def __init__(self, lifespan, name, body_temp=37, intelligence_level=10):
        super().__init__(lifespan, body_temp, intelligence_level)
        self.name = name
    
    def live(self):
        primate_life = super().live()  # Gets primate's live method
        return f"{self.name}: {primate_life} and advanced reasoning"
    
    def use_tools(self):
        basic_tools = super().use_tools()  # Gets primate's tool use
        return f"{basic_tools} and can create complex technology"

# Example 6: Using super() with Method Resolution Order (MRO)
class A:
    def method(self):
        print("A.method called")
        return "A"

class B(A):
    def method(self):
        print("B.method called")
        result = super().method()  # Calls A.method
        return f"B -> {result}"

class C(A):
    def method(self):
        print("C.method called")
        result = super().method()  # Calls A.method
        return f"C -> {result}"

class D(B, C):
    def method(self):
        print("D.method called")
        result = super().method()  # Follows MRO: D -> B -> C -> A
        return f"D -> {result}"

# Demonstration functions
def demonstrate_basic_inheritance():
    print("=== Basic Inheritance with super() ===")
    dog = Dog("Buddy", 3, "Golden Retriever")
    print(f"Dog speaks: {dog.speak()}")
    print(f"Dog info: {dog.info()}")
    print(f"Animal species count: {Animal.species_count}")
    print(f"Dog breed count: {Dog.breed_count}")

def demonstrate_multiple_inheritance():
    print("\n=== Multiple Inheritance ===")
    bird = Bird("Eagle", 5, 200, 3000)
    print(f"Bird speaks: {bird.speak()}")
    print(f"Bird flies: {bird.fly()}")

def demonstrate_class_methods():
    print("\n=== Class Methods with super() ===")
    car1 = Car("Toyota", "Camry", 4)
    car2 = Car("Honda", "Civic", 4)
    print(Car.get_total_vehicles())

def demonstrate_properties():
    print("\n=== Properties with super() ===")
    rect = Rectangle("blue", 5, 3)
    print(f"Rectangle color: {rect.color}")
    print(f"Rectangle area: {rect.area}")
    rect.color = "yellow"  # Triggers warning
    print(f"New color: {rect.color}")

def demonstrate_inheritance_chain():
    print("\n=== Complex Inheritance Chain ===")
    human = Human(80, "Alice")
    print(f"Human life: {human.live()}")
    print(f"Tool use: {human.use_tools()}")

def demonstrate_mro():
    print("\n=== Method Resolution Order (MRO) ===")
    d = D()
    print(f"MRO: {D.__mro__}")
    result = d.method()
    print(f"Final result: {result}")

if __name__ == "__main__":
    demonstrate_basic_inheritance()
    demonstrate_multiple_inheritance()
    demonstrate_class_methods()
    demonstrate_properties()
    demonstrate_inheritance_chain()
    demonstrate_mro()
