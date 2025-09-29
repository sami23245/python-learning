#problem 3
#3 Write a function to calculate the factorial of a given number.

def fac(n):
    if n == 0 or n == 1:
        return 1
    return n * fac(n-1)
print(fac(5))