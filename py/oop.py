# Class that difines a point type and constructor for x and y coordinates
class Point():
  def __init__ (self, x, y):
    self.x = x
    self.y = y


#p = Point(1,2)
#print(p.x)
#print(p.y)

class Flight():
  
  # Constructor
  def __init__ (self, capacity):
    self.capacity = capacity
    self.passengers = []
  
  # Method for adding passengers to flight
  def add_passenger (self, name):
    if len(self.passengers) < self.capacity:
      self.passengers.append(name)
      return True
    else:
      return False

people = ["Rahul", "Amit", "Pratik", "Divesh", "Nidhish"]
nyc = Flight(4)

for folk in people:
  if nyc.add_passenger(folk):
    print(f"{folk} added to the flight")
  else:
    print(f"Sorry, no room in flight for {folk}")
