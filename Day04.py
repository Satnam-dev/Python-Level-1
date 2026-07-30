# Functions with parameter
def std_name():
    print("Satnam")
std_name()

# 
def std_name(a,b):
    c=a+b
    print(c)
std_name(5,6)

# We use " " for string
def std_name(Name):
    print(Name)
std_name("Armaan")    

# 
def std_name(Name):
    print(Name)
std_name("Navjot")    
std_name("Navjot")

# Functions using return keywords
def std_name(q,l):
    area=q*l
    return area
print(std_name(4,5))

# 
def std_name(q,l):
    area=q*l
    return area
A=std_name(6,6)
print(A)

# 
def std_name():
    a=int (input("Enter first value"))
    b=int (input("Enter second value"))
    area=a*b
    return area
a=std_name()
print(a)

# 
a=int (input("Enter first value"))
b=int (input("Enter second value"))
def std_name(a,b):
    area=a*b
    print(area)
std_name(a,b)

# 
a=int (input("Enter first value"))
b=int (input("Enter second value"))
def std_name(a,b):
    sum=a+b
    print(sum)
std_name(a,b)

# Lamda function lamda(x) argument(x):Expression(x)
Satnam= lambda a : a*a
print(Satnam(8))

Satnam= lambda a,b : a*b
print(Satnam(8,4))

# File Handling
# Either Txt  csv Json file
# Exit , malupulation, write, Read, Store, Create,Update,Save
# touch data.txt(Make new file)
# mkdir data
# We made a file in Terminal using touch data.txt after that we use this code to see what written in that file in terminal.
file = open("data.txt","r")
s= file.read()
print(s)
file.close()
# Write 
file = open("data.txt","w")
s= file.write("I'm 20 year old")
print(s)
file.close()
# Use echo "Hello" > data.txt(use in terminal) ,it clear all data
# echo "My name is satnam" >> data.txt (used to add new lines)
# cat data.txt (use in terminal)
# rm data.txt(Remove file)
# used to remove file without terminal
import os 
os.remove("data.txt")