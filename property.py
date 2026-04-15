"""
COMPUTED METHODS AND PROPERTY METHODS IN PYTHON
==============================================

This file demonstrates computed methods and property methods with detailed explanations
and practical examples showing their usage, benefits, and implementation patterns.
"""

import math
from datetime import datetime, date
from typing import Optional


class Person:
    """
    COMPUTED METHODS (Regular Methods)
    ================================
    
    Computed methods are regular instance methods that calculate and return values
    based on the object's current state. They are called explicitly with parentheses.
    
    Characteristics:
    - Called with parentheses: obj.method()
    - Can accept parameters
    - Recalculated every time they're called
    - Can have side effects
    - More flexible for complex computations
    """
    
    def __init__(self, first_name: str, last_name: str, birth_date: date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self._cached_age = None
        self._age_calculated_date = None
    
    # COMPUTED METHOD EXAMPLES
    def get_full_name(self) -> str:
        """Computed method: Combines first and last name"""
        return f"{self.first_name} {self.last_name}"
    
    def calculate_age(self) -> int:
        """Computed method: Calculates current age"""
        today = date.today()
        age = today.year - self.birth_date.year
        if today < date(today.year, self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
    
    def get_age_with_caching(self) -> int:
        """Computed method with caching optimization"""
        today = date.today()
        if self._cached_age is None or self._age_calculated_date != today:
            self._cached_age = self.calculate_age()
            self._age_calculated_date = today
        return self._cached_age
    
    def get_initials(self, include_dots: bool = True) -> str:
        """Computed method with parameters"""
        initials = f"{self.first_name[0]}{self.last_name[0]}"
        return f"{initials[0]}.{initials[1]}." if include_dots else initials


class BankAccount:
    """
    PROPERTY METHODS (@property decorator)
    ====================================
    
    Property methods use the @property decorator to make methods accessible
    like attributes. They provide computed values that appear as simple attributes.
    
    Characteristics:
    - Accessed without parentheses: obj.attribute
    - Cannot accept additional parameters
    - Can have getter, setter, and deleter
    - Provide attribute-like interface for computed values
    - Better for simple computations that feel like attributes
    """
    
    def __init__(self, account_number: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self._balance = initial_balance
        self._transactions = []
        self._interest_rate = 0.02  # 2% annual interest
    
    # PROPERTY METHOD EXAMPLES
    
    @property
    def balance(self) -> float:
        """Property: Current account balance (read-only computed property)"""
        return sum(transaction['amount'] for transaction in self._transactions) + self._balance
    
    @property
    def formatted_balance(self) -> str:
        """Property: Formatted balance as currency string"""
        return f"${self.balance:,.2f}"
    
    @property
    def interest_rate(self) -> float:
        """Property getter: Interest rate with validation"""
        return self._interest_rate
    
    @interest_rate.setter
    def interest_rate(self, value: float) -> None:
        """Property setter: Set interest rate with validation"""
        if not 0 <= value <= 1:
            raise ValueError("Interest rate must be between 0 and 1")
        self._interest_rate = value
    
    @property
    def annual_interest(self) -> float:
        """Property: Calculated annual interest based on current balance"""
        return self.balance * self._interest_rate
    
    @property
    def account_status(self) -> str:
        """Property: Account status based on balance"""
        if self.balance < 0:
            return "OVERDRAWN"
        elif self.balance < 100:
            return "LOW_BALANCE"
        elif self.balance < 10000:
            return "ACTIVE"
        else:
            return "HIGH_BALANCE"
    
    # COMPUTED METHODS for comparison
    def add_transaction(self, amount: float, description: str = "") -> None:
        """Computed method: Add a transaction (has side effects)"""
        self._transactions.append({
            'amount': amount,
            'description': description,
            'timestamp': datetime.now()
        })
    
    def calculate_compound_interest(self, years: int) -> float:
        """Computed method: Calculate compound interest over time"""
        return self.balance * (1 + self._interest_rate) ** years


class Rectangle:
    """
    ADVANCED PROPERTY PATTERNS
    =========================
    
    Demonstrates advanced property usage patterns including:
    - Cached properties
    - Dependent properties
    - Property validation
    - Read-only computed properties
    """
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
        self._area_cache = None
        self._perimeter_cache = None
    
    @property
    def width(self) -> float:
        """Property with getter and setter"""
        return self._width
    
    @width.setter
    def width(self, value: float) -> None:
        """Width setter with validation and cache invalidation"""
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
        self._invalidate_cache()
    
    @property
    def height(self) -> float:
        """Property with getter and setter"""
        return self._height
    
    @height.setter
    def height(self, value: float) -> None:
        """Height setter with validation and cache invalidation"""
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
        self._invalidate_cache()
    
    @property
    def area(self) -> float:
        """Cached property: Area calculation with caching"""
        if self._area_cache is None:
            self._area_cache = self._width * self._height
        return self._area_cache
    
    @property
    def perimeter(self) -> float:
        """Cached property: Perimeter calculation with caching"""
        if self._perimeter_cache is None:
            self._perimeter_cache = 2 * (self._width + self._height)
        return self._perimeter_cache
    
    @property
    def diagonal(self) -> float:
        """Property: Diagonal calculation (always computed)"""
        return math.sqrt(self._width ** 2 + self._height ** 2)
    
    @property
    def aspect_ratio(self) -> float:
        """Property: Aspect ratio (width/height)"""
        return self._width / self._height
    
    @property
    def is_square(self) -> bool:
        """Property: Boolean property indicating if rectangle is square"""
        return abs(self._width - self._height) < 1e-10
    
    def _invalidate_cache(self) -> None:
        """Helper method to clear cached values"""
        self._area_cache = None
        self._perimeter_cache = None


class Temperature:
    """
    PROPERTY METHODS FOR UNIT CONVERSION
    ===================================
    
    Demonstrates how properties can be used for unit conversions
    and maintaining data consistency across different representations.
    """
    
    def __init__(self, celsius: float = 0.0):
        self._celsius = celsius
    
    @property
    def celsius(self) -> float:
        """Property: Temperature in Celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value: float) -> None:
        """Celsius setter with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self) -> float:
        """Property: Temperature in Fahrenheit (computed from Celsius)"""
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value: float) -> None:
        """Fahrenheit setter (converts to Celsius internally)"""
        celsius_value = (value - 32) * 5/9
        if celsius_value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = celsius_value
    
    @property
    def kelvin(self) -> float:
        """Property: Temperature in Kelvin (computed from Celsius)"""
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value: float) -> None:
        """Kelvin setter (converts to Celsius internally)"""
        if value < 0:
            raise ValueError("Kelvin temperature cannot be negative")
        self._celsius = value - 273.15


# DEMONSTRATION AND USAGE EXAMPLES
def demonstrate_computed_vs_property_methods():
    """
    WHEN TO USE COMPUTED METHODS VS PROPERTY METHODS
    ===============================================
    
    Use COMPUTED METHODS when:
    - The operation needs parameters
    - The operation has side effects
    - The operation is expensive and should be called explicitly
    - The operation represents an action rather than an attribute
    
    Use PROPERTY METHODS when:
    - The value feels like an attribute of the object
    - No additional parameters are needed
    - You want attribute-like access syntax
    - The computation is relatively lightweight
    - You need getter/setter behavior
    """
    
    print("=== COMPUTED METHODS DEMO ===")
    person = Person("John", "Doe", date(1990, 5, 15))
    
    # Computed methods - called with parentheses
    print(f"Full name: {person.get_full_name()}")
    print(f"Age: {person.calculate_age()}")
    print(f"Initials: {person.get_initials()}")
    print(f"Initials (no dots): {person.get_initials(False)}")
    
    print("\n=== PROPERTY METHODS DEMO ===")
    account = BankAccount("ACC-001", 1000.0)
    account.add_transaction(500.0, "Deposit")
    account.add_transaction(-200.0, "Withdrawal")
    
    # Property methods - accessed like attributes
    print(f"Balance: {account.balance}")
    print(f"Formatted balance: {account.formatted_balance}")
    print(f"Account status: {account.account_status}")
    print(f"Annual interest: {account.annual_interest}")
    
    # Property with setter
    account.interest_rate = 0.03
    print(f"New interest rate: {account.interest_rate}")
    
    print("\n=== ADVANCED PROPERTIES DEMO ===")
    rect = Rectangle(10, 5)
    
    # Properties that feel like attributes
    print(f"Width: {rect.width}, Height: {rect.height}")
    print(f"Area: {rect.area}")  # Cached
    print(f"Perimeter: {rect.perimeter}")  # Cached
    print(f"Diagonal: {rect.diagonal}")  # Always computed
    print(f"Is square: {rect.is_square}")
    
    # Changing dimensions invalidates cache
    rect.width = 5
    print(f"After making square - Area: {rect.area}, Is square: {rect.is_square}")
    
    print("\n=== UNIT CONVERSION PROPERTIES DEMO ===")
    temp = Temperature(25)  # 25°C
    
    print(f"Celsius: {temp.celsius}°C")
    print(f"Fahrenheit: {temp.fahrenheit}°F")
    print(f"Kelvin: {temp.kelvin}K")
    
    # Setting via different units
    temp.fahrenheit = 100  # Set to 100°F
    print(f"After setting to 100°F - Celsius: {temp.celsius:.2f}°C")


if __name__ == "__main__":
    demonstrate_computed_vs_property_methods()


"""
KEY DIFFERENCES SUMMARY:
=======================

COMPUTED METHODS:
- Syntax: obj.method()
- Can accept parameters
- Explicit method calls
- Can have side effects
- More flexible
- Better for actions/operations

PROPERTY METHODS:
- Syntax: obj.attribute
- No additional parameters
- Attribute-like access
- Getter/setter/deleter support
- Better for computed attributes
- Cleaner API for simple values

BEST PRACTICES:
==============

1. Use properties for values that feel like attributes
2. Use computed methods for operations that need parameters
3. Cache expensive property calculations when appropriate
4. Validate inputs in property setters
5. Use descriptive names that indicate the nature of the computation
6. Consider thread safety for cached properties in multi-threaded applications
7. Document the computational complexity of properties
8. Use properties for unit conversions and data transformations
"""
