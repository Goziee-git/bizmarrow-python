"""
GENERATORS IN PYTHON
====================

A generator is a special type of function that returns an iterator and generates values
one at a time using the 'yield' keyword instead of 'return'. This allows you to iterate
over a sequence of values without storing the entire sequence in memory.

KEY DIFFERENCES: Generator vs Regular Function
-----------------------------------------------
Regular Function:
- Uses 'return' to send back a value
- Returns once and terminates
- Stores all values in memory

Generator Function:
- Uses 'yield' to produce values one at a time
- Can yield multiple times
- Pauses execution and resumes where it left off
- Memory efficient (lazy evaluation)

SYNTAX:
    def generator_function():
        yield value1
        yield value2
        yield value3

WHY USE GENERATORS?
-------------------
1. Memory Efficiency: Generate values on-the-fly instead of storing everything
2. Infinite Sequences: Can represent infinite data streams
3. Pipeline Processing: Chain operations without intermediate storage
4. Better Performance: Process large datasets without loading everything into memory
"""

# ============================================================================
# EXAMPLE 1: Basic Generator - Understanding yield
# ============================================================================

def simple_generator():
    """A basic generator that yields three values"""
    print("First yield")
    yield 1
    
    print("Second yield")
    yield 2
    
    print("Third yield")
    yield 3
    
    print("Generator exhausted")

# How to use it:
def demo_simple_generator():
    print("=== Simple Generator Demo ===")
    gen = simple_generator()  # Creates generator object, doesn't execute yet
    
    print(f"Generator object: {gen}")
    print(f"First value: {next(gen)}")   # Executes until first yield
    print(f"Second value: {next(gen)}")  # Resumes and executes until second yield
    print(f"Third value: {next(gen)}")   # Resumes and executes until third yield
    # next(gen) would raise StopIteration
    
    print("\nUsing for loop:")
    for value in simple_generator():
        print(f"Got: {value}")


# ============================================================================
# EXAMPLE 2: Generator vs Regular Function - Memory Comparison
# ============================================================================

# Regular function - stores everything in memory
def get_numbers_list(n):
    """Returns a list of numbers from 0 to n-1"""
    result = []
    for i in range(n):
        result.append(i)
    return result  # All values stored in memory

# Generator function - generates values on demand
def get_numbers_generator(n):
    """Yields numbers from 0 to n-1 one at a time"""
    for i in range(n):
        yield i  # Only current value in memory

def demo_memory_efficiency():
    print("\n=== Memory Efficiency Demo ===")
    
    # List approach - all 1 million numbers in memory
    # numbers_list = get_numbers_list(1000000)  # Uses ~8MB of memory
    
    # Generator approach - only one number at a time
    numbers_gen = get_numbers_generator(1000000)  # Uses minimal memory
    
    # Both can be iterated the same way
    print("First 5 from generator:")
    for i, num in enumerate(numbers_gen):
        if i >= 5:
            break
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 3: Countdown Generator
# ============================================================================

def countdown(n):
    """Generator that counts down from n to 1"""
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n
        n -= 1
    print("Blastoff!")

def demo_countdown():
    print("\n=== Countdown Generator ===")
    for count in countdown(5):
        print(count)


# ============================================================================
# EXAMPLE 4: Infinite Sequence Generator
# ============================================================================

def infinite_counter(start=0):
    """Generates infinite sequence of numbers"""
    count = start
    while True:  # Infinite loop!
        yield count
        count += 1

def demo_infinite():
    print("\n=== Infinite Generator Demo ===")
    counter = infinite_counter(10)
    
    # Get first 10 values from infinite sequence
    for i in range(10):
        print(next(counter), end=" ")
    print()


# ============================================================================
# EXAMPLE 5: Fibonacci Generator
# ============================================================================

def fibonacci():
    """Generates Fibonacci sequence infinitely"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def fibonacci_limited(n):
    """Generates first n Fibonacci numbers"""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

def demo_fibonacci():
    print("\n=== Fibonacci Generator ===")
    
    # Get first 10 Fibonacci numbers
    fib = fibonacci()
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(next(fib), end=" ")
    print()
    
    # Using limited version
    print("\nUsing fibonacci_limited(15):")
    for num in fibonacci_limited(15):
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 6: Reading Large Files Line by Line
# ============================================================================

def read_large_file(filepath):
    """
    Generator for reading large files line by line
    Memory efficient - doesn't load entire file into memory
    """
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

def demo_file_reading():
    print("\n=== File Reading Generator ===")
    # Example usage (would need actual file)
    # for line in read_large_file('large_file.txt'):
    #     process(line)
    print("Generator reads files line by line without loading entire file")


# ============================================================================
# EXAMPLE 7: Range-like Generator
# ============================================================================

def my_range(start, stop=None, step=1):
    """Custom implementation of range() using generator"""
    if stop is None:
        stop = start
        start = 0
    
    current = start
    if step > 0:
        while current < stop:
            yield current
            current += step
    else:
        while current > stop:
            yield current
            current += step

def demo_my_range():
    print("\n=== Custom Range Generator ===")
    
    print("my_range(5):")
    for num in my_range(5):
        print(num, end=" ")
    print()
    
    print("\nmy_range(2, 10, 2):")
    for num in my_range(2, 10, 2):
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 8: Generator with State
# ============================================================================

def running_average():
    """Generator that maintains running average"""
    total = 0
    count = 0
    average = None
    
    while True:
        value = yield average  # Receives value and yields average
        total += value
        count += 1
        average = total / count

def demo_running_average():
    print("\n=== Running Average Generator ===")
    avg = running_average()
    next(avg)  # Prime the generator
    
    numbers = [10, 20, 30, 40, 50]
    for num in numbers:
        result = avg.send(num)  # Send value and get average
        print(f"Added {num}, Running average: {result}")


# ============================================================================
# EXAMPLE 9: Batch Processing Generator
# ============================================================================

def batch_data(data, batch_size):
    """Yields data in batches of specified size"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def demo_batch_processing():
    print("\n=== Batch Processing Generator ===")
    
    data = list(range(1, 21))  # [1, 2, 3, ..., 20]
    print(f"Original data: {data}")
    
    print("\nProcessing in batches of 5:")
    for batch_num, batch in enumerate(batch_data(data, 5), 1):
        print(f"Batch {batch_num}: {batch}")


# ============================================================================
# EXAMPLE 10: Filtering with Generators
# ============================================================================

def even_numbers(numbers):
    """Generator that yields only even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def squares(numbers):
    """Generator that yields squares of numbers"""
    for num in numbers:
        yield num ** 2

def demo_filtering():
    print("\n=== Filtering with Generators ===")
    
    data = range(1, 11)
    
    # Chain generators together
    evens = even_numbers(data)
    squared_evens = squares(evens)
    
    print("Squares of even numbers from 1-10:")
    for num in squared_evens:
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 11: Generator Expressions (Generator Comprehension)
# ============================================================================

def demo_generator_expressions():
    print("\n=== Generator Expressions ===")
    
    # List comprehension - creates entire list in memory
    squares_list = [x**2 for x in range(10)]
    print(f"List comprehension: {squares_list}")
    print(f"Type: {type(squares_list)}")
    
    # Generator expression - creates generator object
    squares_gen = (x**2 for x in range(10))
    print(f"\nGenerator expression: {squares_gen}")
    print(f"Type: {type(squares_gen)}")
    
    print("Values from generator:")
    for num in squares_gen:
        print(num, end=" ")
    print()
    
    # Generator expressions are memory efficient
    sum_of_squares = sum(x**2 for x in range(1000000))
    print(f"\nSum of first million squares: {sum_of_squares}")


# ============================================================================
# EXAMPLE 12: Pipeline Processing
# ============================================================================

def read_data():
    """Simulates reading data"""
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for item in data:
        yield item

def filter_even(numbers):
    """Filters even numbers"""
    for num in numbers:
        if num % 2 == 0:
            yield num

def multiply_by_two(numbers):
    """Multiplies each number by 2"""
    for num in numbers:
        yield num * 2

def demo_pipeline():
    print("\n=== Pipeline Processing ===")
    
    # Create processing pipeline
    pipeline = multiply_by_two(filter_even(read_data()))
    
    print("Processing pipeline: read -> filter even -> multiply by 2")
    print("Results:", list(pipeline))


# ============================================================================
# EXAMPLE 13: Permutations Generator
# ============================================================================

def permutations(items):
    """Generates all permutations of items"""
    if len(items) <= 1:
        yield items
    else:
        for i in range(len(items)):
            current = items[i]
            remaining = items[:i] + items[i+1:]
            for perm in permutations(remaining):
                yield [current] + perm

def demo_permutations():
    print("\n=== Permutations Generator ===")
    
    items = [1, 2, 3]
    print(f"Permutations of {items}:")
    for perm in permutations(items):
        print(perm)


# ============================================================================
# EXAMPLE 14: Sliding Window Generator
# ============================================================================

def sliding_window(data, window_size):
    """Generates sliding windows of specified size"""
    for i in range(len(data) - window_size + 1):
        yield data[i:i + window_size]

def demo_sliding_window():
    print("\n=== Sliding Window Generator ===")
    
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    window_size = 3
    
    print(f"Data: {data}")
    print(f"Window size: {window_size}")
    print("Windows:")
    for window in sliding_window(data, window_size):
        print(window)


# ============================================================================
# EXAMPLE 15: Tree Traversal Generator
# ============================================================================

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(node):
    """Generator for inorder tree traversal"""
    if node:
        # Traverse left subtree
        yield from inorder_traversal(node.left)
        # Visit current node
        yield node.value
        # Traverse right subtree
        yield from inorder_traversal(node.right)

def demo_tree_traversal():
    print("\n=== Tree Traversal Generator ===")
    
    # Create a simple binary tree
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    
    root = TreeNode(4,
                    TreeNode(2, TreeNode(1), TreeNode(3)),
                    TreeNode(6, TreeNode(5), TreeNode(7)))
    
    print("Inorder traversal:")
    for value in inorder_traversal(root):
        print(value, end=" ")
    print()


# ============================================================================
# PRACTICAL USE CASES
# ============================================================================

def demo_practical_use_cases():
    print("\n=== Practical Use Cases ===")
    
    print("\n1. Processing CSV files:")
    print("   for row in read_csv_generator('data.csv'):")
    print("       process(row)")
    
    print("\n2. API pagination:")
    print("   for page in fetch_pages(api_url):")
    print("       process(page)")
    
    print("\n3. Database queries:")
    print("   for record in fetch_records_batch(query, batch_size=1000):")
    print("       process(record)")
    
    print("\n4. Log file analysis:")
    print("   for line in read_logs('app.log'):")
    print("       if 'ERROR' in line:")
    print("           analyze(line)")
    
    print("\n5. Data streaming:")
    print("   for data_chunk in stream_data(source):")
    print("       transform_and_save(data_chunk)")


# ============================================================================
# GENERATOR METHODS
# ============================================================================

def demo_generator_methods():
    print("\n=== Generator Methods ===")
    
    def counter():
        count = 0
        while True:
            value = yield count
            if value is not None:
                count = value
            else:
                count += 1
    
    gen = counter()
    
    # next() - Get next value
    print(f"next(gen): {next(gen)}")
    print(f"next(gen): {next(gen)}")
    
    # send() - Send value to generator
    print(f"gen.send(10): {gen.send(10)}")
    print(f"next(gen): {next(gen)}")
    
    # close() - Stop generator
    gen.close()
    print("Generator closed")


# ============================================================================
# COMPARISON: List vs Generator
# ============================================================================

def demo_comparison():
    print("\n=== List vs Generator Comparison ===")
    
    import sys
    
    # List - all values in memory
    numbers_list = [x for x in range(10000)]
    print(f"List size: {sys.getsizeof(numbers_list)} bytes")
    
    # Generator - values created on demand
    numbers_gen = (x for x in range(10000))
    print(f"Generator size: {sys.getsizeof(numbers_gen)} bytes")
    
    print("\nList: Fast random access, uses more memory")
    print("Generator: Memory efficient, one-time iteration")


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

def main():
    """Run all demonstrations"""
    demo_simple_generator()
    demo_memory_efficiency()
    demo_countdown()
    demo_infinite()
    demo_fibonacci()
    demo_file_reading()
    demo_my_range()
    demo_running_average()
    demo_batch_processing()
    demo_filtering()
    demo_generator_expressions()
    demo_pipeline()
    demo_permutations()
    demo_sliding_window()
    demo_tree_traversal()
    demo_practical_use_cases()
    demo_generator_methods()
    demo_comparison()

if __name__ == "__main__":
    main()
