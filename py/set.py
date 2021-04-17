# Sets in python are consistent with the mathematical concepts of the set theory
# Unordered listing of unique elements

# set() initializes an empty set

s = set()

# We can add/remove elements using following methods defined on set object

s.add(1)
s.add(2)
s.add(5)
s.add(1)

# Will have the element 1 only once
print (s)

s.remove(1)
print(s)

#len() gives the number of elements in any python sequence
print(f"This set contains {len(s)} elements.")

# Sets in  python: Ordered-NO, Mutable-N/A