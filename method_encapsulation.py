"""
Method Encapsulation in Python

Encapsulation is one of the fundamental principles of Object-Oriented Programming (OOP).
It refers to the bundling of data and methods that operate on that data within a single unit (class),
and restricting direct access to some of the object's components.

In Python, method encapsulation is achieved through naming conventions:
1. Public methods: No underscore prefix (e.g., method_name)
2. Protected methods: Single underscore prefix (e.g., _method_name) - convention only
3. Private methods: Double underscore prefix (e.g., __method_name) - name mangling applied
"""

# Example 1: Basic Method Encapsulation
class Calculator:
    def __init__(self):
        self.result = 0  # Public attribute
    
    # Private method - hidden from external access through name mangling
    # Python transforms __validate to _Calculator__validate internally
    def __validate(self, num):
        """
        Private validation method - cannot be accessed directly from outside the class.
        This method is 'hidden' because Python applies name mangling:
        __validate becomes _Calculator__validate internally.
        """
        if not isinstance(num, (int, float)):  # Fixed typo: flaot -> float
            return False
        return True
    
    # Public method - accessible from outside the class
    def add(self, num):
        """
        Public method that uses the private validation method.
        External code can call this method, but cannot directly call __validate.
        """
        if self.__validate(num):  # Calling private method from within the class
            self.result += num
        else:
            print("Invalid Number")

# Demonstrating encapsulation
calc = Calculator()
calc.add(10)  # Public method - works fine
calc.add(5)   # Public method - works fine
print(f"Result: {calc.result}")

# Attempting to access private method directly - this will fail
try:
    calc.__validate(10)  # This will raise AttributeError
except AttributeError as e:
    print(f"Error accessing private method: {e}")

# However, you can still access it using name mangling (not recommended)
print(f"Accessing private method via name mangling: {calc._Calculator__validate(10)}")

print("\n" + "="*60 + "\n")

# Example 2: Bank Account with Multiple Encapsulation Types
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number    # Public attribute
        self._balance = initial_balance         # Protected attribute (convention)
        self.__pin = None                       # Private attribute
        self.__transaction_history = []         # Private attribute
    
    # Private method - completely hidden from external access
    def __validate_pin(self, pin):
        """
        Private method to validate PIN.
        This method is hidden to prevent external tampering with security logic.
        """
        return self.__pin == pin
    
    # Private method - internal logging
    def __log_transaction(self, transaction_type, amount):
        """
        Private method to log transactions.
        Hidden to maintain data integrity of transaction history.
        """
        self.__transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'timestamp': 'current_time'
        })
    
    # Protected method - intended for internal use or inheritance
    def _calculate_interest(self, rate):
        """
        Protected method - indicated by single underscore.
        This is a convention suggesting the method is for internal use
        or for use by subclasses, but it's still accessible externally.
        """
        return self._balance * rate / 100
    
    # Public method - external interface
    def set_pin(self, new_pin):
        """Public method to set PIN - provides controlled access to private data."""
        if len(str(new_pin)) == 4:
            self.__pin = new_pin
            return True
        return False
    
    # Public method - external interface
    def withdraw(self, amount, pin):
        """
        Public method that uses private validation.
        Demonstrates how public methods can use private methods internally.
        """
        if not self.__validate_pin(pin):
            return "Invalid PIN"
        
        if amount > self._balance:
            return "Insufficient funds"
        
        self._balance -= amount
        self.__log_transaction("withdrawal", amount)
        return f"Withdrawn: ${amount}"
    
    # Public method - external interface
    def deposit(self, amount):
        """Public method for deposits."""
        if amount > 0:
            self._balance += amount
            self.__log_transaction("deposit", amount)
            return f"Deposited: ${amount}"
        return "Invalid amount"
    
    # Public method - controlled access to private data
    def get_balance(self, pin):
        """Public method that provides controlled access to balance."""
        if self.__validate_pin(pin):
            return self._balance
        return "Invalid PIN"

# Demonstrating different levels of encapsulation
account = BankAccount("12345", 1000)
account.set_pin(1234)

# Public methods work fine
print(account.deposit(500))
print(account.withdraw(200, 1234))
print(f"Balance: ${account.get_balance(1234)}")

# Protected method - accessible but not recommended
interest = account._calculate_interest(5)
print(f"Interest calculation: ${interest}")

# Private methods - not directly accessible
try:
    account.__validate_pin(1234)  # This will fail
except AttributeError as e:
    print(f"Cannot access private method: {e}")

print("\n" + "="*60 + "\n")

# Example 3: Different Types of Method Encapsulation
class DataProcessor:
    def __init__(self):
        self.data = []
        self._cache = {}           # Protected - for internal use
        self.__secret_key = "xyz"  # Private - completely hidden
    
    # Public method
    def add_data(self, item):
        """Public method - part of the class interface."""
        self.data.append(item)
        self._invalidate_cache()  # Calling protected method
    
    # Protected method (single underscore)
    def _invalidate_cache(self):
        """
        Protected method - convention suggests internal use.
        Still accessible from outside but indicates it's not part of public API.
        """
        self._cache.clear()
    
    # Protected method
    def _get_cached_result(self, key):
        """Protected method for cache management."""
        return self._cache.get(key)
    
    # Private method (double underscore)
    def __encrypt_data(self, data):
        """
        Private method - name mangling applied.
        Completely hidden from external access through normal means.
        """
        return f"encrypted_{data}_{self.__secret_key}"
    
    # Private method
    def __decrypt_data(self, encrypted_data):
        """Private method for decryption."""
        return encrypted_data.replace(f"encrypted_", "").replace(f"_{self.__secret_key}", "")
    
    # Public method using private methods
    def process_secure_data(self, data):
        """
        Public method that uses private methods internally.
        External code can call this but cannot access the encryption logic directly.
        """
        encrypted = self.__encrypt_data(data)
        # Some processing...
        decrypted = self.__decrypt_data(encrypted)
        return f"Processed: {decrypted}"

# Demonstrating the different access levels
processor = DataProcessor()

# Public method - works
processor.add_data("test")
print(f"Data: {processor.data}")

# Protected method - accessible but not recommended
processor._invalidate_cache()  # Works but violates convention

# Private method - not accessible
try:
    processor.__encrypt_data("secret")  # This will fail
except AttributeError as e:
    print(f"Private method not accessible: {e}")

# Public method using private methods - works
result = processor.process_secure_data("confidential")
print(result)

print("\n" + "="*60 + "\n")

"""
Summary of Method Encapsulation Types in Python:

1. PUBLIC METHODS (no underscore):
   - Fully accessible from outside the class
   - Part of the class's public interface
   - Example: def method_name(self)

2. PROTECTED METHODS (single underscore _):
   - Convention indicating internal use
   - Still accessible from outside but shouldn't be used
   - Intended for use within the class or its subclasses
   - Example: def _method_name(self)

3. PRIVATE METHODS (double underscore __):
   - Name mangling applied by Python
   - Not directly accessible from outside the class
   - Provides true encapsulation
   - Example: def __method_name(self)

Benefits of Method Encapsulation:
- Data Protection: Prevents external code from corrupting internal state
- Interface Clarity: Clear distinction between public API and internal implementation
- Maintainability: Internal methods can be changed without affecting external code
- Security: Sensitive operations can be hidden from external access
- Code Organization: Logical separation of concerns within the class
"""
