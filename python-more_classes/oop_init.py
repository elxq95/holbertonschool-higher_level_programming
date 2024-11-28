"""The __init__ method is run as soon as an object of a class is instantiated (i.e. created)."""
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# THe previous 2 lines can also be written as Person('Swaroop').say_hi()
