class Dog:

    # class attribute
    type = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print("My name is {}".format(self.name))

    def eat(self, snack):
        print(f'I am eating {snack}')

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
print(Dog.type)

# Accessing class methods
Rodger.speak()
Tommy.speak()
Tommy.eat("biscuits")