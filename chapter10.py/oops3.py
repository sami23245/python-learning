import math

class calculator:
    
    def square_root(self,n):
        
        x = math.sqrt(num) #find square root of variable
        
        return x
    
    def square(self,n): #find square of num
        
        x = n * n
        
        return x
    
    def factorial(self,n): # find factorial of num
        
        x = math.factorial(n)
        
        return x
    
    def cube(self,n): #find cube of number
        
        x = n * n * n
        
        return x
    
    
num = int(input("Enter a number: "))

print("this program can find square root, square , factorial and cube of function ")

print("for square root enter 1")
print("for square enter 2")
print("for factorial enter 3")
print("for cube root enter 4")

method = int(input("enter method in which you want your answer: "))

# Create object of Calculator class
calc = calculator()

if method == 1:
    print(f"This is square root of {num} = ",calc.square_root(num))
elif method == 2:
    print(f"This is square of {num} = ",calc.square(num))
elif method == 3:
    print(f"This is factorial of {num} = ",calc.factorial(num))
else:
    print(f"This is cube of {num} = ",calc.cube(num))


