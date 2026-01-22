# Class is a template for creating an object. Contains the data and methods that are functions describing what can be done with the data

class Cars:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def getCar(self):
        return f"The vehicle has a {self.color} color and is a product from {self.brand}"

class Automobile(Cars):
    def __init__(self, brand, color, model, engine):
        super().__init__(brand, color)
        self.model = model
        self.engine = engine

    def getEngine(self):
        print(f"This is a new {self.model} with a {self.engine} engine")


Car1 = Cars("volvo", "black")
print("* ============OBJECT FOR CARS CLASS ===========*")
print(Car1.brand, Car1.color)

Car2 = Automobile("peugeot", "brown", "premium", "v8")
print("* ============OBJECT FOR AUTOMOBILE CLASS ===========*")
print(Car2.brand, Car2.color, Car2.model, Car2.engine)
