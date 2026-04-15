# Nested Classes - Quick Guide

## What is a Nested Class?

A class defined inside another class. In the example below, `Engine` is nested inside `Car`.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = self.Engine()  # Create nested class instance
    
    class Engine:  # Nested class
        def __init__(self):
            self.status = "off"
        
        def start(self):
            self.status = "running"
```

---

## 1. Creating Objects of Nested Class

### Method 1: From Outside (using outer class name)
```python
# Access nested class through outer class
engine = Car.Engine()
engine.start()
```

### Method 2: From Inside Outer Class
```python
class Car:
    def __init__(self):
        self.engine = self.Engine()  # Create instance inside outer class
```

---

## 2. Calling Nested Class Methods

```python
# Create car instance
my_car = Car("Toyota")

# Call nested class method through outer class instance
my_car.engine.start()

# Or create nested class directly
engine = Car.Engine()
engine.start()
```

---

## 3. Interacting with Outer Class from Nested Class

Nested classes don't automatically have access to outer class. You must pass a reference.

```python
class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = self.Engine(self)  # Pass 'self' to nested class
    
    class Engine:
        def __init__(self, car):
            self.car = car  # Store reference to outer class
            self.status = "off"
        
        def start(self):
            self.status = "running"
            # Access outer class attribute
            return f"{self.car.brand}'s engine is {self.status}"

# Usage
my_car = Car("Toyota")
print(my_car.engine.start())  # Output: Toyota's engine is running
```

---

## OOP Concepts

### Encapsulation
Groups related classes together. `Engine` belongs to `Car`.

### Inheritance
```python
class ElectricCar(Car):
    class Engine(Car.Engine):  # Inherit nested class
        def start(self):
            return "Silent electric start"
```

### Polymorphism
```python
class Car:
    class GasEngine:
        def start(self):
            return "Vroom!"
    
    class ElectricEngine:
        def start(self):
            return "Silent start"
```

### Abstraction
Hides complex internal details inside nested classes.

---

## Django Example

```python
class Product(models.Model):
    name = models.CharField(max_length=100)
    
    class Status(models.TextChoices):  # Nested class
        ACTIVE = 'AC', 'Active'
        INACTIVE = 'IN', 'Inactive'
    
    status = models.CharField(choices=Status.choices)

# Usage
product = Product(name="Laptop", status=Product.Status.ACTIVE)
```
