class ConstructorDemo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_data(self):
        print(f"The {self.name} and {self.age} is set in constructor")


obj = ConstructorDemo("Gowtham", 29)
obj.print_data()
print(obj.name)