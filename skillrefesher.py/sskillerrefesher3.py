#calculator 

num1 = float(input("enter first number: "))

num2 = float(input("enter secoand number: "))

print("enter method from(+,-,*,/)")

method = str(input("enter method: "))

if method == '+':
    print(num1 + num2)
elif method == '-':
    print(num1 - num1)
elif method == '*':
    print(num1 * num1)
else:
    print(num1 / num2)

