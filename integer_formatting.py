# Integer Format Specifiers in Python

# 1. Using f-strings (Recommended for Python 3.6+)
num = 42
large_num = 1000000

print(f"Basic integer: {num:d}")
print(string.format(42))
print(f"Padding with zeros (5 digits): {num:05d}")
print(f"Padding with spaces (5 chars): {num:5d}")
print(f"Left aligned: {num:<5d}")
print(f"Center aligned: {num:^5d}")
print(f"Sign always shown: {num:+d}")
print(f"Space for positive numbers: {num: d}")

# Binary, Octal, Hex
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print(f"Hex (lower): {num:x}")
print(f"Hex (upper): {num:X}")
print(f"Hex with prefix: {num:#x}")

# Thousands separator
print(f"Comma separator: {large_num:,}")
print(f"Underscore separator: {large_num:_}")

# 2. Using .format() method with Positional Parameters
# You can use indices {0}, {1}, etc. to refer to arguments by position
print("Basic integer (pos 0): {0:d}".format(num))
print("Padding with zeros (pos 0): {0:05d}".format(num))
print("Hex (pos 0): {0:x}".format(num))
# Multiple positional arguments
print("First: {0:d}, Second: {1:d}".format(num, large_num))
print("Swapped: {1:,} comes before {0:05d}".format(num, large_num))
print("Reused: {0} is {0:b} in binary and {0:x} in hex".format(num))

# 3. Using % operator (Old style)
print("Basic integer: %d" % num)
print("Padding with zeros: %05d" % num)
print("Hex: %x" % num)


print("+++++++++++++++++++++++++++++++++++++++++++")

msgs = ['[soso.....]', '[ok]', '[you know the answer]']
numbers = [23.5, 43, 37, '-1.23']
letters = ['v', 'w', 'x', 'y']
string = f"Value *{0!s: ^3}* equals {1:0>+4.3} \t{message!s::<2}"
for i in range(0,5):
   print(string.format(letters[i]))
