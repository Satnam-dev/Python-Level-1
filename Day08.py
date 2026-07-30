# Oops
# Polymorphism :- Same method(fxn) but different behaviour
# One interface to be used for different datatypes and objects

class Dog:
    def Sound(self):
        print("Barking")
class Cat:
    def Sound(self):
        print("Meow Meow")
d=[Dog(),Cat()]
for d in d:
    d.Sound()        

# Abstraction ;- Hidding implemenation detail and show only esential features .

from abc import ABC , abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car is started")
d=Car()
d.start()               

# super() keyword:- it's used to called the parent class constructor/method from child class.

class Person:
    def __init__(self,name): #__init__=constructor
        self.name=name
class student(Person):
    def __init__(self,name,rollno):
        super().__init__(name)
        self.rollno=rollno
s=student("Satnam",3284 ) 
print(s.name)      
print(s.rollno)


# Class variable Vs Instance variable, class varible create inside the the class (student) and instance varible create outside the class like s1,s2

class School():
    student="Satnam"
s=School()
print(s.student)


class student():
    def __init__(self,name):
        self.name=name
s1= student("Satnam") 
s2= student("Navjot")       
print(s1.name)
print(s2.name)


#

class Employee:
    company="Corptube"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name:- {self.name}") 
        print(f"Salary:- {self.salary}")   
class Developer(Employee):
    def __init__(self,name,salary,tech):
        super().__init__(name,salary)
        self.tech=tech
    def display(self):
        super().display()   
        print(f"Tech:- {self.tech}")
s=Developer("Satnam",0,"Cyber")        
s.display()
print(s.company)