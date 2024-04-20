#OOP INHERITANCE
"""
#1. Specifying a Superclass with class definition
 
class A(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        return 10*self.x

class B(A):
    def g(self):
        return 1000*self.x

print(A(5).f()) 
print(B(7).g()) 
print(B(7).f()) 
print(A(5).g()) 

"""
#2. Overriding Methods

"""
Polymorphism: Same method name, different execution body
    Choosing the right way to accomplish a task

    Method overriding: Same signature, different classes
    Method overloading: Same name and return type, different number of parameters

class A(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        return 10*self.x
    def g(self):
        return 100*self.x

class B(A):
    def __init__(self, x=42, y=99):
        super().__init__(x) # call overridden init!
        self.y = y
    def f(self):
        return 1000*self.x
    def g(self):
        return (super().g(), self.y)

a = A(5)
b = B(7)
print(a.f()) 
print(a.g()) 
print(b.f()) 
print(b.g())



Dynamic Binding
    1. Compiler looks at the static source code
    2. Method overloading can be detected by the compiler
        x = sum(3, 4)
        y = sum(3, 4, 5)
    3. Runtime Environment must make decisions during execution time
        Ex. Taking input from user
        Ex. Assigning null references to new objects
    4. Type of class and method to be called 
       for the implicit parameter may be determined during runtime
"""

class A(object):
    def __init__(self, x):
        self.x = x
    def f(self):
        return 10*self.x
    def g(self):
        self.f()
        return 100*self.x

class B(A):
    def __init__(self, x=42, y=99):
        super().__init__(x) # call overridden init!
        self.y = y
    def f(self):
        print("hello")
        return 1000*self.x
    def g(self):
        return (super().g(), self.y)

a = A(5)
b = B(7)
print(b.g())