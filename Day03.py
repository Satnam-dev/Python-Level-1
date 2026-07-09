# Type casting is used to convert one data type into another .
ab="48"
print( int (ab))
print( ab)

# Used to find data type like -list 
print(type(ab))   

# Use index value,indwx start from 0
Ab="School"
print(Ab[5])
print(Ab[0:6])

# Use for loop
Ab="School"
for l in Ab:
    print(l)

# List (It ia a collection used to store multiple items in a single varible ),
# []
# Example- ab=["Navjot","Satnam","Anjali","Mannat","Amarjot"].

# 1 Used to print specific value
ab=["Navjot","Satnam","Anjali","Mannat","Amarjot"]
print(ab[2])


# 2 Used to inset value in list
a=["School","Uni","Pg","Hostel"]
a.insert(1,"Logo")
print(a)

# 3 Used to remove value in list
b=["Navjot","Satnam","Anjali","Mannat","Amarjot"]
b.remove("Navjot")
print(b)

# 4 Pop (Used to remove last element)
ab=["Navjot","Satnam","Mannat","Anjali"]
ab.pop()
print(ab)

# Features/Charact,eristics 

# 1.Mutable(Changeable)
ab=["Navjot","Satnam","Anjali","Mannat","Amarjot"]
ab[0]="Armaan"
print(ab)

# 2.Ordered

# 3.Allow duplicate values.
ab=["Navjot","Satnam","Anjali","Mannat","Satnam"]
print(ab)
print(type(ab))
 



# Tuples(It is a collection used to store multiple items in a single variable)
# ()
# Example- ab=("table","chair",4,5,5)
ab=("table","chair",4,5,5)
print(ab)
print(type(ab))


# 1.Immutable(Cannnot be changed)
# 2.Ordered
# 3.Allow duplicte value
# 4.Support indexing


# Set(Collection of unique items)
# {} 
# Example- ab={"school","university","Pg"}
ab={"Satnam","Navjot","Armaan","Satnam",1,2}
print(ab)
print(type(ab))

# Used to Add
ab={"Satnam","Navjot","Armaan","Satnam",1,2}
ab.add("Anjali")
print(ab)

# Used to remove
ab={"Satnam","Navjot","Armaan","Satnam",1,2}
ab.remove("Armaan")
print(ab)

# 1.Mutable
# 2.Unordered
# 3.No duplicates allowed 
# 4.No Indexting

# Dictionary (It is collection of data stored in Key:value pairs)
# 1.Mutable
# 2.Ordered
# 3.No duplicate keys

Student={"id":"41","Name":"Satnam","Calss":"BTech","Roll Number":"2301003284"}
print(Student)
print(Student["id"])

# Add
Student["Name"]="Navjot"
print(Student)

# Delete
del Student["Name"]
print(Student)