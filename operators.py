# Operators are used to perform operations on variables and values.

# ***Arithmetic Operators***

# Addition
print(10 + 5)

# Subtraction
print(10 - 5)

# Multiplication
print(10 * 5)

# Division
print(10 / 5)

# Modulus
print(10 % 4)

# Exponentiation
print(10 ** 5)

# Floor division
print(10 // 5)

# ***Assignment Operators***
a = 5

print(a)

b = 6
b += 3
print(b)

c= 6
c -= 3
print(c)

d = 6
d *= 3
print(d)

e = 6
e /= 3
print(e)

f = 6
f %= 3
print(f)

g = 6
g **= 3
print(g)

h = 6
h //= 3
print(h)

i = 6
i &= 3
print(i)

j = 6
j |= 3
print(j)

k = 6
k ^= 3
print(k)

l = 6
l >>= 3
print(l)

m = 6
m <<= 3
print(m)

# ***Comparison Operators***

n = 5
o = 3

print(n == o)

p = 5
q = 3

print(p != q)

r = 5
s = 3

print(r > s)

t = 5
u = 3

print(t < u)

v = 5
w = 3

print(v > w)

x = 5
y = 3

print(x < y)

# ***Logical Operators***

z = 5

print(z > 3 and z < 10)

a1 = 5

print(a1 < 3 or a1 > 10)

a2 = 5

print(not(a2 > 3 and a2 < 10))

# ***Identity Operators***

a3 = ["apple", "banana"]
a4 = ["apple", "banana"]
a5 = a3

print(a3 is a5)

# returns True because a5 is the same object as a3

print(a3 is a4)

# returns False because a3 is not the same object as a4, even if they have the same content

print(a3 == a4)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because a3 is equal to a4

a6 = ["apple", "banana"]
a7 = ["apple", "banana"]
a8 = a6

print(a6 is not a8)

# returns True because a8 is the same object as a6

print(a6 is not a7)

# returns False because a6 is not the same object as a7, even if they have the same content

print(a6 != a7)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because a6 is equal to a7

# ***Membership Operators***

a9 = ["apple", "banana"]

print("banana" in a9)

# returns True because a sequence with the value "banana" is in the list

a10 = ["apple", "banana"]

print("orange" not in a10)

# returns True because a sequence with the value "banana" is in the list