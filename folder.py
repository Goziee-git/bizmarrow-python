class MyClass:
    count = []
    def __init__(self, *args, **kwargs):
       self.fname = args[0]
       self.lname = args[1]
       self.favourite = kwargs['sport']

    def hobby(self, location):
        self.location = "Nigeria"
        return MyClass.count.append(self.location)

class Pclass:
    fname = "John"
    lname = "Praise"


# Create instances
obj1 = MyClass("Jane", "Doe", sport="football")
obj2 = MyClass("Alice", "Smith", sport="basketball")
obj3 = Pclass()

# Create tuple of instances
object1 = (obj1, obj2, obj3)

# Loop through tuple and print fname values
print("=== Looping through tuple ===")
for i in object1:
    print(i.fname)

# Create tuple of fname values
fname_tuple = tuple(i.fname for i in object1)
print(f"\nTuple of fname values: {fname_tuple}")
