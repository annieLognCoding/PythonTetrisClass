class Dog:

    # class attribute
    type = "mammal"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        print("My name is {}".format(self.name)) 
        #f"My name is {self.name}"

    def eat(self, snack):
        print(f'{self.name} is eating {snack}')

# Driver code
# Object instantiation
Rodger = Dog("Rodger", 3)
Tommy = Dog("Annie", 5)

Tommy.speak()

# Accessing class methods
Rodger.speak()
Tommy.speak()
Rodger.eat("biscuits")