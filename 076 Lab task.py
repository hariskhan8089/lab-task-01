076 Lab task # 01
Task 1: 
print ('"we are learning", he said.')
print ('he said,',' "I\'m learning."')


Task 2:
pie=3.14;
radius= 3.12;
circle = 3.14 *(3.12*3.12)
print ("the area circle is:")
print (circle)
 
Task 3:
first=input("enter your first name:")
last=input("enter your last name:")
sap_id = input("enter you sap id: ")

print (last,first)
print (sap_id)


task 4:

#task 04
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : ")) 
# iterating till the range
for i in range(0, n):
    ele = int(input("enter element:"))
    # adding the element
    lst.append(ele) 
  
print(lst)

def Average(lst):
    return sum(lst) / len(lst)
 
average = Average(lst)
 
# Printing average of the list
print("Average of the list =", (average))


# Creating an empty list
lst = []

# Number of elements as input
n = int(input("Enter number of elements: "))

# Iterating to get the elements
for i in range(0, n):
    ele = int(input("Enter element: "))  # Prompt the user to enter an element
    lst.append(ele)

# Reversing the list using the reverse method
reversed_lst = list(reversed(lst))

# Printing the reversed list
print("Reversed list:", reversed_lst)