class Calculator:
    
    def square_root(self,n):
        
        x = (n) ** 0.5 #find square root of variable
        
        return x
    
    def square(self,n): #find square of num
        
        x = n * n
        
        return x
    
    def cube(self,n): # find factorial of num
        
        x = (n) * n * n
        
        return x
    def greed(self):
        print("hello bro")
    
cal = Calculator()
print(cal.greed())