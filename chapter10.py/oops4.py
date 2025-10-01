# Create a class with a class attribute a; create an object from it and set ‘a’directly using ‘object.a = 0’. Does this change the class attribute?

class MyClass:
    a = 5   # class attribute

# Create an object
obj = MyClass()

# Print values before changing
print("Before changing:")

print("MyClass.a =", MyClass.a)   # prints 5
print("obj.a =", obj.a)           # prints 5 (inherited from class)

# Change using object
obj.a = 4   # creates a new instance attribute, doesn't change class attribute

# Print values after changing
print("\nAfter changing:")

print("MyClass.a =", MyClass.a)   # still 5 (unchanged)
print("obj.a =", obj.a)           # now 0 (new instance variable)
