import math

class Calculator:
    
    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def squareroot(self, n):
        return n ** 0.5


# Take input from user
num = int(input("Enter a number: "))

# Create object of Calculator class
calc = Calculator()

# Call methods
print("Square:", calc.square(num))
print("Cube:", calc.cube(num))
print("Square Root:", calc.squareroot(num))
