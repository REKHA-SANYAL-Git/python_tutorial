thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.
"""

"""
Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
"""

"""
Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
"""

"""
Allow Duplicates
Since lists are indexed, lists can have items with the same value:
"""
thislist2 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist2)

# list length

thislist3 = ["apple", "banana", "cherry", "orange"]
print(len(thislist3))

"""
List Items - Data Types
List items can be of any data type: Same or different
"""
list1 = ["apple", "banana", "cherry"]
list2 = [1, "rose", True, 9, "potato"]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# type of list

mylist = ["apple", "banana", "cherry"]

print(type(mylist))
"""
The list() Constructor
It is also possible to use the list() constructor when creating a new list.
"""
thislist4 = list(("bottle", "laptop", "bag")) # note the double round-brackets
print(thislist4)

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""
#access list items

thislist5 = list(("bottle", "laptop", "bag")) # note the double round-brackets
print(thislist5[0])
print(thislist5[-1])
print(thislist5[-2])
print(thislist5[2:3])
print(thislist5[:1])
print(thislist5[1:])
print(thislist5[-2:-1])
"""Check if Item Exists
To determine if a specified item is present in a list use the in keyword:"""
thislist6 = ["apple", "banana", "cherry"]
if "apple" in thislist6:
  print("Yes, 'apple' is in the fruits list")

"""
Change Item Value
To change the value of a specific item, refer to the index number:
"""
thislist7 = ["apple", "banana", "cherry"]
thislist7[1] = "blackcurrant"
print(thislist7)  

thislist8 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist8[1:3] = ["blackcurrant", "watermelon"]
print(thislist8)

thislist9 = ["apple", "banana", "cherry"]

thislist9[1:2] = ["blackcurrant", "watermelon"]

print(thislist9)

thislist10 = ["apple", "banana", "cherry"]

thislist10[1:3] = ["watermelon"]

print(thislist10)

#insert method
thislist11 = ["apple", "banana", "cherry"]

thislist11.insert(2, "watermelon")

print(thislist11) 