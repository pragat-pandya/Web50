def annaounce (f):
  def wrapper():
    print("About to run the function")
    f()
    print("Done with the function")
  return wrapper

@annaounce
def hello():
  print("Hello, World!")


hello()