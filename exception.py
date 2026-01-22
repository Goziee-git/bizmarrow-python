def divide_by(x, y):
   return x / y

def divide_by(x, y):
   try:
      return divide_by(x, y)
   except ZeroDivisionError:
      return 1000000000000000

print("Safe 3 / 2 = {0:g}".format(divide_by(3, 2)))
print(f"Safe 3 / 2 = {0:g}".format(divide_by(3, 2)))