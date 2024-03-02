# Python does not have built-in support for Arrays, but Python Lists can be used instead.

# create an array
cars = ["Ford", "Volvo", "BMW"]

print(cars)

# What is an Array?
  # An array is a special variable, which can hold more than one value at a time.

# Access the element with indexing
x = cars[0]

print(x)

# Modify the element with indexing
cars[0]='Toyota'
print(cars)

# Length of an array
  # The length of an array is always one more than the highest array index.
x = len(cars)

print(x)

# Looping array elements

# for in loop
for x in cars:
  print(x)

# Adding array elements
  # use append() method to add element to the end of an array
  
cars.append('Honda')
print(cars)

  #use insert() method to add element at specified position on an array

cars.insert(0,'Lamborgini')
# Removing array elements
  # use pop()method to remove element from an array

cars.pop(2)
print(cars)

  # use remove()method to remove the first item with the specified value

cars.remove('Toyota')
print(cars)

# copy() method
vehicles=cars.copy()
print(vehicles)

# count() method
number=cars.count("Volvo")
print(number)

# extend() method
houses=['hut','flat','bunglow']
houses.extend(cars)
print(houses)

# index() method
position=houses.index('flat')
print(position)

# Use reverse() method to reverse the list
houses.reverse()
print(houses)

# Use the sort() to sort the list
  # Ascending method

cars.sort()
print(cars)

  # Descending method

cars.sort(reverse=True)
print(cars)

# Use clear() method to clear the whole array

cars.clear()
print(cars)
