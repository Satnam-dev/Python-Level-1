# OPERATORS
# Arithmetic Operators
# 1
a=4
b=3
c=a+b
print("The value of c=",c)
# 2
a=8
b=2
c=a/b
print(c)

# 3
a=8
b=2
c=a*b  # Asterisk (*)
print(a)

# 4
a=2
b=4
c=a**b  # Asterisk ((2x2x2x2)=16)
print(a)

# Assignment Operator
a=4
b="Satnam"
c=a==b
print("The value of c",c)


# = (Used to assign values)
a=10
print(a)

# ==(Equality Operator,Used to compare to values)
a=5
b=10
print(a==b)
print(a==5)

# Logical Operators

# and (Both conditions must be true)
a=True
b=False
c= a and b
print(c)

# or (At least one condition is true)
a=True
b=False
c= a or b
print(c)

#  not (reverse condition (Used to change true to false and false to true))
a=True
b=False
c= not a
print(c)

#  Loops (While, for loops)

#  While
i=1 
while (i<=10):
    print(i)
    i += 1

i=10
while(i>=1):
    print(i)
    i -= 1

# for Loop (End point never print)
for i in range(2,6):
    print(i)

for i in range(12,14):
    print(i)

# Conditional Statements

# if-else
a =5
if(a>6):
   print("true")
else:
    print("false")


a=20
if(a>18):
    print("He can vote",a)
else :
    print("Invalid")


# Sum of all natural number upto 10
# using while loop
total=0
i=1
while(i<=10):
    total= total +i
    i=i+1
    print(total)

#  if elif else(Nested loop)
b=float(input("Enter the Marks: "))
if(90<=b):
    print("Grade A")
elif(80<=b and 90>b):
    print("Grade b")
elif(60<=b and 80>b):
    print("Grade C")
elif(33<=b and 60>b):
    print("Grade B")
else:
    print("Faliure")

# Strings ()