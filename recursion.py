"""
RECURSION IN PYTHON
===================

Recursion is when a function calls itself to solve a problem by breaking it down
into smaller, similar subproblems.

KEY COMPONENTS:
1. Base Case: The condition that stops the recursion (prevents infinite loop)
2. Recursive Case: The function calling itself with modified arguments

STRUCTURE:
    def recursive_function(parameters):
        if base_case_condition:
            return base_case_value
        else:
            return recursive_function(modified_parameters)
"""

# ============================================================================
# EXAMPLE 1: Simple Countdown (Understanding the Basics)
# ============================================================================

def countdown(n):
    """Counts down from n to 1"""
    # Base case: stop when n reaches 0
    if n <= 0:
        print("Blastoff!")
        return
    
    # Recursive case: print and call with n-1
    print(n)
    countdown(n - 1)

# How it works:
# countdown(3) -> prints 3, calls countdown(2)
#   countdown(2) -> prints 2, calls countdown(1)
#     countdown(1) -> prints 1, calls countdown(0)
#       countdown(0) -> prints "Blastoff!", returns

# Usage:
# countdown(5)


# ============================================================================
# EXAMPLE 2: Factorial (Classic Example)
# ============================================================================

def factorial(n):
    """
    Calculates n! = n × (n-1) × (n-2) × ... × 1
    Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)

# How it works for factorial(5):
# factorial(5) = 5 * factorial(4)
#              = 5 * (4 * factorial(3))
#              = 5 * (4 * (3 * factorial(2)))
#              = 5 * (4 * (3 * (2 * factorial(1))))
#              = 5 * (4 * (3 * (2 * 1)))
#              = 5 * (4 * (3 * 2))
#              = 5 * (4 * 6)
#              = 5 * 24
#              = 120

# Usage:
# print(factorial(5))  # 120
# print(factorial(0))  # 1


# ============================================================================
# EXAMPLE 3: Fibonacci Sequence
# ============================================================================

def fibonacci(n):
    """
    Returns the nth Fibonacci number
    Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
    Rule: F(n) = F(n-1) + F(n-2)
    """
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)

# How it works for fibonacci(5):
#                    fib(5)
#                   /      \
#              fib(4)      fib(3)
#             /     \      /     \
#        fib(3)   fib(2) fib(2) fib(1)
#        /   \    /   \   /   \
#    fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
#    /   \
# fib(1) fib(0)

# Usage:
# for i in range(10):
#     print(f"F({i}) = {fibonacci(i)}")


# ============================================================================
# EXAMPLE 4: Sum of List Elements
# ============================================================================

def sum_list(numbers):
    """Calculates sum of all numbers in a list using recursion"""
    # Base case: empty list
    if len(numbers) == 0:
        return 0
    
    # Recursive case: first element + sum of rest
    return numbers[0] + sum_list(numbers[1:])

# How it works for sum_list([1, 2, 3, 4]):
# sum_list([1, 2, 3, 4]) = 1 + sum_list([2, 3, 4])
#                        = 1 + (2 + sum_list([3, 4]))
#                        = 1 + (2 + (3 + sum_list([4])))
#                        = 1 + (2 + (3 + (4 + sum_list([]))))
#                        = 1 + (2 + (3 + (4 + 0)))
#                        = 10

# Usage:
# print(sum_list([1, 2, 3, 4, 5]))  # 15


# ============================================================================
# EXAMPLE 5: Power Function
# ============================================================================

def power(base, exponent):
    """
    Calculates base^exponent using recursion
    Example: 2^3 = 2 × 2 × 2 = 8
    """
    # Base case
    if exponent == 0:
        return 1
    
    # Recursive case: base^n = base × base^(n-1)
    return base * power(base, exponent - 1)

# Optimized version (divide and conquer):
def power_optimized(base, exponent):
    """More efficient: O(log n) instead of O(n)"""
    if exponent == 0:
        return 1
    
    # If exponent is even: base^n = (base^(n/2))^2
    if exponent % 2 == 0:
        half = power_optimized(base, exponent // 2)
        return half * half
    # If exponent is odd: base^n = base × base^(n-1)
    else:
        return base * power_optimized(base, exponent - 1)

# Usage:
# print(power(2, 5))  # 32
# print(power_optimized(2, 10))  # 1024


# ============================================================================
# EXAMPLE 6: String Reversal
# ============================================================================

def reverse_string(s):
    """Reverses a string using recursion"""
    # Base case: empty or single character
    if len(s) <= 1:
        return s
    
    # Recursive case: last char + reverse of rest
    return s[-1] + reverse_string(s[:-1])

# How it works for reverse_string("hello"):
# reverse_string("hello") = "o" + reverse_string("hell")
#                         = "o" + ("l" + reverse_string("hel"))
#                         = "o" + ("l" + ("l" + reverse_string("he")))
#                         = "o" + ("l" + ("l" + ("e" + reverse_string("h"))))
#                         = "o" + ("l" + ("l" + ("e" + "h")))
#                         = "olleh"

# Usage:
# print(reverse_string("hello"))  # "olleh"


# ============================================================================
# EXAMPLE 7: Palindrome Check
# ============================================================================

def is_palindrome(s):
    """Checks if a string is a palindrome using recursion"""
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Base cases
    if len(s) <= 1:
        return True
    
    # Check first and last characters
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check middle part
    return is_palindrome(s[1:-1])

# Usage:
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("hello"))    # False
# print(is_palindrome("A man a plan a canal Panama"))  # True


# ============================================================================
# EXAMPLE 8: Binary Search (Divide and Conquer)
# ============================================================================

def binary_search(arr, target, left=0, right=None):
    """
    Searches for target in sorted array using recursion
    Returns index if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    # Base case: element not found
    if left > right:
        return -1
    
    # Find middle
    mid = (left + right) // 2
    
    # Base case: element found
    if arr[mid] == target:
        return mid
    
    # Recursive cases
    if arr[mid] > target:
        # Search left half
        return binary_search(arr, target, left, mid - 1)
    else:
        # Search right half
        return binary_search(arr, target, mid + 1, right)

# Usage:
# sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
# print(binary_search(sorted_list, 7))   # 3
# print(binary_search(sorted_list, 10))  # -1


# ============================================================================
# EXAMPLE 9: Greatest Common Divisor (GCD) - Euclidean Algorithm
# ============================================================================

def gcd(a, b):
    """
    Finds the greatest common divisor of two numbers
    Uses Euclidean algorithm: gcd(a, b) = gcd(b, a % b)
    """
    # Base case
    if b == 0:
        return a
    
    # Recursive case
    return gcd(b, a % b)

# How it works for gcd(48, 18):
# gcd(48, 18) = gcd(18, 48 % 18) = gcd(18, 12)
#             = gcd(12, 18 % 12) = gcd(12, 6)
#             = gcd(6, 12 % 6)   = gcd(6, 0)
#             = 6

# Usage:
# print(gcd(48, 18))  # 6
# print(gcd(100, 35))  # 5


# ============================================================================
# EXAMPLE 10: Flatten Nested List
# ============================================================================

def flatten(nested_list):
    """Flattens a nested list of arbitrary depth"""
    result = []
    
    for item in nested_list:
        # Base case: item is not a list
        if not isinstance(item, list):
            result.append(item)
        # Recursive case: item is a list
        else:
            result.extend(flatten(item))
    
    return result

# Usage:
# nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
# print(flatten(nested))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ============================================================================
# EXAMPLE 11: Directory Tree Traversal
# ============================================================================

def count_files(path, indent=0):
    """
    Recursively counts and displays files in a directory
    (Conceptual example - would need os module to actually run)
    """
    import os
    
    if not os.path.exists(path):
        return 0
    
    count = 0
    
    try:
        # Base case: it's a file
        if os.path.isfile(path):
            print("  " * indent + f"File: {os.path.basename(path)}")
            return 1
        
        # Recursive case: it's a directory
        print("  " * indent + f"Dir: {os.path.basename(path)}/")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            count += count_files(item_path, indent + 1)
        
        return count
    except PermissionError:
        return 0

# Usage:
# total = count_files(".")
# print(f"Total files: {total}")


# ============================================================================
# EXAMPLE 12: Tower of Hanoi (Classic Puzzle)
# ============================================================================

def tower_of_hanoi(n, source, destination, auxiliary):
    """
    Solves the Tower of Hanoi puzzle
    n: number of disks
    source: starting peg
    destination: target peg
    auxiliary: helper peg
    """
    # Base case: only one disk
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    # Recursive case:
    # 1. Move n-1 disks from source to auxiliary (using destination)
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # 2. Move the largest disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")
    
    # 3. Move n-1 disks from auxiliary to destination (using source)
    tower_of_hanoi(n - 1, auxiliary, destination, source)

# Usage:
# tower_of_hanoi(3, 'A', 'C', 'B')


# ============================================================================
# EXAMPLE 13: Permutations
# ============================================================================

def permutations(items):
    """Generates all permutations of a list"""
    # Base case: empty or single item
    if len(items) <= 1:
        return [items]
    
    result = []
    
    # Recursive case: for each item, generate permutations of remaining items
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i+1:]
        
        # Get permutations of remaining items
        for perm in permutations(remaining):
            result.append([current] + perm)
    
    return result

# Usage:
# print(permutations([1, 2, 3]))
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]


# ============================================================================
# RECURSION VS ITERATION COMPARISON
# ============================================================================

# Recursive version
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Both produce the same result, but:
# - Recursive: More elegant, easier to understand for some problems
# - Iterative: More efficient (no function call overhead), no stack overflow risk


# ============================================================================
# TAIL RECURSION (Optimization Concept)
# ============================================================================

def factorial_tail_recursive(n, accumulator=1):
    """
    Tail recursive version - last operation is the recursive call
    (Python doesn't optimize tail recursion, but some languages do)
    """
    if n <= 1:
        return accumulator
    return factorial_tail_recursive(n - 1, n * accumulator)

# Usage:
# print(factorial_tail_recursive(5))  # 120


# ============================================================================
# DEMONSTRATION FUNCTION
# ============================================================================

def demonstrate_recursion():
    print("=== Countdown ===")
    countdown(5)
    
    print("\n=== Factorial ===")
    print(f"5! = {factorial(5)}")
    
    print("\n=== Fibonacci ===")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}", end="  ")
    print()
    
    print("\n=== Sum List ===")
    print(f"Sum of [1,2,3,4,5] = {sum_list([1,2,3,4,5])}")
    
    print("\n=== Power ===")
    print(f"2^10 = {power(2, 10)}")
    
    print("\n=== String Reversal ===")
    print(f"Reverse of 'hello' = {reverse_string('hello')}")
    
    print("\n=== Palindrome Check ===")
    print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
    print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")
    
    print("\n=== Binary Search ===")
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Search 7 in {arr}: index {binary_search(arr, 7)}")
    
    print("\n=== GCD ===")
    print(f"GCD(48, 18) = {gcd(48, 18)}")
    
    print("\n=== Flatten Nested List ===")
    nested = [1, [2, 3], [4, [5, 6]], 7]
    print(f"Flatten {nested} = {flatten(nested)}")
    
    print("\n=== Tower of Hanoi (3 disks) ===")
    tower_of_hanoi(3, 'A', 'C', 'B')
    
    print("\n=== Permutations ===")
    print(f"Permutations of [1,2,3]:")
    for perm in permutations([1, 2, 3]):
        print(perm)

if __name__ == "__main__":
    demonstrate_recursion()
