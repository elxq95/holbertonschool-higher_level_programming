class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

# __init__ is initializer or constructor
    def __init__(self, name): #this is a method that belongs to the class
        """Initializes the data."""
        # self is a reference to the current instance of the class.
        # When self is used inside a class, it allows you to access or modify 
        # the attributes and methods of that particular instance.
        # self makes it possible to distinguish between attributes that belong 
        # to the instance and those that might be temporary or belong to another instance.
        self.name = name
        # self.name = name creates an attribute called name for the instance.
        # The left side, self.name, refers to the instance attribute name.
        # The right side, name, refers to the parameter passed to __init__.
        # This line assigns the value of name (from the argument) to self.name, 
        # so that the instance has a name attribute with that value.
        print("(Initializing {})".format(self.name)) 
        # The .format() method replaces {} in the string with the value inside the parentheses.
        # In this case, self.name is the value passed into .format().
        # self.name is an attribute of the object instance
        # it gets its value from the __init__ method, which assigns self.name based on
        # argument passed when the object is created.


        # When this person is created, the robot
        # adds to the population
        # Instead of Robot.population, we could have also used self.__class__.population 
        # because every object refers to its class via the self.__class__ attribute.
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod #the @classmethod decorator tells Python that how_many is a class method

    # Unlike regular instance methods, which operate on individual instances of a class, 
    # class methods operate on the class itself.
    # Class methods take cls as their first parameter, which is a reference to the class itself, 
    # not to an instance (whereas instance methods take self).
    def how_many(cls): #cls is the class itself - cls would refer to Robot
        #it allows the class method to access class-level variables and other class methods.
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))
        # cls.population is a class attribute named population.
        # Class attributes are shared across all instances of the class, 
        # meaning they are common to all objects created from this class.



droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
