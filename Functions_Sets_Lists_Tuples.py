# Basic Functions, Sets, Lists & Tuples
# Function -- Defintion and call
def CompareNum1(Val1, Val2):
    if int(Val1) >= int(Val2):
        print (str(Val1) + ' is greater than ' + str(Val2))        
    else:
        print (str(Val2) + ' is greater than ' + str(Val1))

CompareNum1(120,110)        

def CompareNum2(Val1 = "10", Val2 = "15"):
    if int(Val1) >= int(Val2):
        print (str(Val1) + ' is greater than ' + str(Val2))
    else:
        print (str(Val2) + ' is greater than ' + str(Val1))

CompareNum2()

# Find the Number of Arguements
def ArgFinder(ArgCount=0, *VarArgs): #VarArgs -- To List All the arguements    
    print('Number of Arguements Are ' + str(ArgCount))
    print(VarArgs[0] + ' ' + str(VarArgs[1]) + ' ' + VarArgs[2])

ArgFinder(3, 'Say', 2, 'Hello')

# to pass optional Arguements to a Function -- compare VarArgs = VarArgs[0]

# Sets & Lists (Tuple is a List) --> Storing Data In Memory
# Importing Set Library
# Sets should not contain Duplicate Entrees
from sets import Set
SetA = Set(['Karthik','Dhanu','Iyal','Iyal'])
SetB = Set(['Chicago','Minneapolis','Dallas'])
SetC = SetA.union(SetB)

print SetC #one 'Iyal' is de-duped

# Lists
ListA = [0, 4, 8]
ListB = [1, 3, 6]
ListA.extend(ListB)
ListA.append(6)

print ListA
print ListA[1:4]

# List May contain Duplicate Entrees

# Tuples -- create complex Lists (Lists are mutable tuples are not)
SampTup = (1,2,3,(4,5,6,(7,8,9)))

print SampTup

# Print Tuple in Levels (Hierarchy)
for Val1 in SampTup:
    if type(Val1) == int: #type to identify the data type of an element
        print Val1
    else:
        for Val2 in Val1:
            if type(Val2) == int:
                print "\t", Val2
            else:
                for Val3 in Val2:
                    print "\t\t", Val3

