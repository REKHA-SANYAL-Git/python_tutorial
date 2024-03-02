# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

# To create a class, use the keyword class:

class MyClass:
    x=5

print(MyClass)

# Create object

p1=MyClass()
print(p1.x)

# The _init_() function on a class

class Person:
    def __init__(self,name,age):
        self.name= name
        self.age= age
p2= Person("Rekha",24)

print(p2.name)
print(p2.age)

# The __init__() function is called automatically every time the class is being used to create a new object.

p3= Person("Priti",27)

print(p3.name)
print(p3.age)

# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.


class Place:
  def __init__(self, name,location):
    self.name = name
    self.location = location

  def __str__(self):
    return f"{self.name}({self.location})"

p4 = Place("Alipore zoo", 'kolkata')

print(p4)

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Poem:
   def __init__(self,name,author):
      self.name = name
      self.author = author

   def mypoem(self):
      print("My Favourite Poem is "+self.name+" composed by "+self.author) 

p5= Poem("Mrityunjay","Rabindranath Tagore")

p5.mypoem()

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# Modify Object Properties
class Colour:
  def __init__(self, name):
    self.name = name

  def mycolour(self):
    print("Hello my favorite colour is " + self.name)

p6 = Colour("Black")

p6.name = "Green"

print(p6.name)
p6.mycolour()

# Delete Object Properties
class Machine:
  def __init__(self, name, count):
    self.name = name
    self.count = count

  def mymachine(self):
    print("Hello I have "+ self.name)

p7 = Machine("Machine", 1)

del p7.age

print(p7.age)

# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Nocontent:
   pass