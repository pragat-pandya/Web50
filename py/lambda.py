#def square(x):
 # return x*

# Square function using lambda
#
#square = lambda x: x*x
#for i in range(1,11):
#  print(square(i))  
#
#

people = [
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Cho", "house": "Ravenclaw"},
  {"name": "Draco", "house": "Slytherin"}
]

# Sorting dictionary by name 
#
#def f(people):
#  return people["name"]
#people.sort(key=f)
#print(people)
#
#

# Sorting dictoinary by name using lambda
#
people.sort(key=lambda person:person["name"])
print(people)
#
#