"""
DECORATORS IN PYTHON
====================

A decorator is a function that takes another function as an argument and extends 
or modifies its behavior without permanently modifying the function itself.

Think of it like wrapping a gift - the gift (original function) stays the same,
but you add wrapping paper (decorator) around it.

SYNTAX:
    @decorator_name
    def function():
        pass

This is equivalent to:
    function = decorator_name(function)
"""

# ============================================================================
# EXAMPLE 1: Basic Decorator
# ============================================================================

def simple_decorator(func):
    """A basic decorator that prints before and after function execution"""
    def wrapper():
        print("Before function call")
        func()  # Call the original function
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# Usage:
# say_hello()
# Output:
# Before function call
# Hello!
# After function call


# ============================================================================
# EXAMPLE 2: Decorator with Arguments
# ============================================================================

def decorator_with_args(func):
    """Decorator that handles functions with arguments"""
    def wrapper(*args, **kwargs):
        print(f"Function called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function returned: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Usage:
# add(5, 3)
# greet("Alice", greeting="Hi")


# ============================================================================
# EXAMPLE 3: Timing Decorator (Practical Use Case)
# ============================================================================

import time

def timer(func):
    """Measures execution time of a function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done!"

@timer
def calculate_sum(n):
    return sum(range(n))

# Usage:
# slow_function()
# calculate_sum(1000000)


# ============================================================================
# EXAMPLE 4: Decorator with Parameters
# ============================================================================

def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                print(f"Execution {i + 1}:")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def say_hi():
    print("Hi there!")

@repeat(times=2)
def count_to(n):
    for i in range(1, n + 1):
        print(i, end=" ")
    print()

# Usage:
# say_hi()
# count_to(5)


# ============================================================================
# EXAMPLE 5: Authentication Decorator
# ============================================================================

def require_auth(func):
    """Simulates authentication check"""
    def wrapper(user, *args, **kwargs):
        if user.get("authenticated"):
            print(f"User {user['name']} is authenticated")
            return func(user, *args, **kwargs)
        else:
            print("Access denied! Please log in.")
            return None
    return wrapper

@require_auth
def view_profile(user):
    return f"Profile: {user['name']}, Email: {user['email']}"

@require_auth
def delete_account(user):
    return f"Account {user['name']} deleted"

# Usage:
# authenticated_user = {"name": "Alice", "email": "alice@example.com", "authenticated": True}
# guest_user = {"name": "Guest", "email": "", "authenticated": False}
# view_profile(authenticated_user)
# view_profile(guest_user)


# ============================================================================
# EXAMPLE 6: Logging Decorator
# ============================================================================

def log_calls(func):
    """Logs function calls with arguments"""
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {func.__name__}")
        print(f"[LOG] Arguments: {args}, {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f"[LOG] {func.__name__} raised exception: {e}")
            raise
    return wrapper

@log_calls
def divide(a, b):
    return a / b

# Usage:
# divide(10, 2)
# divide(10, 0)  # Will log the exception


# ============================================================================
# EXAMPLE 7: Caching/Memoization Decorator
# ============================================================================

def memoize(func):
    """Caches function results to avoid redundant calculations"""
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        print(f"Calculating result for {args}")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@memoize
def expensive_calculation(x, y):
    time.sleep(1)  # Simulate expensive operation
    return x ** y

# Usage:
# fibonacci(10)
# fibonacci(10)  # Second call uses cache
# expensive_calculation(2, 10)
# expensive_calculation(2, 10)  # Instant result from cache


# ============================================================================
# EXAMPLE 8: Multiple Decorators (Stacking)
# ============================================================================

def uppercase(func):
    """Converts result to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    """Adds exclamation marks"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"{result}!!!"
    return wrapper

@exclaim
@uppercase
def greet_person(name):
    return f"hello, {name}"

# Decorators are applied bottom-up:
# 1. uppercase is applied first
# 2. exclaim is applied second
# Usage:
# greet_person("alice")  # Returns: "HELLO, ALICE!!!"


# ============================================================================
# EXAMPLE 9: Class-based Decorator
# ============================================================================

class CountCalls:
    """Decorator that counts how many times a function is called"""
    def __init__(self, func):
        self.func = func
        self.count = 0
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} has been called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def process_data(data):
    return f"Processing: {data}"

# Usage:
# process_data("file1.txt")
# process_data("file2.txt")
# process_data("file3.txt")


# ============================================================================
# EXAMPLE 10: Preserving Function Metadata with functools.wraps
# ============================================================================

from functools import wraps

def better_decorator(func):
    """Decorator that preserves original function metadata"""
    @wraps(func)  # This preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@better_decorator
def documented_function(x, y):
    """This function adds two numbers"""
    return x + y

# Without @wraps, documented_function.__name__ would be "wrapper"
# With @wraps, it correctly shows "documented_function"
# Usage:
# print(documented_function.__name__)  # "documented_function"
# print(documented_function.__doc__)   # "This function adds two numbers"


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

def validate_positive(func):
    """Ensures all numeric arguments are positive"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative value not allowed: {arg}")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def calculate_area(length, width):
    return length * width

# Usage:
# calculate_area(5, 10)  # Works
# calculate_area(-5, 10)  # Raises ValueError


def retry(max_attempts=3):
    """Retries function execution on failure"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorator

@retry(max_attempts=3)
def unstable_network_call():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Network error")
    return "Success!"

# Usage:
# unstable_network_call()  # Will retry up to 3 times


# ============================================================================
# DEMONSTRATION FUNCTION
# ============================================================================

def demonstrate_decorators():
    print("=== Basic Decorator ===")
    say_hello()
    
    print("\n=== Decorator with Arguments ===")
    result = add(5, 3)
    greet("Bob")
    
    print("\n=== Timing Decorator ===")
    slow_function()
    
    print("\n=== Repeat Decorator ===")
    say_hi()
    
    print("\n=== Authentication Decorator ===")
    auth_user = {"name": "Alice", "email": "alice@example.com", "authenticated": True}
    guest = {"name": "Guest", "email": "", "authenticated": False}
    view_profile(auth_user)
    view_profile(guest)
    
    print("\n=== Memoization ===")
    print(f"Fibonacci(5) = {fibonacci(5)}")
    print(f"Fibonacci(5) again = {fibonacci(5)}")
    
    print("\n=== Multiple Decorators ===")
    print(greet_person("charlie"))
    
    print("\n=== Class-based Decorator ===")
    process_data("data1")
    process_data("data2")
    
    print("\n=== Function Metadata ===")
    print(f"Function name: {documented_function.__name__}")
    print(f"Function doc: {documented_function.__doc__}")

if __name__ == "__main__":
    demonstrate_decorators()
