# Opps - Object oriented programming..... it help to organise programming using object and class
# Class - it is a template or blue print or we can say collection of oject called class. or 
# we can say it's a blup rint of object.
# object -it's a real instances of the class.
class Student:
    pass
Student1 = Student()
Student2 = Student()

print(Student1)
print(Student2)

#Constructor 
# __init__
#It's special member fuction that is automatically called when object is created.
#it's is used to initilalize the data memeber of an object.
class Student:
    def __init__(self):
        print("Student Created")
s1=Student()
s2=Student()

class Student:
    def __init__(self,Name,RollNO):
        self.Name=Name
        self.RollNO=RollNO
s1=Student("Satnam",23001003284)

print(s1.RollNO)
print(s1.Name)

# Inheritance= It is used to derive a class from base class and inherits the properties of base class into derived class.
# Derived class= It's also called child class.
# Base class= It is also called parent class.
# Single inheritance= It has only one derived class from one base class.
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    def bark(self):
        print("Dog is barking")
d=Dog()
d.eat()
d.bark()        

# Multi-level inheritance 
# In this a class is derived from another derived class.
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog(Animal):
    pass
class Cat(Dog):
    pass

d=Cat()
d.eat()

# Multiple inheritance
# One class derived from two or more parent classes
class Animal:
    def eat(self):
        print("Animal is eating")
class Dog():
    def bark(self):
        print("Dog is barking")
class Cat(Animal,Dog):
    pass        
d=Cat()
d.eat()
d.bark()        