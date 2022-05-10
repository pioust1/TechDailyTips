"""

Shallow and deep copy differences
assignment operation that creates references to the same object and not create copies
one needs to identify how to make real copies of data (only for mutable objects)
"""
import copy as cp

x_one = [1, 56, 90, 2]
"""
copy the value through assignment operator
"""
y_one = x_one

print(f"x_one  {x_one} and type is {type(x_one)}")
print(f"y_one  {x_one} and type is {type(y_one)}")
# modify the value for x and add a value to y
x_one[0] = 20

print(f"x_one changed {x_one} and type is {type(x_one)}")
print(f"y_one changed  {x_one} and type is {type(y_one)}")

y_one.append(3)

print(f"x_one append {x_one} and type is {type(x_one)}")
print(f"y_one append  {x_one} and type is {type(y_one)}")

"""
Create shallow copies of the x using list/dict/set factory function
"""

x_two = [[1, 3, 5], ["old value", "test", "new"], 90, 2]
y_two = list(x_two)

print(f"x_two  {x_two} and type is {type(x_two)}")
print(f"y_two   {y_two} and type is {type(y_two)}")

x_two[0][1] = 201

print(f"x_two modified {x_two} and type is {type(x_two)}")
print(f"y_two  modified  {y_two} and type is {type(y_two)}")

x_two[1][1] = "updated test"
print(f"x_two modified {x_two} and type is {type(x_two)}")
print(f"y_two  modified {y_two} and type is {type(y_two)}")

y_two.append(5)

print(f"x_two append {x_two} and type is {type(x_two)}")
print(f"y_two  append {y_two} and type is {type(y_two)}")
"""
since we created the shallow copy of the object the second level child objects are changed again if modified in the main
copy.
to create deep copy
use the module copy
"""

x_three = [[1, 3, 5], ["old value", "test", "deep copy orig"], ["adding-new-value"], 2]
y_three = cp.deepcopy(x_three)

print(f"x_three deep copy orig  {x_three} and type is {type(x_three)}")
print(f"y_three  deep copy orig {y_three} and type is {type(y_three)}")

x_three[1][1] = "updated-test"

print(f"x_three deep copy updated  {x_three} and type is {type(x_three)}")
print(f"y_three  deep copy updated {y_three} and type is {type(y_three)}")
