# Define a class circle
class circle:
# Define constructor that takes list as arguement
  def __init__(self, list):
# Assign list to variable
    self.list = list
# Print list
    print("The list is:", self.list)
# Create list of numbers
list = [10, 501, 22, 37, 100, 999, 87, 351]
# Create an instance of circle class with the list as arguement
c = circle(list)
