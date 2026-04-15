"""
ITERATORS IN PYTHON
===================

An iterator is an object that implements two special methods:
1. __iter__() - Returns the iterator object itself
2. __next__() - Returns the next value from the iterator

When there are no more items to return, __next__() raises StopIteration exception.

WHAT IS AN ITERATOR?
--------------------
An iterator is an object that can be iterated (looped) upon. It represents a stream
of data that returns one element at a time.

ITERABLE vs ITERATOR:
---------------------
- Iterable: An object that has __iter__() method (list, tuple, string, dict)
- Iterator: An object that has both __iter__() and __next__() methods

PROTOCOL:
---------
1. __iter__() must return the iterator object (usually self)
2. __next__() must return the next value or raise StopIteration when done
3. Once StopIteration is raised, the iterator is exhausted

WHY USE CUSTOM ITERATORS?
--------------------------
1. Create custom iteration behavior
2. Lazy evaluation (compute values on demand)
3. Memory efficiency
4. Represent infinite sequences
5. Encapsulate complex iteration logic
"""

# ============================================================================
# EXAMPLE 1: Basic Iterator - Understanding the Concept
# ============================================================================

class SimpleIterator:
    """A basic iterator that counts from 1 to n"""
    #we can use this to initialise the iterator(list, dict, str, sets, tuples)
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0
    #this method makes the obj an iterable
    def __iter__(self):
        """Returns the iterator object (self)"""
        print("__iter__() called")
        return self
    
    def __next__(self):
        """Returns the next value"""
        print(f"__next__() called, current = {self.current}")
        
        self.current += 1
        
        if self.current > self.max_count:
            print("Raising StopIteration")
            raise StopIteration
        
        return self.current

def demo_simple_iterator():
    print("=== Simple Iterator Demo ===")
    
    iterator = SimpleIterator(3)
    
    # Manual iteration using next()
    print("\nManual iteration:")
    print(f"Value: {next(iterator)}")
    print(f"Value: {next(iterator)}")
    print(f"Value: {next(iterator)}")
    # next(iterator)  # Would raise StopIteration
    
    # Using for loop (calls __iter__() and __next__() automatically)
    print("\nUsing for loop:")
    iterator2 = SimpleIterator(3)
    for value in iterator2:
        print(f"Got: {value}")


# ============================================================================
# EXAMPLE 2: How Built-in Iterables Work
# ============================================================================

def demo_builtin_iterables():
    print("\n=== Built-in Iterables Demo ===")
    
    # List is iterable
    my_list = [1, 2, 3]
    
    # Get iterator from iterable
    iterator = iter(my_list)  # Calls my_list.__iter__()
    
    print(f"List: {my_list}")
    print(f"Iterator: {iterator}")
    
    # Use next() to get values
    print(f"First: {next(iterator)}")   # Calls iterator.__next__()
    print(f"Second: {next(iterator)}")
    print(f"Third: {next(iterator)}")
    # next(iterator)  # Would raise StopIteration
    
    # This is what for loop does internally:
    print("\nWhat for loop does internally:")
    my_list2 = ['a', 'b', 'c']
    iterator2 = iter(my_list2)
    while True:
        try:
            item = next(iterator2)
            print(item)
        except StopIteration:
            break


# ============================================================================
# EXAMPLE 3: Countdown Iterator
# ============================================================================

class Countdown:
    """Iterator that counts down from start to 0"""
    
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        return value

def demo_countdown():
    print("\n=== Countdown Iterator ===")
    
    countdown = Countdown(5)
    
    for num in countdown:
        print(num, end=" ")
    


# ============================================================================
# EXAMPLE 4: Even Numbers Iterator
# ============================================================================

class EvenNumbers:
    """Iterator that generates even numbers up to max_value"""
    
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        
        value = self.current
        self.current += 2
        return value

def demo_even_numbers():
    print("\n=== Even Numbers Iterator ===")
    
    evens = EvenNumbers(10)
    
    print("Even numbers from 0 to 10:")
    for num in evens:
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 5: Fibonacci Iterator
# ============================================================================

class Fibonacci:
    """Iterator that generates Fibonacci sequence up to n terms"""
    
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        
        if self.count == 0:
            self.count += 1
            return self.a
        elif self.count == 1:
            self.count += 1
            return self.b
        else:
            result = self.a + self.b
            self.a = self.b
            self.b = result
            self.count += 1
            return result

def demo_fibonacci():
    print("\n=== Fibonacci Iterator ===")
    
    fib = Fibonacci(10)
    
    print("First 10 Fibonacci numbers:")
    for num in fib:
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 6: Infinite Iterator
# ============================================================================

class InfiniteCounter:
    """Iterator that counts infinitely from start"""
    
    def __init__(self, start=0):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        value = self.current
        self.current += 1
        return value

def demo_infinite():
    print("\n=== Infinite Iterator ===")
    
    counter = InfiniteCounter(10)
    
    print("First 10 values from infinite counter:")
    for i, value in enumerate(counter):
        if i >= 10:
            break
        print(value, end=" ")
    print()


# ============================================================================
# EXAMPLE 7: Range-like Iterator
# ============================================================================

class MyRange:
    """Custom implementation of range() as an iterator"""
    
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        
        self.step = step
        self.current = self.start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

def demo_my_range():
    print("\n=== Custom Range Iterator ===")
    
    print("MyRange(5):")
    for num in MyRange(5):
        print(num, end=" ")
    print()
    
    print("\nMyRange(2, 10, 2):")
    for num in MyRange(2, 10, 2):
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 8: Reverse Iterator
# ============================================================================

class ReverseIterator:
    """Iterator that iterates through a sequence in reverse"""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        
        self.index -= 1
        return self.data[self.index]

def demo_reverse():
    print("\n=== Reverse Iterator ===")
    
    data = [1, 2, 3, 4, 5]
    print(f"Original: {data}")
    
    print("Reversed:")
    for item in ReverseIterator(data):
        print(item, end=" ")
    print()


# ============================================================================
# EXAMPLE 9: Iterator with State Reset
# ============================================================================

class ReusableIterator:
    """Iterator that can be reset and reused"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        self.index = 0  # Reset on each iteration
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        value = self.data[self.index]
        self.index += 1
        return value
    
    def reset(self):
        """Manual reset method"""
        self.index = 0

def demo_reusable():
    print("\n=== Reusable Iterator ===")
    
    iterator = ReusableIterator([1, 2, 3])
    
    print("First iteration:")
    for item in iterator:
        print(item, end=" ")
    print()
    
    print("\nSecond iteration (automatically resets):")
    for item in iterator:
        print(item, end=" ")
    print()


# ============================================================================
# EXAMPLE 10: File Line Iterator
# ============================================================================

class FileLineIterator:
    """Iterator that reads file line by line"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        line = self.file.readline()
        
        if not line:
            self.file.close()
            raise StopIteration
        
        return line.strip()

def demo_file_iterator():
    print("\n=== File Line Iterator ===")
    print("(Conceptual example - would need actual file)")
    print("Usage:")
    print("  for line in FileLineIterator('data.txt'):")
    print("      process(line)")


# ============================================================================
# EXAMPLE 11: Batch Iterator
# ============================================================================

class BatchIterator:
    """Iterator that yields data in batches"""
    
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        batch = self.data[self.index:self.index + self.batch_size]
        self.index += self.batch_size
        return batch

def demo_batch_iterator():
    print("\n=== Batch Iterator ===")
    
    data = list(range(1, 16))  # [1, 2, 3, ..., 15]
    
    print(f"Data: {data}")
    print("\nBatches of 5:")
    
    for batch_num, batch in enumerate(BatchIterator(data, 5), 1):
        print(f"Batch {batch_num}: {batch}")


# ============================================================================
# EXAMPLE 12: Iterable Container Class
# ============================================================================

class MyList:
    """Custom list-like container that is iterable"""
    
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)
    
    def __iter__(self):
        """Returns a new iterator for this container"""
        return MyListIterator(self.items)

class MyListIterator:
    """Iterator for MyList"""
    
    def __init__(self, items):
        self.items = items
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        
        value = self.items[self.index]
        self.index += 1
        return value

def demo_iterable_container():
    print("\n=== Iterable Container Class ===")
    
    my_list = MyList()
    my_list.add("apple")
    my_list.add("banana")
    my_list.add("cherry")
    
    print("Items in MyList:")
    for item in my_list:
        print(f"  - {item}")
    
    print("\nCan iterate multiple times:")
    for item in my_list:
        print(f"  * {item}")


# ============================================================================
# EXAMPLE 13: Iterator with Filter
# ============================================================================

class FilterIterator:
    """Iterator that filters items based on a condition"""
    
    def __init__(self, data, condition):
        self.data = data
        self.condition = condition
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.data):
            item = self.data[self.index]
            self.index += 1
            
            if self.condition(item):
                return item
        
        raise StopIteration

def demo_filter_iterator():
    print("\n=== Filter Iterator ===")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print(f"Numbers: {numbers}")
    
    print("\nEven numbers only:")
    for num in FilterIterator(numbers, lambda x: x % 2 == 0):
        print(num, end=" ")
    print()
    
    print("\nNumbers greater than 5:")
    for num in FilterIterator(numbers, lambda x: x > 5):
        print(num, end=" ")
    print()


# ============================================================================
# EXAMPLE 14: Chained Iterator
# ============================================================================

class ChainIterator:
    """Iterator that chains multiple iterables together"""
    
    def __init__(self, *iterables):
        self.iterables = iterables
        self.current_iterable_index = 0
        self.current_iterator = iter(iterables[0]) if iterables else iter([])
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                return next(self.current_iterator)
            except StopIteration:
                self.current_iterable_index += 1
                
                if self.current_iterable_index >= len(self.iterables):
                    raise StopIteration
                
                self.current_iterator = iter(self.iterables[self.current_iterable_index])

def demo_chain_iterator():
    print("\n=== Chained Iterator ===")
    
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    list3 = [10, 20, 30]
    
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")
    print(f"List 3: {list3}")
    
    print("\nChained together:")
    for item in ChainIterator(list1, list2, list3):
        print(item, end=" ")
    print()


# ============================================================================
# COMPARISON: Iterator vs Generator
# ============================================================================

def demo_iterator_vs_generator():
    print("\n=== Iterator vs Generator Comparison ===")
    
    # Iterator class
    class CounterIterator:
        def __init__(self, n):
            self.n = n
            self.current = 0
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self.current >= self.n:
                raise StopIteration
            value = self.current
            self.current += 1
            return value
    
    # Generator function
    def counter_generator(n):
        for i in range(n):
            yield i
    
    print("Iterator class (more code):")
    for num in CounterIterator(5):
        print(num, end=" ")
    print()
    
    print("\nGenerator function (simpler):")
    for num in counter_generator(5):
        print(num, end=" ")
    print()
    
    print("\nUse iterators when:")
    print("  - Need complex state management")
    print("  - Want to encapsulate iteration logic in a class")
    print("  - Need multiple iterator instances with independent state")
    
    print("\nUse generators when:")
    print("  - Simple iteration logic")
    print("  - Want cleaner, more readable code")
    print("  - Don't need class-based structure")


# ============================================================================
# MAIN DEMONSTRATION
# ============================================================================

def main():
    """Run all demonstrations"""
    demo_simple_iterator()
    demo_builtin_iterables()
    demo_countdown()
    demo_even_numbers()
    demo_fibonacci()
    demo_infinite()
    demo_my_range()
    demo_reverse()
    demo_reusable()
    demo_file_iterator()
    demo_batch_iterator()
    demo_iterable_container()
    demo_filter_iterator()
    demo_chain_iterator()
    demo_iterator_vs_generator()

if __name__ == "__main__":
    main()
