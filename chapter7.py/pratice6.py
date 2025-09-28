n = int(input("enter your num:"))

for i in range(1,n+1):
    if(i ==1 or i == n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")


for i in range(1,11):
    print(f"{n} x {11-i} = {n*(11-i)}")