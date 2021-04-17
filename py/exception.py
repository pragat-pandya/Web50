import sys

try:
  x = int(input("x: "))
  y = int(input("y: "))
except ValueError:
  print("Error: Invalid input for an Integer")
  sys.exit(1)

try:
  x/y
except ZeroDivisionError:
  print("y is 0, cannot divide by zero.")
  # Exit the program
  sys.exit(1)

print(f"{x}/{y} = {x/y}")

